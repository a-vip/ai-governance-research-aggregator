# 🤖 AI Governance & Sovereign Algorithms Research Aggregator

<div align="center">
  <p><strong>A continuously updated repository of the latest academic research.</strong></p>
  <p><em>Curated and maintained by <a href="https://aviperera.com">Avi Perera</a></em></p>
  <p>
    <a href="https://aviperera.com">Website</a> •
    <a href="https://twitter.com/aviperera_">Twitter</a> •
    <a href="https://www.researchgate.net/profile/Avi-Perera">ResearchGate</a> •
    <a href="https://orcid.org/0009-0005-1903-6868">ORCID</a>
  </p>
  <hr>
</div>

Welcome to the **AI Governance Research Aggregator**. This resource autonomously queries academic databases every week to compile the latest papers on Artificial Intelligence Policy, Ethics, Lethal Autonomous Weapons Systems (LAWS), Surveillance, and Meaningful Human Control.

*Last Updated: July 06, 2026*

## 📚 Latest Research Digest

### [Real-Time Visual Intelligence on Low-Cost UAVs: A Modular Approach for Tracking, Scanning, and Navigation](https://arxiv.org/pdf/2607.02298v1)
**Authors:** Andrei-Marian Ungureanu, Stelian Spînu | **Published:** July 02, 2026

> Autonomous drones are rapidly transforming modern warfare and civil applications alike. This paper presents the development of an integrated intelligent drone system designed to serve as a personal assistant. Leveraging the DJI Tello drone platform, we implemented a modular architecture that integrates three core artificial intelligence functionalities: facial detection, facial recognition, and depth estimation from monocular vision. A web-based interface enables seamless drone control and real-time video monitoring, while a Python-based server processes visual data and executes inference pipelines using lightweight neural models optimized for embedded systems. Unlike existing commercial solutions, this system emphasizes accessibility, low-cost hardware, and open-source technologies. The system demonstrates robust performance in real-world conditions, including person tracking, indoor scanning, and autonomous line following using virtual sensors. This project validates the applicability of advanced AI techniques in real-time robotic systems and illustrates the feasibility of deploying them on constrained hardware, providing a foundation for future research in autonomous UAVs for military, rescue, and surveillance missions.

---

### [Beyond the Performance Illusion: Structure-Aware Stratified Partitioning and Curriculum Distributionally Robust Optimization for Spatially Correlated Domains](https://arxiv.org/pdf/2607.02055v1)
**Authors:** Prathamesh Patil, Arpit Jain, Aswanth Krishnan | **Published:** July 02, 2026

> Performance evaluation in AI systems commonly assumes that random dataset splits produce independent and identically distributed (i.i.d.) subsets. We show that this assumption often breaks down in spatiotemporally correlated domains such as aerial surveillance, precision agriculture, and medical imaging, leading to two systematic failures: data leakage, where correlated samples span training and validation splits and inflate performance estimates, and hidden stratification, where errors on minority subpopulations are obscured by aggregate metrics. To address these issues, we propose a unified evaluation and training framework for spatially correlated data. We introduce Structure-Aware Stratified Partitioning (SASP), which constructs validation splits that reduce spatiotemporal leakage while preserving meaningful class balance, and Curriculum Distributionally Robust Optimization (CDRO), a curriculum-based relaxation of distributionally robust training that stabilizes optimization under these stricter splits. Across multiple benchmarks, this combination yields consistently improved generalization, more reliable confidence calibration, and exposes failure modes that remain hidden under conventional random-split evaluation.

---

### [From Battlefield to Boardroom: Strategic Red Teaming as an Epistemic Governance Instrument in the Age of AI](https://arxiv.org/pdf/2607.01913v1)
**Authors:** Jeroen Janssen | **Published:** July 02, 2026

