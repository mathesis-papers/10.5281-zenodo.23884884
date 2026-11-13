import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import json
from math import comb
from pathlib import Path

import verify


def adjoint(matrix):
    metric = [comb(8, index) for index in range(9)]
    return [[matrix[column][row] * Fraction(metric[column], metric[row])
             for column in range(9)] for row in range(9)]


def enumerated_reduction(probabilities):
    multiplicity = Counter(word.bit_count() for word in range(256))
    result = [Fraction(0) for index in range(8)]
    for word in range(256):
        weight = word.bit_count()
        retained_weight = (word >> 1).bit_count()
        result[retained_weight] += probabilities[weight] / multiplicity[weight]
    return result


def crosscheck():
    unit = verify.identity()
    raising = verify.zero()
    for column in range(1, 9):
        raising[column - 1][column] = Fraction(9 - column)
    lowering = adjoint(raising)
    spin_z = verify.diagonal([Fraction(4 - index) for index in range(9)])
    operators = [
        (Fraction(1, 1540), verify.add(verify.scale(3, verify.multiply(spin_z, spin_z)),
                                     verify.scale(-20, unit))),
        (Fraction(3, 3080), verify.add(verify.multiply(spin_z, raising),
                                     verify.multiply(raising, spin_z))),
        (Fraction(3, 3080), verify.add(verify.multiply(spin_z, lowering),
                                     verify.multiply(lowering, spin_z))),
        (Fraction(3, 3080), verify.multiply(raising, raising)),
        (Fraction(3, 3080), verify.multiply(lowering, lowering)),
    ]
    normalization = verify.zero()
    for coefficient, operator in operators:
        normalization = verify.add(normalization, verify.scale(
            coefficient, verify.multiply(adjoint(operator), operator)))
    assert normalization == unit

    def sparse_channel(matrix):
        result = verify.zero()
        for coefficient, operator in operators:
            result = verify.add(result, verify.scale(coefficient, verify.multiply(
                verify.multiply(operator, matrix), adjoint(operator))))
        return result

    cartesian = [verify.scale(Fraction(1, 2), verify.add(raising, lowering)),
                 verify.scale(Fraction(1, 2), verify.add(raising, verify.scale(-1, lowering))),
                 spin_z]
    quadrupoles = []
    for first in range(3):
        for second in range(3):
            y_count = int(first == 1) + int(second == 1)
            operator = verify.scale(Fraction(1, 2), verify.add(
                verify.multiply(cartesian[first], cartesian[second]),
                verify.multiply(cartesian[second], cartesian[first])))
            if y_count == 2:
                operator = verify.scale(-1, operator)
            if first == second:
                operator = verify.add(operator, verify.scale(Fraction(-20, 3), unit))
            quadrupoles.append((-1 if y_count == 1 else 1, operator))
    identities = 0
    for row in range(9):
        for column in range(9):
            matrix_unit = verify.zero()
            matrix_unit[row][column] = Fraction(1)
            cartesian_output = verify.zero()
            for sign, operator in quadrupoles:
                cartesian_output = verify.add(cartesian_output, verify.scale(
                    Fraction(3 * sign, 770), verify.multiply(
                        verify.multiply(operator, matrix_unit), operator)))
            assert sparse_channel(matrix_unit) == cartesian_output
            identities += 1
    initial = [Fraction(value, 1764) for value in [209, 92, 560, 0, 441, 0, 294, 168, 0]]
    output_matrix = sparse_channel(verify.diagonal(initial))
    output = [output_matrix[index][index] for index in range(9)]
    assert output_matrix == verify.diagonal(output)
    for probabilities in [initial, output]:
        assert enumerated_reduction(probabilities) == verify.reduce_diagonal(probabilities, 7)
    before = verify.trace_norm_from_uniform(enumerated_reduction(initial))
    after = verify.trace_norm_from_uniform(enumerated_reduction(output))
    assert (after - before) / Fraction(7, 4) == Fraction(95, 90552)
    return {
        'status': 'all assertions passed',
        'arithmetic': 'exact fractions',
        'five_vs_nine_kraus_matrix_identities': identities,
        'five_kraus_completeness': True,
        'enumerated_bitstrings_per_state': 256,
        'states_reduced_by_enumeration': 2,
        'input_trace_norm': str(before), 'output_trace_norm': str(after),
        'anticoherence_decrease': str((after - before) / Fraction(7, 4)),
        'independence_scope': 'Distinct five-Kraus and bitstring formulations; matrix primitives shared with verify.py.',
        'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    arguments = parser.parse_args()
    result = json.dumps(crosscheck(), indent=2) + '\n'
    if arguments.output:
        arguments.output.write_text(result)
    print(result, end='')


if __name__ == '__main__':
    main()
