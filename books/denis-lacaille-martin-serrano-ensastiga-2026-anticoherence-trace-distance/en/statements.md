# Precise statements and proofs

## Setting {#setting}

Let $N\geq1$ be an integer and $j=N/2$. Work on the $(N+1)$-dimensional symmetric subspace of $N$ qubits, in the normalized Dicke basis $|D_N^r\rangle$, $0\leq r\leq N$. A density matrix is positive semidefinite with trace one. The reduction $\rho_t$ is the ordinary partial trace over $N-t$ qubits, expressed in the normalized symmetric basis. For $1\leq t\leq N$, set

$$
A_t(\rho)=1-\frac{\|\rho_t-I/(t+1)\|_1}{K_t},
$$

$$
K_t=\max_{\sigma\geq0,\,\operatorname{Tr}\sigma=1}
\|\sigma-I/(t+1)\|_1=\frac{2t}{t+1}.
$$

The norm is unhalved. To prove the last equality, diagonalize $\sigma$ and write its eigenvalue probability vector as a convex combination of simplex vertices. Convexity bounds the distance by its value $2t/(t+1)$ at any vertex. Each vertex is a density matrix attaining the bound. In particular $K_t>0$ for $t\geq1$; $t=0$ is excluded. Halving both the norm and its maximum gives the same score.

Call $\Phi$ covariant when it is completely positive, trace preserving, and

$$
\Phi(U X U^\dagger)=U\Phi(X)U^\dagger.
$$

