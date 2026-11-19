# 精确陈述与证明

## 设定 {#setting}

设整数 $N\geq1$，$j=N/2$。在 $N$ 个比特的 $(N+1)$ 维对称子空间工作，使用归一化 Dicke 基 $|D_N^r\rangle$，$0\leq r\leq N$。密度矩阵半正定，且迹等于一。$\rho_t$ 是对 $N-t$ 个比特取普通偏迹后，在归一化对称基下表示的矩阵。对 $1\leq t\leq N$，定义

$$
A_t(\rho)=1-\frac{\|\rho_t-I/(t+1)\|_1}{K_t},
$$

$$
K_t=\max_{\sigma\geq0,\,\operatorname{Tr}\sigma=1}
\|\sigma-I/(t+1)\|_1=\frac{2t}{t+1}.
$$

范数不乘二分之一。最后一个等式这样证明：将 $\sigma$ 对角化，把特征值概率向量写成概率单纯形顶点的凸组合。由凸性，距离不超过任意顶点处的值 $2t/(t+1)$。每个顶点对应的密度矩阵都取到此值。因此 $t\geq1$ 时 $K_t>0$；不包括 $t=0$。若同时将范数和最大值减半，评分不变。

称 $\Phi$ 协变，是指它完全正、保迹，且对每个矩阵 $X$ 和每个单比特 SU(2) 旋转的自旋 $j$ 表示 $U$，都有

