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

*Last Updated: June 18, 2026*

## 📚 Latest Research Digest

### [Detecting Hidden ML Training With Zero-Overhead Telemetry](https://arxiv.org/pdf/2606.19262v1)
**Authors:** Robi Rahman, Sabiha Tajdari | **Published:** June 17, 2026

> Hardware-enabled monitoring of GPU workloads underpins many proposals for AI compute governance, but if developers can defeat monitoring mechanisms, such schemes are unworkable. We evaluate the adversarial robustness of GPU workload classification using only zero-overhead, privacy-preserving NVML telemetry: content-agnostic signals that observe physical effects of computation without accessing model weights, training data, or hyperparameters. Across 5 rounds of monitor-evader iteration, we evaluate 20 evasion strategy families on 9 GPU models spanning 4 architecture generations. We develop a classifier that achieves 98.2% binary accuracy at identifying training workloads across the whole corpus, and 43-87% accuracy against the most challenging unexpected workloads even when they are adversarially disguised.

---

### [DREAM: Extending Vision-Language Models with Dual-Objective Encoding for Cross-Modal Retrieval](https://arxiv.org/pdf/2606.19062v1)
**Authors:** Kaleem Ullah, Altaf Hussain, Muhammad Munsif, Sung Wook Baik | **Published:** June 17, 2026

> In today's media-driven world, the exponential growth of video content across domains such as surveillance, education, and entertainment has made retrieving semantically relevant videos via natural language queries increasingly critical. Early video retrieval systems relied on handcrafted features or shallow cross-modal mappings, limiting their ability to capture complex semantics and temporal dynamics. While large-scale vision-language models have improved cross-modal alignment, challenges remain in modeling fine-grained temporal dependencies and nuanced linguistic structures. In this paper, we introduce DREAM: Dual-path Representation Enhancement and Alignment Model, a novel multimodal framework that addresses these limitations through enhanced visual and textual encoding. DREAM incorporates a hybrid language modeling strategy that combines masked and permuted language modeling objectives to capture both local and global linguistic semantics. On the visual side, we design a hierarchical vision encoder with cascaded group attention, which integrates spatial and temporal information through multi-stage token interaction and coarse-to-fine attention refinement. We validate DREAM through comprehensive evaluations on the widely-used MSRVTT, MSVD and LSMDC benchmark datasets, where it achieves new state-of-the-art R1 scores of 49.4%, 49.7% and 27.3%, respectively. Qualitative analyses further show the model's ability to maintain coherent attention across frames and align complex queries with dynamic video content. These findings underscore the effectiveness of hierarchical attention and dual-objective textual modeling in enabling robust, context-aware video retrieval, and pave the way for future research in advancing cross-modal representation learning.

---

### [Engagement Intensity as a Learner-Modeling Signal for Adaptive AI Ethics Instruction](https://arxiv.org/pdf/2606.18548v1)
**Authors:** Yongkyung Oh, Lynn Talton, Alex Bui | **Published:** June 16, 2026

> Adaptive AI ethics instruction in graduate research training benefits from intake measures that reflect differences in prior LLM experience. Prior coursework or workshop attendance is an obvious candidate, but it is not clear whether it is associated with pre-instruction ratings on key AI perception items. We compare three candidate intake features, self-reported usage frequency, self-rated LLM familiarity, and prior AI education, across five baseline perception outcomes in 93 bioscience graduate and postdoctoral trainees enrolled in a required research ethics course. Usage frequency shows Holm-corrected associations with all five outcomes, self-rated familiarity with three, and prior AI education with none. A threshold-like pattern at the lower end of the scale is most visible for training interest and accuracy trust rather than appearing as a uniform gradient across all five outcomes. In a short intake survey, reported LLM use is more consistently associated with these perceptions than prior coursework or workshops, with self-rated familiarity serving as a secondary indicator. These results suggest that simple pre-instruction behavioral signals can inform lightweight intake profiling for adaptive AI ethics education.

---

### [Children Are Not the Enemy: Child-Fit Security as an Alternative to Bans and Surveillance](https://arxiv.org/pdf/2606.17957v1)
**Authors:** Kopo M. Ramokapane, Rui Huan, Zaina Dkaidek, Awais Rashid | **Published:** June 16, 2026

> Digital technologies are now central to children's learning, play, communication, identity formation, and social participation. Yet dominant approaches to children's online safety often rely on containment mechanisms, including bans, age gates, parental controls, monitoring, and screen-time restrictions. These approaches can be useful in specific contexts, but they often frame child protection primarily as a problem of restricting access to systems designed for adults. In this paper, we argue that this framing is inadequate for children's digital lives and insufficient as a security paradigm. We propose Child-fit security, a design paradigm in which technologies likely to be used by children treat a child as legitimate users, not attackers to be excluded, vulnerabilities to be patched, or risks to be managed. In this paradigm, children's wellbeing, development, privacy, safety, agency, and rights become core security requirements. This shifts the focus of protection from apps, accounts, and data to the child-system relationship, which means protecting both the child and their participation. We conceptualise child-fit security, contrast it with containment-oriented approaches, define its core principles, and discuss its implications for security design. We conclude by presenting a research agenda for making child-fit security operational.

