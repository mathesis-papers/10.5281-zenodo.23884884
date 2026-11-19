# Can symmetric noise make a state less directionless?

Imagine eight identical quantum two-level systems, called qubits. Instead of tracking which particular qubit is in state 1, consider states that treat every permutation of the qubits alike. There are nine basic symmetric patterns: zero ones, one one, and so on up to eight ones. Their quantum state space is also the space of a single spin-four particle.

The question is whether noise that respects every spatial rotation must make such a state more directionless. For one proposed score, **the answer is no**. Haobo Ma and Wenlin Zhang reconstruct a spin-four example for which rotation-respecting noise lowers the order-seven trace-distance anticoherence score by exactly

$$
\frac{95}{90552}.
$$

That small decrease is decisive: a rule asserting that the score never decreases is a universal statement, so one admissible exception disproves it. The example uses a mixed state, meaning a probabilistic mixture rather than one pure quantum state. It addresses the full mixed-state definition, which allows retaining seven out of eight qubits.

## A score built from a smaller view

First consider an ordinary probability list. A fair eight-outcome die has probabilities $1/8$ in every slot. To measure a list's departure from fairness, add its absolute deviations from $1/8$. A list can move closer to uniform in some slots and farther away in others; the total decides.

A quantum state is described by a density matrix: a positive semidefinite matrix whose trace is one. Its eigenvalues form a probability list. For a diagonal matrix, the diagonal entries themselves are that list. Off-diagonal entries contain quantum coherence, so a general density matrix carries more information than a classical distribution.

To examine order $t$, discard $8-t$ qubits mathematically, by a partial trace. Write the retained state as $\rho_t$. Because the original state is symmetric, the retained symmetric space has $t+1$ basic patterns. The reference state is $I/(t+1)$, equally weighted on those patterns. Here $I$ is the identity matrix on that space. This is uniformity on the **symmetric space**, whose dimension is $t+1$, rather than on the full $2^t$-dimensional qubit space.

The candidate score is

$$
\begin{aligned}
A_t(\rho)&=1-\frac{\|\rho_t-I/(t+1)\|_1}{K_t},\\
K_t&=\frac{2t}{t+1}.
\end{aligned}
$$