> Organizations increasingly make strategic decisions about AI systems whose behaviour, failure modes, and institutional effects cannot be fully known at design time. This technical report reframes strategic red teaming as a board-level governance discipline for testing the assumptions under which AI-enabled strategies are approved, funded, and supervised.   The report proposes a six-component model for strategic red teaming in AI governance: an explicit assumption register, an adversarial mandate, independence criteria, evidence grading, a board-facing decision record, and a follow-up mechanism for unresolved findings. The model is intended to make strategic uncertainty inspectable before it becomes operational exposure. It treats red teaming not as penetration testing, scenario theatre, or generic risk review, but as structured adversarial testing of the claims on which governance decisions depend.   The contribution is conceptual and design-oriented. It does not claim empirical validation, regulatory endorsement, or legal sufficiency. Instead, it provides a candidate governance artefact for organizations that need to connect AI strategy, accountability, oversight, and evidence. The report also defines limitations and a minimum validation protocol for future empirical testing in organizational settings.

---

### [Sampling for Region-Aggregated Spatial Scan Statistics](https://arxiv.org/pdf/2607.01451v1)
**Authors:** Foad Namjoo, Drew McClelland, Michael Matheny, Jeff M. Phillips | **Published:** July 01, 2026

> Anomaly detection in geospatial data is a crucial tool in geographic information science (GIS), with applications ranging from national security to public-health surveillance to the study of societal disparities. This work focuses on spatial scan statistics and addresses a key mismatch: spatial counts are typically aggregated into predefined regions (census tracts, zip codes, counties), whereas the most efficient scan algorithms operate on spatial point data. The standard remedy -- collapsing each region to its centroid, as in widely used tools such as SaTScan -- is convenient but, as we show, discards the region's spatial extent and causes a significant loss in statistical power. To resolve this, we propose a simple yet scalable fix: replace each spatial region with 20-50 points sampled uniformly from its geometry and spread the region's values evenly across them. This approach improves statistical power while maintaining computational tractability. A convergence analysis explains why so few samples per region suffice. We recommend this sampling-based conversion as the default way to apply point-based spatial scan statistics to region-aggregated data for anomaly detection.

---

### [Bilinear control of age--space structured populations](https://arxiv.org/pdf/2607.01347v1)
**Authors:** Jiguang Yu, Louis Shuo Wang | **Published:** July 01, 2026

> We study constrained bilinear optimal control for nonlocal age--space structured population equations with renewal boundary conditions and endogenous surveillance feedback. The control acts as a coefficient in a mixed transport--diffusion equation, while a scalar observable generated by the state enters both the interior dynamics and the renewal law. This produces a nonlinear closed-loop control-to-state map and a feedback-dependent adjoint system. Using a characteristic mild formulation rather than a standard Lions--Magenes argument, we establish closed-loop well-posedness and Frechet differentiability. We then derive the reduced and feedback-corrected adjoint equations. The feedback derivative is identified as a low-rank perturbation $\ell_{\bar y,\bar u}(p)(t)χ(a,x)$; in the Volterra-kernel regime, the associated transfer operator is quasinilpotent, yielding an explicit resolvent representation of the adjoint. Finally, we prove first-order optimality conditions and decompose the switching function into reduced and feedback-induced components.

---

### [LongVQUBench: Benchmarking Long-Term Video Quality Understanding of Vision-Language Models](https://arxiv.org/pdf/2607.01086v1)
**Authors:** Arpita Nema, Hanwei Zhu, Xi Zhang, Weisi Lin | **Published:** July 01, 2026

> The evaluation of long-term video quality understanding remains an open challenge for large vision-language models (LVLMs). Existing video quality benchmarks predominantly focus on short clips and isolated distortions, overlooking the temporal continuity, cumulative degradation, and reasoning complexity inherent in long-duration content. To address these limitations, we present LongVQUBench, a comprehensive benchmark for long-term video quality understanding. LongVQUBench contains over 1200 diverse videos spanning movies, documentaries, surveillance footage, egocentric recordings, and animated content, accompanied by 1500 multiple-choice and open-ended questions for validation and testing. To assess perceptual reasoning across different temporal scopes, we introduce three progressively complex evaluation levels: (i) local event quality understanding (LQU) for analyzing localized distortions; (ii) cross-event quality reasoning (CQR) for integrating multiple degraded events; and (iii) global quality understanding (GQU) for holistic perceptual evaluation over extended durations. Furthermore, a needle distortion question-answering (NDQA) paradigm is embedded across all three levels, where spatial or temporal artifacts are sparsely inserted to probe fine-grained detection and reasoning capabilities. Extensive experiments on 14 state-of-the-art LVLMs reveal significant performance degradation with increasing video length and reasoning depth, highlighting their limited capacity for long-range temporal integration and perceptual attribution. We envision LongVQUBench as a foundational step toward the systematic, hierarchical, and explainable evaluation of LVLMs' long-term video quality understanding.