---

### [OmniTraffic: A Controllable Generation Pipeline and Benchmark for Spatio-Temporal Traffic Reasoning](https://arxiv.org/pdf/2606.15749v1)
**Authors:** Maonan Wang, Zhengyan Huang, Kemou Jiang, Yuhang Fu, Jiayue Zhu, Yuxin Cai, Xingchen Zou, Qiaosheng Zhang, Yi Yu, Ding Wang, Xi Chen, Ben M. Chen, Yuxuan Liang, Zhiyong Cui, Man On Pun, Yirong Chen | **Published:** June 14, 2026

> Traffic scene understanding requires models to reason beyond object recognition, including lane topology, multi-view geometry, temporal evolution, and signal-phase semantics. However, existing traffic-oriented multimodal benchmarks largely emphasize passive visual recognition or isolated video understanding, offering limited support for evaluating structure-aware traffic reasoning under controlled conditions. We introduce OmniTraffic, a controllable generation pipeline and benchmark for spatio-temporal traffic reasoning. Built around 12 real-world intersections reconstructed into editable 3D traffic environments and complemented by surveillance footage from two countries, OmniTraffic supports both controlled and natural-condition evaluation. It defines a three-level task hierarchy spanning scene perception, multi-view and temporal reasoning, and decision support. Using structured traffic metadata, OmniTraffic generates synchronized multi-view VQA samples covering vehicle states, lane functions, view--BEV correspondence, temporal dynamics, and signal-phase analysis, resulting in 8M VQA samples and a 3K human-verified test set. Evaluation of eleven frontier MLLMs reveals a large human--model gap, with the most pronounced failures in topology-grounded and spatio-temporal reasoning tasks. Fine-tuning a lightweight MLLM on simulated OmniTraffic data further improves performance on real-world traffic scenes, demonstrating the value of simulation-generated supervision for traffic-specific multimodal reasoning. Beyond a fixed dataset, OmniTraffic provides an extensible pipeline with configurable intersections, camera views, traffic demands, signal phases, visual conditions, and rare events.

---

### [EnvShip-Bench: An Environment-Enhanced Benchmark for Short-Term Vessel Trajectory Prediction](https://arxiv.org/pdf/2606.15240v1)
**Authors:** Kun Ma, Qilong Han, Chengjing Song, Jingzheng Yao, Hao Wang, Changmao Wu | **Published:** June 13, 2026

> Vessel trajectory prediction is important for intelligent shipping, maritime surveillance, and navigation safety. However, existing public maritime AIS resources are often limited by inconsistent forecasting protocols, uneven data quality, and the lack of benchmark-ready contextual annotations, which hinder fair comparison and context-aware modeling. To address this gap, we present EnvShip-Bench, a unified benchmark for short-term vessel trajectory prediction built from large-scale raw AIS data from the Danish Maritime Authority (DMA) and NOAA through a common processing pipeline. EnvShip-Bench adopts a standardized forecasting protocol with 10 minutes of observation, 10 minutes of prediction, and 20-second sampling in vessel-centric local metric coordinates. Beyond the large-scale core benchmark, it provides a quality-first compact subset for efficient and reproducible experimentation, together with synchronized environmental and nearby-vessel context extensions. As a result, EnvShip-Bench supports trajectory-only, environment-aware, and interaction-aware forecasting under a unified evaluation framework. Extensive benchmark statistics and analysis demonstrate that EnvShip-Bench offers a standardized, extensible, and context-aware foundation for maritime trajectory forecasting research.

---

### [KATANA: A Fast, Low-Power Mapping of Kalman Filters onto Edge NPUs for Real-Time Tracking](https://arxiv.org/pdf/2606.14992v1)
**Authors:** Bodhisatwa Kundu, Anish Rooj, Sumit Saha, Abhradeep Sarkar, Arghadip Das, Arnab Raha, Mrinal K. Naskar | **Published:** June 12, 2026

> State estimation is the closed-loop core of every real-time tracking system, from radar surveillance and counter-UAV defense to autonomous driving and robotics. These deployments run on edge platforms, where defense systems mount on vehicles and drones, and civilian pipelines live on cars and handheld devices. Here, every additional watt of compute erodes mission duration or operational range. Two hard constraints follow: each new measurement must be fused before the next control cycle, and the total compute must fit within a strict battery and thermal power envelope. The Linear and Extended Kalman Filters (LKF, EKF) are dominant estimators on these systems, but today they execute almost exclusively on CPUs, which serialize multi-object tracking (MOT) updates, or on custom FPGA/ASIC accelerators that lengthen design cycles. Contemporary AI-PC SoCs, like the Intel Core Ultra Series 1 and 2, integrate a low-power, data-parallel Neural Processing Unit (NPU). We therefore ask whether the Kalman filter can be mapped onto this existing matrix engine to meet real-time and low-power budgets simultaneously, avoiding a dedicated accelerator and keeping the CPU and GPU free for primary workloads. We present KATANA, an NPU-aware optimization framework delivering the first end-to-end mapping of the LKF and EKF onto a commercial NPU, alongside a cross-platform characterization on shipping AI-PC silicon. KATANA applies three algebraic graph rewrites: subtract-to-add reformulation via a precomputed negative-projection matrix H_neg, static-shape tensor fusion, and block-diagonal batched parallelization, ensuring 100% of operations execute on the DPU matrix engine. On the Series 2, the optimized batched EKF reaches 223.35 FPS at 13.43 W active power, and the LKF reaches 408.73 FPS at 14.05 W, delivering up to a 97.9% reduction in dynamic energy versus the CPU implementation.