for every matrix $X$ and every spin-$j$ representation $U$ of a single-qubit SU(2) rotation.
::: {.theorem #universal-refutation title="Failure of universal monotonicity" mathesis="collected:denis-lacaille-martin-serrano-ensastiga-2026-anticoherence-trace-distance:4:s1" lean="D5/S3/Quantum/Measurement/AnticoherenceTraceDistanceRefutation.result"}
It is false that for every integer $N\geq1$, every integer $1\leq t\leq N$, every covariant channel $\Phi$ as above and every density matrix $\rho$, one has $A_t(\rho)\leq A_t(\Phi(\rho))$.
:::

::: proof
The public formal declaration is exactly the negation of this universal assertion. The explicit witness below explains its mechanism; the exact normalized decrement is a separate statement.
:::

## The explicit construction {#construction}

Take $N=8$. Order the basis by $r=0,\ldots,8$ and take out-of-range basis vectors as zero:

$$
\begin{aligned}
J_z|r\rangle&=(4-r)|r\rangle,\\
J_+|r\rangle&=\sqrt{r(9-r)}|r-1\rangle.
\end{aligned}
$$

$$
\begin{aligned}
J_-&=J_+^\dagger,\\
J_x&=(J_++J_-)/2,\\
J_y&=(J_+-J_-)/(2i).
\end{aligned}
$$

$$
\begin{aligned}
Q_{ab}&=\frac12(J_aJ_b+J_bJ_a)-\frac{20}{3}\delta_{ab}I,\\
&\qquad a,b\in\{x,y,z\}.
\end{aligned}
$$

$$
\Phi(X)=\frac3{770}\sum_{a,b}Q_{ab}XQ_{ab}.
$$

$$
\begin{aligned}
\rho&=\operatorname{diag}(v)/1764,\\
v&=(209,92,560,0,441,\\
&\qquad 0,294,168,0).
\end{aligned}
$$
::: {.theorem #exact-decrease title="Exact decrease for the spin-four witness" mathesis="collected:denis-lacaille-martin-serrano-ensastiga-2026-anticoherence-trace-distance:4:s1" status="written-proof" proof="pf-exact-decrease" doi="10.5281/zenodo.23884885" source="Theorem 1" request="https://github.com/the-omega-institute/trureturing-requests/issues/250"}
The displayed $\Phi$ is completely positive, trace preserving and SU(2)-covariant; $\rho$ is a mixed density matrix, and

$$
A_7(\Phi(\rho))-A_7(\rho)=-\frac{95}{90552}<0.
$$

Consequently the trace-distance candidate fails (T4) on the full mixed-state domain.
:::

::: {.proof #pf-exact-decrease}
By [@quadrupole-normalization] below, $\sum Q_{ab}^2=(770/3)I$. Thus $\sqrt{3/770}Q_{ab}$ are normalized Kraus operators: the operator-sum expression gives complete positivity and normalization gives trace preservation. All $Q_{ab}$ are Hermitian, so the channel is also unital.

For every spin rotation $U$ there is a real orthogonal matrix $R$ with $UJ_aU^\dagger=\sum_cR_{ac}J_c$. Hence

$$
UQ_{ab}U^\dagger=\sum_{c,d}R_{ac}R_{bd}Q_{cd}.
$$

Insert this in the channel sum. The two orthogonality contractions $\sum_aR_{ac}R_{ae}=\delta_{ce}$ and $\sum_bR_{bd}R_{bf}=\delta_{df}$ leave $\Phi(UXU^\dagger)$. This proves covariance for every rotation and every matrix. The state entries are nonnegative, sum to one and have more than one positive entry, proving mixedness.

The exact channel evaluation and partial-trace derivation are in [the calculation appendix](#calculation). They give

$$
\|\rho_7-I/8\|_1=\frac{19}{84},
$$

$$
\|[\Phi(\rho)]_7-I/8\|_1=\frac{3933}{17248}.
$$

$$
\frac{3933}{17248}-\frac{19}{84}=\frac{95}{51744}.
$$
Divide by the positive $K_7=7/4$ and use the minus sign in the score to obtain the exact decrement. This expands the manuscript Theorem 1 and Sections 2–3.
:::
::: {.lemma #quadrupole-normalization title="Quadrupole normalization for general spin" mathesis="collected:denis-lacaille-martin-serrano-ensastiga-2026-anticoherence-trace-distance:4:s2" status="written-proof" proof="pf-quadrupole-normalization" doi="10.5281/zenodo.23884885" source="Lemma 1" request="https://github.com/the-omega-institute/trureturing-requests/issues/251"}
Let finite-dimensional Hermitian spin operators satisfy $[J_a,J_b]=i\sum_c\epsilon_{abc}J_c$ and $\sum_aJ_a^2=CI$, where $C=j(j+1)$. Set $S_{ab}=(J_aJ_b+J_bJ_a)/2$ and $Q_{ab}=S_{ab}-(C/3)\delta_{ab}I$. Then

$$
\sum_{a,b}Q_{ab}^2=\frac{C(4C-3)}6 I.
$$
:::

::: {.proof #pf-quadrupole-normalization}
The commutation relations and contraction of the Levi-Civita symbols give $\sum_a[J_a,[J_a,J_b]]=2J_b$. Expanding the left side gives $2CJ_b-2\sum_aJ_aJ_bJ_a$, so $\sum_aJ_aJ_bJ_a=(C-1)J_b$. Expand the four terms of the symmetrized product and pair them by renaming indices:

$$
\begin{aligned}
\sum_{a,b}S_{ab}^2
&=\frac12\sum_{a,b}(J_aJ_bJ_aJ_b+J_aJ_b^2J_a)\\
&=\frac12\bigl(C(C-1)+C^2\bigr)I.
\end{aligned}
$$
Now use $\sum_aS_{aa}=CI$ and subtract the scalar trace part:

$$
\begin{aligned}
\sum_{a,b}Q_{ab}^2
&=\left(C^2-\frac C2-\frac{C^2}3\right)I\\
&=\frac{C(4C-3)}6I.
\end{aligned}
$$
At spins zero and one-half the right side is zero and the identity remains valid; one cannot divide by this coefficient to normalize a channel there. For spin four, $C=20$ gives $770/3>0$. Source: manuscript Lemma 1.
:::

## Calculation appendix: from operators to probabilities {#calculation}

Put $c=\sqrt{3/3080}$. The same channel is $\Phi(X)=\sum_qL_qXL_q^\dagger$, where

$$
L_0=(3J_z^2-20I)/\sqrt{1540},
$$

$$
\begin{aligned}
L_{+1}&=-c(J_zJ_++J_+J_z),\\
L_{-1}&=c(J_zJ_-+J_-J_z),
\end{aligned}
$$

$$
L_{+2}=cJ_+^2,\qquad L_{-2}=cJ_-^2.
$$

To verify equality with the Cartesian sum, use $Q_{xx}+Q_{yy}=-Q_{zz}$, $J_zJ_\pm+J_\pm J_z=2(Q_{xz}\pm iQ_{yz})$ and $J_\pm^2=Q_{xx}-Q_{yy}\pm2iQ_{xy}$. For Hermitian $A,B$,

$$
\begin{aligned}
&(A+iB)X(A-iB)+(A-iB)X(A+iB)\\
&\hspace{2em}=2AXA+2BXB.
\end{aligned}
$$
With $D=Q_{xx}-Q_{yy}$, also

$$
Q_{xx}XQ_{xx}+Q_{yy}XQ_{yy}
=\frac12(DXD+Q_{zz}XQ_{zz}).
$$
After cancellation of the plus/minus cross terms, the coefficients of $Q_{zz}XQ_{zz}$, $DXD$, and each distinct off-diagonal symmetric component $Q_{ab}XQ_{ab}$ are $9/1540$, $3/1540$, and $3/385$, respectively, agreeing with the Cartesian expression.

Each input column of each $L_q$ has one possible output. At $m=4-r$, the shifts and squared amplitudes are below; out-of-range amplitudes vanish:

- $L_0$: $r\mapsto r$, $(3m^2-20)^2/1540$.
- $L_{+1}$: $r\mapsto r-1$, $3(2m+1)^2[20-m(m+1)]/3080$.
- $L_{-1}$: $r\mapsto r+1$, $3(2m-1)^2[20-m(m-1)]/3080$.
- $L_{+2}$: $r\mapsto r-2$, $3[20-m(m+1)][20-(m+1)(m+2)]/3080$.
- $L_{-2}$: $r\mapsto r+2$, $3[20-m(m-1)][20-(m-1)(m-2)]/3080$.
Multiply each input probability by the corresponding weight and sum by output position to obtain

$$
\begin{aligned}
\Phi(\rho)&=\operatorname{diag}(u)/194040,\\
u&=(22288,30100,25528,13149,45540,\\
&\qquad 10584,24654,11613,10584).
\end{aligned}
$$
The reduction formula follows from normalized Dicke splitting:

$$
|D_N^r\rangle=\sum_k
\sqrt{\frac{\binom tk\binom{N-t}{r-k}}{\binom Nr}}
|D_t^k\rangle\otimes|D_{N-t}^{r-k}\rangle.
$$
The numerator counts strings with $k$ ones in the first block and $r-k$ in the second, out of all weight-$r$ strings counted by the denominator. Distinct weights of the second block are orthogonal, so partial trace removes cross terms. Thus a diagonal input stays diagonal after reduction, with

$$
p_k^{(t)}=\sum_{r=0}^N p_r
\frac{\binom tk\binom{N-t}{r-k}}{\binom Nr},\qquad 0\leq k\leq t.
$$
Take out-of-range binomial coefficients as zero. For $N=8,t=7$ this becomes $p_k^{(7)}=(8-k)p_k/8+(k+1)p_{k+1}/8$. The input and output give, respectively,

$$
\rho_7=\frac1{168}\operatorname{diag}(21,21,40,21,21,21,21,2).
$$

$$
\begin{aligned}
[\Phi(\rho)]_7&=\operatorname{diag}(w)/517440,\\
w&=(69468,87252,64205,82635,\\
&\qquad 78360,59892,43533,32095).
\end{aligned}
$$
The uniform numerators are 21 and 64680. Absolute deviations sum to $38/168=19/84$ and $117990/517440=3933/17248$, completing the calculation used in [@exact-decrease].
::: {.proposition #sibling-orders title="All orders for the same witness" mathesis="collected:denis-lacaille-martin-serrano-ensastiga-2026-anticoherence-trace-distance:4:s3" status="written-proof" proof="pf-sibling-orders" doi="10.5281/zenodo.23884885" source="Proposition 1" request="https://github.com/the-omega-institute/trureturing-requests/issues/252"}
For the displayed $\rho,\Phi$, the fidelity candidate

$$
A_t^F(\sigma)=\frac{(\operatorname{Tr}\sqrt{\sigma_t})^2-1}{t}
$$

strictly increases for every integer $t=1,\ldots,8$. The trace-distance candidate strictly increases for $t=1,\ldots,6,8$ and strictly decreases for $t=7$.
:::

::: {.proof #pf-sibling-orders}
Apply the binomial reduction formula above to input and output. All changes below mean output minus input. The last column gives integer lower bounds for $10^6\Delta A_t^F$, all positive.

| $t$ | $\Delta A_t$ | $10^6\Delta A_t^F\geq$ |
|---|---|---|
| 1 | $19/784$ | 3663 |
| 2 | $4275/120736$ | 8574 |
| 3 | $2831/75460$ | 13085 |
| 4 | $4959/241472$ | 18296 |
| 5 | $741/75460$ | 26268 |
| 6 | $19/2464$ | 38910 |
| 7 | $-95/90552$ | 62258 |
| 8 | $3889/17248$ | 365375 |

The trace column uses only rational arithmetic. For fidelity put $s=10^{15}$ and, for each reduced probability $p$, set $n(p)=\lfloor\sqrt{\lfloor s^2p\rfloor}\rfloor$. Since $n(p)^2\leq s^2p<(n(p)+1)^2$,

$$
\frac{n(p)}s\leq\sqrt p<\frac{n(p)+1}s.
$$

Summing gives nonnegative bounds $L_\sigma\leq\operatorname{Tr}\sqrt{\sigma_t}<U_\sigma$. Squaring preserves the order, so

$$
\Delta A_t^F\geq
\frac{L_{\Phi(\rho)}^2-U_\rho^2}{t}.
$$

The table integers are floors of $10^6$ times these rational lower bounds, rather than rounded approximations to the actual changes. The manuscript's Proposition 1, Table 1 and exact `siblings.json` certificate give the finite evaluations. The prescription above specifies each enclosure and sign without a floating-point assumption.
:::

## Boundary cases and scope {#boundaries}

For a probabilistic mixture of rotations, $\Phi(\rho)=\sum_iw_iU_i\rho U_i^\dagger$, $w_i\geq0$, $\sum_iw_i=1$, partial trace intertwines collective rotations with retained rotations $V_i$. Thus

$$
\begin{aligned}
&[\Phi(\rho)]_t-\frac{I}{t+1}\\
&\qquad=\sum_iw_i V_i\left(\rho_t-\frac{I}{t+1}\right)V_i^\dagger.
\end{aligned}
$$

Convexity and unitary invariance of the trace norm imply $A_t(\Phi(\rho))\geq A_t(\rho)$. Since our example reverses this, its channel is outside this subclass.

At full order $t=N$, covariance makes $\Phi(I/(N+1))$ invariant. Irreducibility makes it scalar, and trace preservation fixes it as $I/(N+1)$. For Hermitian $X=X_+-X_-$ with $X_\pm\geq0$, positivity and trace preservation give

$$
\|\Phi(X)\|_1\leq\operatorname{Tr}\Phi(X_+)+\operatorname{Tr}\Phi(X_-)
=\|X\|_1.
$$

Apply this to $X=\rho-I/(N+1)$ to prove full-order monotonicity. These are the arguments in manuscript Section 4. Neither proves monotonicity for an arbitrary reduced order. The counterexample has $t=7>N/2=4$ and a mixed input. The restricted mixed-state and pure-input questions, and minimal spin/order, remain unsettled by this example.
