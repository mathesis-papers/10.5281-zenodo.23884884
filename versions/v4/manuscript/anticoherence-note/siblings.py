import argparse
from fractions import Fraction
import hashlib
import json
from math import isqrt
from pathlib import Path

import verify


def root_bounds(probability, scale):
    numerator = isqrt(probability.numerator * scale * scale // probability.denominator)
    lower = Fraction(numerator, scale)
    upper = Fraction(numerator + 1, scale)
    assert lower * lower <= probability < upper * upper
    return lower, upper


def fidelity_bounds(probabilities, scale):
    roots = [root_bounds(probability, scale) for probability in probabilities]
    lower = (sum(pair[0] for pair in roots) ** 2 - 1) / (len(probabilities) - 1)
    upper = (sum(pair[1] for pair in roots) ** 2 - 1) / (len(probabilities) - 1)
    return lower, upper


def check_siblings():
    initial = [Fraction(value, 1764) for value in [209, 92, 560, 0, 441, 0, 294, 168, 0]]
    output = [Fraction(value, 194040) for value in
              [22288, 30100, 25528, 13149, 45540, 10584, 24654, 11613, 10584]]
    scale = 10 ** 15
    rows = []
    for retained in range(1, 9):
        before = verify.reduce_diagonal(initial, retained)
        after = verify.reduce_diagonal(output, retained)
        normalizer = Fraction(2 * retained, retained + 1)
        trace_change = (verify.trace_norm_from_uniform(before)
                        - verify.trace_norm_from_uniform(after)) / normalizer
        before_bounds = fidelity_bounds(before, scale)
        after_bounds = fidelity_bounds(after, scale)
        lower = after_bounds[0] - before_bounds[1]
        upper = after_bounds[1] - before_bounds[0]
        displayed = Fraction((lower * 10 ** 6).__floor__(), 10 ** 6)
        displayed_upper = Fraction((upper * 10 ** 6).__ceil__(), 10 ** 6)
        assert 0 < displayed <= lower < upper
        assert upper <= displayed_upper
        assert trace_change >= 0 if retained != 7 else trace_change == -Fraction(95, 90552)
        rows.append({'t': retained, 'input_reduction': list(map(str, before)),
                     'output_reduction': list(map(str, after)),
                     'trace_anticoherence_change': str(trace_change),
                     'fidelity_change_lower_bound': str(displayed),
                     'fidelity_change_upper_bound': str(displayed_upper),
                     'fidelity_displayed_lower_bound': str(displayed)})
    return {'status': 'all assertions passed', 'root_scale': '10**15',
            'arithmetic': 'exact rational square-root enclosures using integer isqrt',
            'output_precision': 'Exact interval endpoints rounded outward to multiples of 10**-6.',
            'formula': 'A_F=(sum(sqrt(p_k))**2-1)/t; trace change is output minus input',
            'scope': 'This one mixed-state witness at every t=1,...,8; not a universal fidelity theorem.',
            'shared_dependency': 'Dicke binomial reductions from verify.py', 'rows': rows,
            'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    arguments = parser.parse_args()
    result = json.dumps(check_siblings(), indent=2) + '\n'
    if arguments.output:
        arguments.output.write_text(result)
    print(result, end='')


if __name__ == '__main__':
    main()
