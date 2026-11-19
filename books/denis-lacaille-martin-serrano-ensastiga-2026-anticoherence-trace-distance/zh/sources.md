<style>pre:has(> code[class*="typst"]) { display: none; }</style>

# 来源与参与

本书解释 Haobo Ma 与 Wenlin Zhang 的公开论文第 4 版：[精确版本 DOI：10.5281/zenodo.23884885](https://doi.org/10.5281/zenodo.23884885)。概念 DOI [10.5281/zenodo.23884884](https://doi.org/10.5281/zenodo.23884884) 聚合各版本。论文及本书按 CC BY 4.0 提供。Haobo Ma 的机构为 Chrono AI（新加坡）；Wenlin Zhang 的机构为新加坡国立大学与 Chrono AI（新加坡）。

## 研究脉络

- J. Denis、T. Lacaille、J. Martin 与 E. Serrano-Ensástiga，*Total, quantum, and classical measures of anticoherence for mixed spin states*，[arXiv:2605.29436v1](https://arxiv.org/abs/2605.29436v1)，[DOI](https://doi.org/10.48550/arXiv.2605.29436)。第 II.B 节式 (7)–(8) 给出 (T4)，第 III.A.2 节式 (22) 的 $p=1$ 是迹距离候选量；第 III.A.3 节式 (26) 是保真度候选量。第 III.B.2 节命题 6 的凸屋顶结论带有总评分满足公理的前提。
- D. Baguette 与 J. Martin，*Anticoherence measures for pure spin states*，Physical Review A **96**, 032304 (2017)，[DOI](https://doi.org/10.1103/PhysRevA.96.032304)。这是纯态评分的相关背景。
- T. Aschieri、B. Ruba 与 J. P. Solovej，*SU(2)-equivariant quantum channels: semiclassical analysis*，Communications in Mathematical Physics **405**, 298 (2024)，[DOI](https://doi.org/10.1007/s00220-024-05178-1)。本文的信道归一化与协变证明直接计算，不依赖该文的分类。

## 数学证据与可参与工作

[@universal-refutation] 对应公开 Lean 定理。它否定完整混合态范围的全称命题。[形式化源码](lean:D5/S3/Quantum/Measurement/AnticoherenceTraceDistanceRefutation.result)已经包含本见证及其合法性、输出和约化距离的证明；本文重建了这个既有见证。精确归一化下降、一般自旋恒等式和全部阶数的比较分别保留书面证明及以下共用请求：

- [精确下降：复用既有见证与距离，补足归一化等式和可引用陈述](https://github.com/the-omega-institute/trureturing-requests/issues/250)，[@exact-decrease]。

- [一般自旋四极恒等式：不依赖反例的独立代数结果](https://github.com/the-omega-institute/trureturing-requests/issues/251)，[@quadrupole-normalization]。

- [全部阶数的比较：复用既有输出与约化，给出精确保真度符号](https://github.com/the-omega-institute/trureturing-requests/issues/252)，[@sibling-orders]。

参与者可在对应请求中协调范围，再从自己的 fork 向 [trureturing 的 dev 分支](https://github.com/the-omega-institute/trureturing/blob/dev/docs/CONTRIBUTING.md)提交聚焦的 PR，遵守上游现有准入与评审规则。已有的普遍否定不需要重复证明。

