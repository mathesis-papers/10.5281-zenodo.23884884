# Trace-distance anticoherence counterexample

This package reconstructs the spin-four, order-seven counterexample to the
trace-distance case of axiom (T4) in Denis, Lacaille, Martin and
Serrano-Ensástiga, *Total, quantum, and classical measures of anticoherence
for mixed spin states*, arXiv:2605.29436v1, Sections II.B and III.A.2.

## Contents

- `note.tex`: the main source, including its bibliography and complete proof.
- `metadata.json`: scientific identity, byline, license and source attribution.
- `verify.py` and `verification.json`: exact rational channel and reduction checks.
- `crosscheck.py` and `crosscheck.json`: five/nine-Kraus comparison and bitstring reductions.
- `siblings.py` and `siblings.json`: all eight orders and rigorous fidelity enclosures.

## Rebuild

Use Python 3.10 or newer. The mathematical checkers use only its standard
library. From this directory run:

```sh
python3 verify.py --output verification.json
python3 crosscheck.py --output crosscheck.json
python3 siblings.py --output siblings.json
```

Compile `note.tex` with Tectonic 0.17.0:

```sh
tectonic --untrusted note.tex
```

Alternatively, compile directly with `pdflatex`, providing `geometry`, `amsmath`,
`amssymb`, `amsthm`, `booktabs` and `hyperref`:

```sh
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error note.tex
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error note.tex
```

Run enough passes to resolve references. No external bibliography file is needed.

Each checker must print `all assertions passed`. The first two recover the
order-seven trace norms `19/84` and `3933/17248` and the anticoherence decrease
`95/90552`. The sibling checker proves, with exact integer-square-root bounds,
that this witness increases the fidelity candidate at all orders 1 through 8.
For trace-distance anticoherence its change is positive at orders 1–6 and 8
and negative at order 7. Full rational reductions and enclosures are in JSON.

## Scientific attribution and verification scope

The input and channel are the existing witness in:

https://github.com/the-omega-institute/trureturing/blob/d1876cfbbef8c13023311126691b180eefa69569/D5/S3/Quantum/Measurement/AnticoherenceTraceDistanceRefutation.lean

Its declaration `result` states `not claim`. The note supplies a readable
Cartesian-tensor proof, sparse channel evaluation, Dicke reductions and
finite sibling-order comparison of that witness. It does not claim discovery
of a different counterexample. The declaration covers the mixed-state
trace-distance claim; the sibling-order statements are finite exact checks.

`verify.py` works in a rational similarity basis and checks trace preservation,
generator covariance, metric adjoints and the exact witness. The analytic proof
in the note establishes covariance for every SU(2) rotation. `crosscheck.py`
uses the five-Kraus representation on all 81 matrix units and enumerates
256 bitstrings for each order-seven reduction. It shares matrix primitives
with `verify.py`; this is not an independent software stack. `siblings.py`
uses that program's binomial reduction function and integer `isqrt` to bound
each square root at scale 10^15. Its positive fidelity lower bounds are rigorous,
not floating-point estimates or a universal fidelity-monotonicity theorem.

The counterexample defeats the universally quantified mixed-state trace-distance
candidate; it does not disprove the conditional Proposition 6, the fidelity
candidate, or the proved purity/Hilbert–Schmidt constructions. Universal
restricted-order and pure-input behavior and minimum spin/order are not settled.

The note and its scientific metadata carry the license CC BY 4.0.