---

### [AMBUSH: Collaborative Capture in Complex Environments with Neural Acceleration](https://arxiv.org/pdf/2607.01029v1)
**Authors:** Junfeng Chen, YinHang Luo, Xinyi Wang, Junrui Li, Meng Guo | **Published:** July 01, 2026

> Collaborative capture of dynamic targets is common in nature as an essential strategy for weaker species against the strong. Similar concepts have shown to be useful for numerous robotic applications, such as security and surveillance, search and rescue. However, most existing works focus on analytical and geometric solutions or end-to-end reinforcement learning methods, which are largely constrained to obstacle-free environments or scenarios with sparse, regularly distributed obstacles. This work tackles the problem from a unique perspective: the renowned strategy of``ambush'' alone would suffice for multiple slower pursuers to capture one faster evader with different levels of intelligence efficiently in complex environments. A parameterized strategy of ambush (including discrete and continuous parameters) is designed first, which takes into account the topological properties of the workspace, the truncated line-of-sight visibility, the relative speed ratio and the limited capture range. Then, a Hybrid Monte Carlo Tree Search (H-MCTS) algorithm is proposed to optimize the associated parameters through long-term planning, enabling the identification of highly promising parameters for future capture. Lastly, the neural acceleration is trained offline to learn the ranking of different choices of parameters across various environments, and to directly predict scores, replacing the rollout process in H-MCTS. The neural acceleration is adopted during online H-MCTS to accelerate the planning procedure while guaranteeing the planning quality. Its efficiency and effectiveness are validated in extensive simulations and hardware experiments, against evaders with different capabilities and intelligence levels, including two-times higher velocity and human-controlled behavior.

---

### [Two AI Metrics Diverged: Will it Make All the Difference?](https://arxiv.org/pdf/2607.00913v1)
**Authors:** Alex Fogelson, Zachary A. Brown, Hans Gundlach, Jayson Lynch, Neil Thompson | **Published:** July 01, 2026

> As exponential compute scaling continues, will the capabilities of frontier AI models outstrip what is accessible to developers on a small fixed budget? Or will capabilities converge, with "meek models inheriting the earth"? Building on Gundlach et al. (2025b), we show that the answer depends on how we value and measure AI capabilities. We discuss conventional performance measures and show that, while validation loss shows a shrinking gap, on other metrics frontier models grow their lead forever. Classifying performance metrics by their functional forms in relation to training (and inference) compute, we provide tight mathematical conditions for determining which metrics favor meek models, and show that bounded performance metrics always do. But careful interpretation of performance metrics is essential: we show that many common bounded metrics have closely-related counterpart metrics that are unbounded (and vice versa). Determining the apt metric in a domain is a prerequisite for policy, since bounded and unbounded metrics may suggest opposing policy responses. If a particular capability -- like software engineering, synthetic biology, or rhetorical persuasiveness -- is unbounded when measured in the terms we care about, frontier-level capability will likely be concentrated in the hands of a few wealthy actors. Conversely, if that capability is instead bounded, frontier-level capabilities proliferate through meek models into the hands of the many.

---

### [Partial Skeleton Visibility for Action Recognition: A Constrained Field-of-View Approach](https://arxiv.org/pdf/2607.00716v1)
**Authors:** Yingjie Dai, Tianyang Xu, Yanglin Deng, Xiao-Jun Wu, Josef Kittler | **Published:** July 01, 2026

