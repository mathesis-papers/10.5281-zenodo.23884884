# Sources and contributions

This book explains version 4 of the public paper by Haobo Ma and Wenlin Zhang: [exact-version DOI 10.5281/zenodo.23884885](https://doi.org/10.5281/zenodo.23884885). The [concept DOI 10.5281/zenodo.23884884](https://doi.org/10.5281/zenodo.23884884) groups versions. The paper and this explanation are provided under CC BY 4.0. Haobo Ma is affiliated with Chrono AI, Singapore; Wenlin Zhang with the National University of Singapore and Chrono AI, Singapore.

## Research context

- J. Denis, T. Lacaille, J. Martin and E. Serrano-Ensástiga, *Total, quantum, and classical measures of anticoherence for mixed spin states*, [arXiv:2605.29436v1](https://arxiv.org/abs/2605.29436v1), [DOI](https://doi.org/10.48550/arXiv.2605.29436). Section II.B, equations (7)–(8), states (T4); Section III.A.2, equation (22) at $p=1$, is the trace-distance candidate. Section III.A.3, equation (26), gives the fidelity candidate. The convex-roof result in Section III.B.2, Proposition 6, assumes that the total score satisfies the axioms.
- D. Baguette and J. Martin, *Anticoherence measures for pure spin states*, Physical Review A **96**, 032304 (2017), [DOI](https://doi.org/10.1103/PhysRevA.96.032304). This supplies context for pure-state scores.
- T. Aschieri, B. Ruba and J. P. Solovej, *SU(2)-equivariant quantum channels: semiclassical analysis*, Communications in Mathematical Physics **405**, 298 (2024), [DOI](https://doi.org/10.1007/s00220-024-05178-1). The present channel normalization and covariance arguments are direct calculations and do not use a classification theorem from that work.

## Mathematical evidence and contribution opportunities

[@universal-refutation] corresponds to the public Lean theorem negating the universal assertion on the full mixed-state range. The [formal source](lean:D5/S3/Quantum/Measurement/AnticoherenceTraceDistanceRefutation.result) already contains the witness and proofs of its admissibility, output and reduced distances; the paper reconstructs that existing witness. The exact normalized decrement, general-spin identity and all-order comparison retain their written proofs and the following shared requests:

- [Exact decrement: reuse the existing witness and distances, adding the normalizer equality and a usable statement](https://github.com/the-omega-institute/trureturing-requests/issues/250), [@exact-decrease].

- [General spin quadrupole identity: an independent algebraic result](https://github.com/the-omega-institute/trureturing-requests/issues/251), [@quadrupole-normalization].

- [All-order comparison: reuse the output and reductions and certify fidelity signs](https://github.com/the-omega-institute/trureturing-requests/issues/252), [@sibling-orders].

Coordinate the scope on the corresponding request, then submit a focused PR from a contributor fork directly to [trureturing dev](https://github.com/the-omega-institute/trureturing/blob/dev/docs/CONTRIBUTING.md), following its existing admission and review rules. The already proved universal negation needs no duplicate proof.