The trace norm $\|X\|_1$ adds the singular values of $X$; for the diagonal Hermitian differences in this example, it adds absolute diagonal entries. The constant $K_t$ is the largest possible distance of a state from the uniform reference. Thus a smaller distance gives a larger score. The complete definition and normalization argument appear in [the precise statements](statements.md#setting).

## What does rotation-respecting noise mean?

A quantum channel is a linear transformation of states that preserves total probability and remains positive even when an untouched auxiliary system is present. Those requirements are called trace preservation and complete positivity. They ensure that the transformation is legitimate quantum noise.

Rotation covariance says that rotating first and applying the noise gives the same result as applying the noise first and then rotating. It is a statement about how the channel treats directions. It does not say that the noise consists of choosing a rotation at random.

J. Denis, T. Lacaille, J. Martin and E. Serrano-Ensástiga proposed that the score should satisfy

$$
A_t(\Phi(\rho))\geq A_t(\rho).
$$

for every such covariant channel $\Phi$, every density matrix and every mixed-state order $1\leq t\leq N=2j$. Their discussion after Proposition 2 in arXiv:2605.29436v1 left the trace-distance case open, supported by numerical evidence. The present paper supplies an exact counterexample to that proposed property, called axiom (T4).

## The counterexample becomes arithmetic

The nine input probabilities, in order of the number of ones, are

$$
\begin{aligned}
p&=v/1764,\\
v&=(209,92,560,0,441,\\
&\qquad 0,294,168,0).
\end{aligned}
$$

All are nonnegative and their numerators add to 1764. Several are positive, so this diagonal state is mixed. The channel is built from quadratic combinations of the three spin components. Summing over all Cartesian directions makes its rotational symmetry visible; a separate identity proves its probability normalization. The [construction and proof](statements.md#construction) give these matrices explicitly.

Why can we reduce eight qubits to seven using school arithmetic? In a symmetric pattern with $r$ ones, the discarded qubit is 1 with probability $r/8$ and 0 with probability $(8-r)/8$. To retain exactly $k$ ones, either start with $k$ and discard 0, or start with $k+1$ and discard 1. Therefore

$$
\begin{aligned}
p_k^{(7)}&=\frac{8-k}{8}p_k+\frac{k+1}{8}p_{k+1},\\
&0\leq k\leq7.
\end{aligned}
$$

For instance, the first retained probability is $209/1764+(92/1764)/8=1/8$. Carrying this out for input and output gives two eight-entry distributions, displayed on separate lines:

$$
p^{(7)}=\frac1{168}(21,21,40,21,21,21,21,2).
$$

$$
\begin{aligned}
q^{(7)}&=w/517440,\\
w&=(69468,87252,64205,82635,\\
&\qquad 78360,59892,43533,32095).
\end{aligned}
$$

In the input, six entries already equal $1/8=21/168$. The remaining entries deviate by $+19/168$ and $-19/168$. In the output, the uniform comparison numerator is $64680$. Adding the absolute deviations yields

$$
D_{\mathrm{in}}=\frac{19}{84},
$$

$$
D_{\mathrm{out}}=\frac{3933}{17248}.
$$

The output is slightly farther from uniform:

$$
D_{\mathrm{out}}-D_{\mathrm{in}}=\frac{95}{51744}>0.
$$

Since $K_7=7/4$, subtracting the normalized distance from one reverses this increase:

$$
A_7(\Phi(\rho))-A_7(\rho)=-\frac{95}{90552}<0.
$$

The essential point is the sign, certified by fractions rather than a floating-point approximation. The [explicit-witness theorem](statements.md#exact-decrease) proves all the channel hypotheses as well as the strict decrease.

## Where the intuitive argument breaks

Trace distance contracts under a quantum channel. That familiar principle compares two states acted on by the **same channel on the same space**. Here the score is measured after discarding qubits. Rotation covariance of the nine-level channel does not provide a channel on seven-qubit reductions that reproduces its action for every input. That missing passage is where the tempting proof fails.

There are two instructive controls. If the noise really is a probabilistic mixture of rotations, each rotation passes through the partial trace, and convexity of the trace norm gives the proposed inequality. At full order $t=8$, the channel fixes the uniform spin-four state, so ordinary trace-norm contraction also gives the inequality. The counterexample occupies the gap between those facts. Their arguments are given in [the boundary cases](statements.md#boundaries).

A focused film follows the probabilities and the missing passage between the full and reduced systems.

::: {.film src="001-symmetry-and-distance"}
Symmetry, reduction and the exact sign of the counterexample. English narration with aligned Chinese and English subtitles.
:::

## How far does the answer reach?

For this same state and channel, the trace-distance score increases at orders $1,2,3,4,5,6,8$ and decreases at order 7. A different candidate, based on fidelity, increases at all eight orders. The [all-order proposition](statements.md#sibling-orders) gives exact trace changes and rational certificates for the fidelity signs. A single successful test of fidelity does not prove its universal monotonicity.

The paper leaves open the universal fidelity question, the trace-distance question restricted to mixed-state orders $t\leq N/2$, and pure-input violations in the usual range $t\leq j$. It does not determine the smallest spin or order at which a violation can occur. The source's established purity and Hilbert–Schmidt results remain valid. Its convex-roof proposition is conditional on the total score satisfying the axioms; the counterexample shows that this hypothesis fails for the trace-distance candidate on the full mixed-state domain.

The public Lean theorem proves that the universal mixed-state trace-distance assertion is false; see [@universal-refutation]. The explicit normalized value and the additional manuscript statements are distinguished in the precise chapter. The witness was already present in the [upstream formal source](lean:D5/S3/Quantum/Measurement/AnticoherenceTraceDistanceRefutation.result); Ma and Zhang supply a self-contained Cartesian-tensor reconstruction and exact calculation of it.

The aligned seminar presentation develops this same argument, with technical details in its appendix.

::: {.slides src="seminar"}
Academic presentation with speaker notes in Chinese and English.
:::

See [sources and contributions](sources.md) for the exact paper version, original literature and focused formalization tasks.