> Skeleton-based action recognition has achieved remarkable success by exploiting joint coordinates and their topological connections, yet prevailing methods overwhelmingly assume complete and clean skeleton inputs. In real-world deployments, such as egocentric vision, crowded surveillance, wearable devices, or edge robotics, limited field-of-view (FoV) frequently causes substantial joint visibility dropout, leading to severe performance degradation that existing models are largely unprepared to handle. To bridge this critical yet underexplored gap, we introduce PartialVisGraph, a novel hypergraph framework tailored for robust skeleton action recognition under constrained FoV. We first construct highly expressive hypergraphs by introducing learnable virtual hyperedges that form a soft incidence matrix, capturing flexible high-order dependencies beyond conventional pairwise graphs. We then propose the Single-Head Sample-Adaptive Transformer, which adaptively aggregates joint features onto hyperedges while explicitly incorporating a visibility prior. This prior selectively gates information flow, preventing occluded or out-of-view joints from corrupting reliable feature propagation. We further establish rigorous evaluation protocols with realistic FoV simulation benchmarks on NTU RGB+D 60 and 120. Extensive experiments demonstrate that PartialVisGraph consistently achieves state-of-the-art accuracy under partial visibility, with gains of up to 68.8\% on subsets with severe FoV restrictions compared to recent strong baselines, while remaining superior on full-visibility settings. Our approach offers a principled and practical pathway toward deployable skeleton-based action understanding in unconstrained environments.

---

### [Real-Time Source-Free Object Detection](https://arxiv.org/pdf/2606.31834v1)
**Authors:** Sairam VCR, Varun Gopal, Poornima Jain, Vineeth N Balasubramanian, Muhammad Haris Khan | **Published:** June 30, 2026

> Real-world detectors for autonomous driving, surveillance, and robotics must handle domain-shifts under strict latency and memory constraints, yet existing source-free object detection (SFOD) methods rely on heavyweight architectures that prioritize accuracy alone. We show this trade-off is unnecessary: building on YOLOv10, an NMS-free dual-head detector, we achieve state-of-the-art adaptation accuracy while being faster and more compact. We observe that directly applying vanilla mean-teacher self-training to dual-head detectors leads to suboptimal adaptation performance due to two key factors. First, simple pseudo-label generation strategies, such as using a single head or directly combining high-confidence predictions from both heads, yield suboptimal supervision under domain-shift. We propose DHF (Dual-Head Pseudo-Label Fusion) which selectively admits one-to-one (O2O) and one-to-many (O2M) head predictions, preserving precision and recovering missed objects. Second, we observe domain-shift collapses multi-scale feature discriminability. We propose the use of our MARD (Multi-scale Adaptive Representation Diversification) loss which mitigates this by enforcing detection-aware variance and covariance constraints on multi-scale feature maps. Both modules are training-time only, leaving inference unchanged. Across domain-shift benchmarks, our method, RT-SFOD yields 1.4 to 3.5\% mAP gains, 1.3$\times$ higher throughput, with $\sim$2$\times$ fewer parameters than prior state-of-the-art SFOD methods, thus advancing the Pareto frontier of the speed-accuracy-model size trade-off. We report main results with YOLOv10, and demonstrate generalizability with additional YOLO- and DETR-based dual-head detectors. Code is available here: https://github.com/Sairam13001/RT-SFOD/

---


## 🔗 Related Resources & Authority Insights

To dive deeper into the intersection of technology, law, and international security, explore the following curated resources:

*   **[Avi Perera | Official Website](https://aviperera.com)** - Read the latest articles on Sovereign Algorithms and AI Governance.
*   **[Sovereign Dashboard](https://sovdash.com)** - An interactive analysis platform for state-level AI capabilities.
*   **[The LAWS Framework](https://github.com/a-vip/ai-governance-laws-frameworks)** - Legal analysis frameworks regarding artificial intelligence governance.

<br>

<div align="center">
  <small><em>This repository is fully autonomous and powered by GitHub Actions.</em></small><br>
  <small><em>Copyright © Avi Perera. All academic papers belong to their respective authors.</em></small>
</div>