$$
\Phi(U X U^\dagger)=U\Phi(X)U^\dagger.
$$
::: {.theorem #universal-refutation title="普遍单调性为假" mathesis="collected:denis-lacaille-martin-serrano-ensastiga-2026-anticoherence-trace-distance:4:s1" lean="D5/S3/Quantum/Measurement/AnticoherenceTraceDistanceRefutation.result"}
并非对每个整数 $N\geq1$、每个整数 $1\leq t\leq N$、每个上述协变信道 $\Phi$ 以及每个密度矩阵 $\rho$，都有 $A_t(\rho)\leq A_t(\Phi(\rho))$。
:::

::: proof
公开形式化声明恰好否定这一全称断言。下文的明确见证解释其机制；归一化下降的精确等式是另一个陈述。
:::

## 明确的构造 {#construction}

取 $N=8$。按 $r=0,\ldots,8$ 排列基，令越界基向量为零：

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
::: {.theorem #exact-decrease title="自旋四见证的精确下降" mathesis="collected:denis-lacaille-martin-serrano-ensastiga-2026-anticoherence-trace-distance:4:s1" status="written-proof" proof="pf-exact-decrease" doi="10.5281/zenodo.23884885" source="Theorem 1" request="https://github.com/the-omega-institute/trureturing-requests/issues/250"}
上述 $\Phi$ 完全正、保迹且 SU(2) 协变；$\rho$ 是混合密度矩阵，并且

$$
A_7(\Phi(\rho))-A_7(\rho)=-\frac{95}{90552}<0.
$$

因此迹距离候选量在完整混合态范围不满足 (T4)。
:::

::: {.proof #pf-exact-decrease}
由下述 [@quadrupole-normalization]，$\sum Q_{ab}^2=(770/3)I$。因此 $\sqrt{3/770}Q_{ab}$ 是满足归一化的 Kraus 算子：其算子和表达式保证完全正，归一化保证保迹。所有 $Q_{ab}$ 厄米，因此该信道也保持单位矩阵。

每个自旋旋转 $U$ 对应一个实正交矩阵 $R$，满足 $UJ_aU^\dagger=\sum_cR_{ac}J_c$，因此

$$
UQ_{ab}U^\dagger=\sum_{c,d}R_{ac}R_{bd}Q_{cd}.
$$

代入信道求和。两次正交收缩 $\sum_aR_{ac}R_{ae}=\delta_{ce}$ 和 $\sum_bR_{bd}R_{bf}=\delta_{df}$ 留下 $\Phi(UXU^\dagger)$，证明对每个旋转及每个矩阵都协变。状态的对角元非负、和为一，且有多个正项，故为混合态。

[计算附录](#calculation)给出信道精确求值和偏迹推导，得到

$$
\|\rho_7-I/8\|_1=\frac{19}{84},
$$

$$
\|[\Phi(\rho)]_7-I/8\|_1=\frac{3933}{17248}.
$$

$$
\frac{3933}{17248}-\frac{19}{84}=\frac{95}{51744}.
$$
除以正数 $K_7=7/4$，并注意评分中的负号，就得到精确下降。此证明按原稿 Theorem 1 及第 2–3 节展开。
:::
::: {.lemma #quadrupole-normalization title="一般自旋的四极归一化" mathesis="collected:denis-lacaille-martin-serrano-ensastiga-2026-anticoherence-trace-distance:4:s2" status="written-proof" proof="pf-quadrupole-normalization" doi="10.5281/zenodo.23884885" source="Lemma 1" request="https://github.com/the-omega-institute/trureturing-requests/issues/251"}
设有限维厄米自旋算子满足 $[J_a,J_b]=i\sum_c\epsilon_{abc}J_c$ 与 $\sum_aJ_a^2=CI$，其中 $C=j(j+1)$。令 $S_{ab}=(J_aJ_b+J_bJ_a)/2$，$Q_{ab}=S_{ab}-(C/3)\delta_{ab}I$。则

$$
\sum_{a,b}Q_{ab}^2=\frac{C(4C-3)}6 I.
$$
:::

::: {.proof #pf-quadrupole-normalization}
由交换关系及 Levi-Civita 符号收缩，$\sum_a[J_a,[J_a,J_b]]=2J_b$。展开左侧得到 $2CJ_b-2\sum_aJ_aJ_bJ_a$，故 $\sum_aJ_aJ_bJ_a=(C-1)J_b$。对称化乘积的四项展开后，对指标换名合并：

$$
\begin{aligned}
\sum_{a,b}S_{ab}^2
&=\frac12\sum_{a,b}(J_aJ_bJ_aJ_b+J_aJ_b^2J_a)\\
&=\frac12\bigl(C(C-1)+C^2\bigr)I.
\end{aligned}
$$
再用 $\sum_aS_{aa}=CI$，减去标量迹部分：

$$
\begin{aligned}
\sum_{a,b}Q_{ab}^2
&=\left(C^2-\frac C2-\frac{C^2}3\right)I\\
&=\frac{C(4C-3)}6I.
\end{aligned}
$$
自旋零与二分之一时右侧为零，恒等式仍成立；此时不能除以该系数来定义归一化信道。自旋四时 $C=20$，系数为 $770/3>0$。来源：原稿 Lemma 1。
:::

## 计算附录：从算子到概率 {#calculation}

令 $c=\sqrt{3/3080}$。同一个信道可写成 $\Phi(X)=\sum_q L_qXL_q^\dagger$，其中

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

为核对它与笛卡尔求和相等，使用 $Q_{xx}+Q_{yy}=-Q_{zz}$、$J_zJ_\pm+J_\pm J_z=2(Q_{xz}\pm iQ_{yz})$ 以及 $J_\pm^2=Q_{xx}-Q_{yy}\pm2iQ_{xy}$。对厄米矩阵 $A,B$，

$$
\begin{aligned}
&(A+iB)X(A-iB)+(A-iB)X(A+iB)\\
&\hspace{2em}=2AXA+2BXB.
\end{aligned}
$$
令 $D=Q_{xx}-Q_{yy}$，另有

$$
Q_{xx}XQ_{xx}+Q_{yy}XQ_{yy}
=\frac12(DXD+Q_{zz}XQ_{zz}).
$$
两组正负号交叉项抵消后，$Q_{zz}XQ_{zz}$、$DXD$、每个不同的非对角对称分量 $Q_{ab}XQ_{ab}$ 的系数依次为 $9/1540$、$3/1540$、$3/385$，与笛卡尔表达式一致。

每个 $L_q$ 的每一输入列只有一个可能输出。设 $m=4-r$，以下分别列出位移和振幅平方；越界振幅为零：

- $L_0$: $r\mapsto r$, $(3m^2-20)^2/1540$.
- $L_{+1}$: $r\mapsto r-1$, $3(2m+1)^2[20-m(m+1)]/3080$.
- $L_{-1}$: $r\mapsto r+1$, $3(2m-1)^2[20-m(m-1)]/3080$.
- $L_{+2}$: $r\mapsto r-2$, $3[20-m(m+1)][20-(m+1)(m+2)]/3080$.
- $L_{-2}$: $r\mapsto r+2$, $3[20-m(m-1)][20-(m-1)(m-2)]/3080$.
将输入概率乘相应权重，再按输出位置相加，得到

$$
\begin{aligned}
\Phi(\rho)&=\operatorname{diag}(u)/194040,\\
u&=(22288,30100,25528,13149,45540,\\
&\qquad 10584,24654,11613,10584).
\end{aligned}
$$
约化公式来自归一化 Dicke 分解：

$$
|D_N^r\rangle=\sum_k
\sqrt{\frac{\binom tk\binom{N-t}{r-k}}{\binom Nr}}
|D_t^k\rangle\otimes|D_{N-t}^{r-k}\rangle.
$$
分子计算前一块有 $k$ 个 1、后一块有 $r-k$ 个 1 的基字符串数，分母是全部重量为 $r$ 的字符串数。后一块不同重量的向量正交，取偏迹消去交叉项。因此对角输入约化后仍对角，且

$$
p_k^{(t)}=\sum_{r=0}^N p_r
\frac{\binom tk\binom{N-t}{r-k}}{\binom Nr},\qquad 0\leq k\leq t.
$$
越界二项式系数取零。代入 $N=8,t=7$，得 $p_k^{(7)}=(8-k)p_k/8+(k+1)p_{k+1}/8$。输入与输出的结果分别为

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
均匀态的分子分别是 21 和 64680。绝对偏差和分别为 $38/168=19/84$ 与 $117990/517440=3933/17248$，补全 [@exact-decrease] 使用的计算。
::: {.proposition #sibling-orders title="同一见证的全部阶数" mathesis="collected:denis-lacaille-martin-serrano-ensastiga-2026-anticoherence-trace-distance:4:s3" status="written-proof" proof="pf-sibling-orders" doi="10.5281/zenodo.23884885" source="Proposition 1" request="https://github.com/the-omega-institute/trureturing-requests/issues/252"}
对上述 $\rho,\Phi$，保真度候选量

$$
A_t^F(\sigma)=\frac{(\operatorname{Tr}\sqrt{\sigma_t})^2-1}{t}
$$

在每个整数 $t=1,\ldots,8$ 都严格上升。迹距离候选量在 $t=1,\ldots,6,8$ 严格上升，在 $t=7$ 严格下降。
:::

::: {.proof #pf-sibling-orders}
将上面的二项式约化公式用于输入与输出。下表中变化量均为输出减输入；最后一列给出 $10^6\Delta A_t^F$ 的整数下界，全部为正。

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

迹距离一列只用有理数运算。对保真度，令 $s=10^{15}$，对每个约化概率 $p$ 定义 $n(p)=\lfloor\sqrt{\lfloor s^2p\rfloor}\rfloor$。因为 $n(p)^2\leq s^2p<(n(p)+1)^2$，所以

$$
\frac{n(p)}s\leq\sqrt p<\frac{n(p)+1}s.
$$

逐项相加得到非负界 $L_\sigma\leq\operatorname{Tr}\sqrt{\sigma_t}<U_\sigma$。平方保持次序，故

$$
\Delta A_t^F\geq
\frac{L_{\Phi(\rho)}^2-U_\rho^2}{t}.
$$

表中整数是这些有理下界乘以 $10^6$ 后向下取整，而不是真实变化量的四舍五入近似。原稿 Proposition 1、Table 1 及精确 `siblings.json` 证书给出了有限求值。上述步骤指定每个包围区间与符号，不需要浮点假设。
:::

## 边界情形与范围 {#boundaries}

若 $\Phi(\rho)=\sum_iw_iU_i\rho U_i^\dagger$ 是旋转的概率混合，$w_i\geq0$，$\sum_iw_i=1$，偏迹将集体旋转变成保留空间上的旋转 $V_i$，因此

$$
\begin{aligned}
&[\Phi(\rho)]_t-\frac{I}{t+1}\\
&\qquad=\sum_iw_i V_i\left(\rho_t-\frac{I}{t+1}\right)V_i^\dagger.
\end{aligned}
$$

迹范数的凸性及酉不变性给出 $A_t(\Phi(\rho))\geq A_t(\rho)$。本例出现相反方向，故其信道不属于这个子类。

完整阶数 $t=N$ 时，协变性使 $\Phi(I/(N+1))$ 旋转不变。不可约性使其为标量矩阵，保迹性再确定为 $I/(N+1)$。对厄米矩阵 $X=X_+-X_-$，其中 $X_\pm\geq0$，正性与保迹性给出

$$
\|\Phi(X)\|_1\leq\operatorname{Tr}\Phi(X_+)+\operatorname{Tr}\Phi(X_-)
=\|X\|_1.
$$

取 $X=\rho-I/(N+1)$ 即得完整阶数的单调性。这两段论证来自原稿第 4 节，都不保证任意约化阶数的单调性。本反例满足 $t=7>N/2=4$，且输入为混合态。受限的混合态问题、纯输入问题以及最小自旋与阶数，都没有被本例解决。
