import argparse
from fractions import Fraction
import hashlib
import json
from math import comb
from pathlib import Path


DIMENSION = 9
RATIONAL = Fraction


def zero():
    return [[RATIONAL(0) for column in range(DIMENSION)] for row in range(DIMENSION)]


def identity():
    result = zero()
    for index in range(DIMENSION):
        result[index][index] = RATIONAL(1)
    return result


def add(left, right):
    return [[left[row][column] + right[row][column] for column in range(DIMENSION)]
            for row in range(DIMENSION)]


def scale(coefficient, matrix):
    return [[coefficient * entry for entry in row] for row in matrix]


def multiply(left, right):
    result = zero()
    for row in range(DIMENSION):
        for inner in range(DIMENSION):
            if left[row][inner]:
                for column in range(DIMENSION):
                    if right[inner][column]:
                        result[row][column] += left[row][inner] * right[inner][column]
    return result


def commutator(left, right):
    return add(multiply(left, right), scale(-1, multiply(right, left)))


def diagonal(entries):
    result = zero()
    for index, entry in enumerate(entries):
        result[index][index] = entry
    return result


def trace(matrix):
    return sum(matrix[index][index] for index in range(DIMENSION))


def reduce_diagonal(probabilities, retained):
    return [sum(probabilities[weight] * RATIONAL(comb(retained, index)
                * comb(8 - retained, weight - index), comb(8, weight))
                for weight in range(9) if 0 <= weight - index <= 8 - retained)
            for index in range(retained + 1)]


def trace_norm_from_uniform(probabilities):
    return sum(abs(entry - RATIONAL(1, len(probabilities))) for entry in probabilities)


def verify():
    unit = identity()
    raising, lowering = zero(), zero()
    for index in range(1, DIMENSION):
        raising[index - 1][index] = RATIONAL(9 - index)
        lowering[index][index - 1] = RATIONAL(index)
    spin_z = diagonal([RATIONAL(4 - index) for index in range(DIMENSION)])
    spin_x = scale(RATIONAL(1, 2), add(raising, lowering))
    imaginary_y = scale(RATIONAL(1, 2), add(raising, scale(-1, lowering)))
    assert commutator(spin_z, raising) == raising
    assert commutator(spin_z, lowering) == scale(-1, lowering)
    assert commutator(raising, lowering) == scale(2, spin_z)
    assert add(add(multiply(spin_x, spin_x), scale(-1, multiply(imaginary_y, imaginary_y))),
               multiply(spin_z, spin_z)) == scale(20, unit)
    cartesian = [spin_x, imaginary_y, spin_z]
    quadrupoles = []
    for first in range(3):
        for second in range(3):
            y_count = int(first == 1) + int(second == 1)
            entry = scale(RATIONAL(1, 2), add(multiply(cartesian[first], cartesian[second]),
                                            multiply(cartesian[second], cartesian[first])))
            if y_count == 2:
                entry = scale(-1, entry)
            if first == second:
                entry = add(entry, scale(RATIONAL(-20, 3), unit))
            sign = -1 if y_count == 1 else 1
            quadrupoles.append((sign, entry))
    metric = [comb(8, index) for index in range(DIMENSION)]
    for sign, entry in quadrupoles:
        for row in range(DIMENSION):
            for column in range(DIMENSION):
                assert metric[row] * entry[row][column] == sign * metric[column] * entry[column][row]

    def channel(matrix):
        result = zero()
        for sign, entry in quadrupoles:
            result = add(result, scale(sign, multiply(multiply(entry, matrix), entry)))
        return scale(RATIONAL(3, 770), result)

    assert channel(unit) == unit
    covariance_checks = 0
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            matrix_unit = zero()
            matrix_unit[row][column] = RATIONAL(1)
            transformed = channel(matrix_unit)
            assert trace(transformed) == trace(matrix_unit)
            for generator in [spin_z, raising, lowering]:
                assert channel(commutator(generator, matrix_unit)) == commutator(generator, transformed)
                covariance_checks += 1
    initial = [RATIONAL(value, 1764) for value in [209, 92, 560, 0, 441, 0, 294, 168, 0]]
    expected = [RATIONAL(value, 194040) for value in
                [22288, 30100, 25528, 13149, 45540, 10584, 24654, 11613, 10584]]
    assert min(initial) >= 0 and sum(initial) == 1
    output = channel(diagonal(initial))
    assert output == diagonal(expected)
    assert min(expected) >= 0 and sum(expected) == 1
    shifts = [0, -1, 1, -2, 2]
    sparse_output = [RATIONAL(0) for index in range(DIMENSION)]
    for index, probability in enumerate(initial):
        magnetization = 4 - index
        upward = 20 - magnetization * (magnetization + 1)
        downward = 20 - (magnetization - 1) * magnetization
        weights = [RATIONAL((3 * magnetization ** 2 - 20) ** 2, 1540),
                   RATIONAL(3 * (2 * magnetization + 1) ** 2 * upward, 3080),
                   RATIONAL(3 * (2 * magnetization - 1) ** 2 * downward, 3080),
                   RATIONAL(3 * upward * (20 - (magnetization + 1) * (magnetization + 2)), 3080),
                   RATIONAL(3 * downward * (20 - (magnetization - 2) * (magnetization - 1)), 3080)]
        assert min(weights) >= 0 and sum(weights) == 1
        for shift, weight in zip(shifts, weights):
            if 0 <= index + shift < DIMENSION:
                sparse_output[index + shift] += probability * weight
            else:
                assert weight == 0
    assert sparse_output == expected
    initial_reduced = reduce_diagonal(initial, 7)
    output_reduced = reduce_diagonal(expected, 7)
    assert initial_reduced == [RATIONAL(value, 168) for value in [21, 21, 40, 21, 21, 21, 21, 2]]
    assert output_reduced == [RATIONAL(value, 517440) for value in
                              [69468, 87252, 64205, 82635, 78360, 59892, 43533, 32095]]
    assert sum(initial_reduced) == sum(output_reduced) == 1
    initial_distance = trace_norm_from_uniform(initial_reduced)
    output_distance = trace_norm_from_uniform(output_reduced)
    assert initial_distance == RATIONAL(19, 84)
    assert output_distance == RATIONAL(3933, 17248)
    assert output_distance - initial_distance == RATIONAL(95, 51744)
    normalizer = RATIONAL(7, 4)
    decrease = (output_distance - initial_distance) / normalizer
    assert decrease == RATIONAL(95, 90552) > 0
    return {'status': 'all assertions passed', 'arithmetic': 'exact fractions; no floating point',
            'matrix_units_checked': 81, 'infinitesimal_covariance_identities': covariance_checks,
            'trace_preservation_identities': 81, 'unitality': True,
            'quadrupole_metric_adjoint_identities': 729,
            'input_density': list(map(str, initial)), 'output_density': list(map(str, expected)),
            'input_reduction': list(map(str, initial_reduced)),
            'output_reduction': list(map(str, output_reduced)),
            'input_trace_norm': str(initial_distance), 'output_trace_norm': str(output_distance),
            'trace_norm_increase': str(output_distance - initial_distance),
            'normalizer': str(normalizer), 'anticoherence_decrease': str(decrease),
            'input_anticoherence': str(1 - initial_distance / normalizer),
            'output_anticoherence': str(1 - output_distance / normalizer),
            'verification_scope': 'Finite exact matrix identities plus the analytic proof in note.tex.',
            'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    arguments = parser.parse_args()
    result = json.dumps(verify(), indent=2) + '\n'
    if arguments.output:
        arguments.output.write_text(result)
    print(result, end='')


if __name__ == '__main__':
    main()