---

### ["Stuck in a Spiral": Shame and Guilt as Social Regulators of AI Use in Computing Education](https://arxiv.org/pdf/2606.14920v1)
**Authors:** Kate Hamilton, Irene Hou, Dev Patel, Sheena Nnam, Hena Patel, Stephen MacNeil | **Published:** June 12, 2026

> While prior work has examined patterns of adoption and social norms around AI use, less is known about how emotional factors, such as shame and guilt, shape students use of AI tools. We present an interview study with 19 computing students through a functionalist perspective of shame and guilt, which interprets emotions as social signals that regulate behavior. Our findings show that these emotions regulate when and how students make their use visible, as they engage in hiding behaviors and selective disclosure. Students described shaming themselves, their peers, and even faculty for using AI. Shame and guilt often coexist with continued AI use, creating cycles of reduced agency and moral tension rather than promoting behavior change. Students described feeling tensions between their AI use and their identities as competent, hardworking, or ethical computing students. Students also used language and metaphors of addiction to describe their experiences. These results highlight the need to consider the socio-emotional aspects of AI use, which may be influenced by how AI policies are implemented and enforced. We discuss classroom practices that can foster healthy, open discussion and support responsible AI use.

---

### [Robust Network Flow Interdiction Problems with Applications to Counter-Narcotics](https://arxiv.org/pdf/2606.14611v1)
**Authors:** Diksha Gupta, Madhav Marathe, Anil Vullikanti | **Published:** June 12, 2026

> Interdiction problems arise in a number of application areas, including global security, supply chains, and critical infrastructure protection - the goal is inhibit the movement of goods, people or information. An area of particular interest is counter-narcotics, where nodes or edges in a network are placed under surveillance or blocked to minimize the flow of illicit drugs from source to the destination. A fundamental challenge in this narco-traffic interdiction is data scarcity: available datasets are limited by the very nature of the problem and provide only partial and uncertain views of trafficking networks. Thus, developing robust interdiction methods that take this inherent lack of information is critical.   In this paper we initiate the study of network flow interdiction problems under network uncertainty. First, using a limited real-world dataset, we generate an ensemble of plausible network realizations representing alternative trafficking scenarios. The method combines simulations with mathematical programming techniques to generate network ensembles that are consistent with the observed data. Second, we formulate the robust network flow interdiction problem and develop an integer linear program to solve the problem. We evaluate the optimal interdiction strategy and obtain the residual flows over the scenarios. Our analysis reveals that even modest budgets can yield significant flow reductions. However, optimal solutions vary substantially across scenarios, motivating the need for robust solutions. We show that the robust strategy achieves near-optimal performance across all near-real world realizations while remaining stable under structural uncertainty. This simulation-driven approach provides a principled basis for policy analysis and supports maximizing the return on interdiction investments in uncertain, data-limited environments.

---

### [Regulating the Machine Contributor: Governance and Policy Alignment in Open Source](https://arxiv.org/pdf/2606.14594v1)
**Authors:** Jassem Manita, Aziz Amari | **Published:** June 12, 2026

> AI-assisted software development has moved from line-level autocomplete to agents that can plan changes, edit files, and submit pull requests with limited human supervision. Open-source software, however, evolves through a process designed for humans: contributor agreements, codes of conduct, and review norms all assume a legally accountable person who can attest to provenance and answer reviewer questions. Autonomous and semi-autonomous AI contributors strain those assumptions, and the 2025-2026 record of agent-driven incidents, AI-generated nuisance volume, and platform-level shutdowns shows that the gap is operationally consequential. Several open-source organisations have responded with contribution policies, but the result is fragmented, and its alignment with emerging AI governance frameworks (EU AI Act, NIST AI RMF with the UC Berkeley Agentic AI Profile, ISO/IEC 42001 and 23894) is unmapped at the contribution level. We compare policies across six organisations (SymPy, LLVM, matplotlib, OpenInfra, the Apache Software Foundation, and the Linux Foundation) using Most-Similar Systems Design with indicator-based coding and process tracing for SymPy and LLVM. From this we derive a six-dimensional taxonomy (disclosure, responsibility, human oversight, licensing, enforcement, maintainer workload), an ordinal Policy Maturity Score, and a mapping of documented agent incidents onto the dimensions each policy fails to govern. Aligning the dimensions with the regulatory frameworks above identifies overlapping gaps neither side currently closes, and we close by sketching the shape of a harmonised tiered framework and the empirical evaluation needed to calibrate it.

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
