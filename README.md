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

*Last Updated: August 17, 2026*

## 📚 Latest Research Digest

### [Algorithmic Gender Prediction Is Illegitimate, But Gender Imputation Can Yield Valid Measurements](https://arxiv.org/pdf/2608.13444v1)
**Authors:** Evan Dong, Angelina Wang | **Published:** August 13, 2026

> Machine learning ethics researchers and critical HCI scholars have argued that algorithmically predicting gender is wrong. At the same time, other researchers rely on predicted gender labels to study gender disparities and develop algorithmic fairness techniques. How do we reconcile these two seemingly contradictory intuitions? We differentiate two ways gender prediction may be wrong: being illegitimate, thereby contributing to harm; and being invalid, thereby producing unusable measurements. Our analysis translates arguments against gender prediction into these terms of legitimacy and validity and shows how gender imputation applied for fairness purposes can be illegitimate yet still yield valid disparity measurements. We clarify this bind by drawing upon transfeminist literature to distinguish sexism that targets women and femininity from sexism that targets transgender and nonbinary people. While gender imputation can produce valid measurements for the former, it is illegitimate and harmful for the latter. We argue that practitioners should deploy gender imputation only when it would achieve anti-discrimination benefits that cannot be achieved through other reasonable means, while harms are minimized to the extent possible. We examine this tension in three case studies: auditing gender bias in generative image models, measuring gender disparities in film, and imputing gender from personal names. By disentangling legitimacy from validity, and differentiating these two forms of sexism, we show how debates over gender prediction have conflated distinct concerns, obscuring both the settings in which gender imputation can support fairness efforts and the harms towards transgender and nonbinary people that it fundamentally cannot capture. We conclude by recommending the development of more inclusive methods that address all kinds of sexism.

---

### [Rules or Character? Scaling Laws for AI Safety Design](https://arxiv.org/pdf/2608.13345v1)
**Authors:** Satoshi Takahashi, Nobuji Kouno, Masaaki Komatsu, Ryuji Hamamoto | **Published:** August 13, 2026

> Artificial Intelligence (AI) safety systems combine character shaping (e.g., Reinforcement Learning from Human Feedback [RLHF], Constitutional AI), which modifies behavioral distributions at training time, with rule enforcement (e.g., output filters, safety classifiers), which blocks harmful outputs at inference time, yet little formal analysis exists on how their optimal balance should change as deployment scales increase. We introduce a stylized comparative-statics model that parameterizes safety design as a resource allocation alpha in [0,1] between these two approaches, incorporating scale-dependent filter degradation, common-mode failures, and character fragility -- the risk that shaped behavior degrades or collapses under novel conditions. Under a multiplicative Pareto damage model, we derive closed-form expected harm and supplement it with tail-risk (CVaR) analysis via Monte Carlo simulation. Across three scenarios (optimistic, moderate, pessimistic), the optimal alpha* is interior or at the rules-only boundary and shifts weakly toward character shaping as deployment scale T grows, from negligible (Delta alpha* = +0.01) to pronounced (Delta alpha* = +0.21) depending on scenario. The dominant parameter is the baseline character fragility rate p^(0)_frag, which shifts alpha* by 0.50 across its range -- far exceeding the effect of tail severity, filter quality, or common-mode failure probability. CVaR and expected-harm optima converge at large T. These results suggest that safety architecture decisions depend less on deployment scale per se than on the reliability of character shaping under distributional shift.

---

### [Stochastic Spatial Metapopulation Modelling of HPAI Control and Poultry Restocking on Jolly Island](https://arxiv.org/pdf/2608.12956v1)
**Authors:** Hammed O. Fatoyinbo, Indranil Ghosh, Parul Tiwari, Peter O. Olanipekun, Afeez Abidemi, Ryan H. L. Ip | **Published:** August 13, 2026

> Highly pathogenic avian influenza (HPAI) outbreaks require rapid control during active transmission and evidence-based decisions on the safe restocking of depopulated farms. We developed a stochastic spatial SEIR-based metapopulation model for a synthetic HPAI outbreak on the fictional Jolly Island. Farms were classified as `Broiler-2', `organic duck', or `Other' production systems. The model incorporated local, environmental, movement-mediated, and distance-dependent transmission, together with reactive and preventive culling, production-specific confinement, and capacity-based restocking. The simulated epidemic was geographically concentrated and differed substantially among production classes. Preventive culling reduced mean cumulative burden from 16,362.7 to 13,631.9 infectious-farm-days, with an overall reduction of 16.7\%. Earlier confinement substantially reduced epidemic magnitude, while stronger environmental transmission increased the epidemic peak. Restocking risk declined as the epidemic approached resolution. Under the model assumptions, 24 May 2026 was the first candidate date satisfying the predefined rebound-probability threshold of 0.20. For restocking on 15 March 2026, none of the tested restocking fractions met this criterion. Capacity-based restocking reduced cumulative burden by 8.45\% and rebound probability from 0.780 to 0.533, compared with restocking relative to the baseline population. These findings demonstrate the value of integrating epidemic control and post-outbreak recovery within a single modelling framework. Timely confinement, targeted preventive culling, and phased capacity-based restocking may reduce both epidemic burden and resurgence risk, although operational decisions should also incorporate surveillance, biosecurity, economic considerations, and regulatory requirements.

---

### [CRAFT: LLM-Based Iterative Refinement for Temporal Reasoning over Clinical Narratives](https://arxiv.org/pdf/2608.12779v1)
**Authors:** Chengyang He, Tahreem Arif, Marko Zivkovic, Lijing Wang, Yue Ning, Ping Wang | **Published:** August 13, 2026

> Understanding the temporal progression of symptoms in clinical narratives is critical for disease monitoring, safety surveillance, and causality assessment. Clinical narratives, however, rarely provide explicit temporal anchors. Current approaches to temporal information reasoning focus predominantly on pairwise relation classification across multi-visit and timestamp-rich records, leaving the reconstruction of structured symptom trajectories from individual anchor-sparse reports largely unaddressed. We propose CRAFT, an LLM framework that pairs a generator with a constraint-based verifier to iteratively produce and refine stage-wise symptom timelines through targeted feedback. We conduct evaluation on MedTempo, a new benchmark of 5,347 vaccine adverse-event narratives spanning three COVID-19 vaccine types, with expert-validated temporal stage annotations for 3,166 reports. Experiments across four LLM backbones demonstrate that CRAFT consistently improves temporal ordering accuracy, with ablation analysis isolating the contribution of generator and verifier components across model capability levels.

---

### [From Fair Representation to Just Recognition in Generative AI](https://arxiv.org/pdf/2608.12669v1)
**Authors:** Severin Engelmann, Daniel Susser | **Published:** August 13, 2026

> The fair AI/ML literature has long distinguished distributive fairness, concerning how automated systems allocate resources and opportunities, from representational fairness, concerning how they shape the ways individuals and social groups are perceived, understood, and accorded social status. Generative AI is rebalancing these normative dimensions. Unlike predictive systems, large language models (LLMs) and related technologies are fundamentally expressive: their primary function is to convey meaning rather than automate domain-specific decisions. Representational harm has also become central to value alignment, especially in research on what and whose values and perspectives AI systems should represent. Existing approaches to harms in the representation of social groups often appeal to descriptive accuracy, but this strategy has important limitations. For many social groups, no stable or bounded referent exists against which representational accuracy can be judged. It is also unclear who has the authority to decide what counts as misrepresentation, while even accurate representations can reproduce harmful social patterns. The underlying problem, we argue, is therefore not simply misrepresentation but misrecognition. Drawing on political theory, especially Nancy Fraser's account of participatory parity, we show how moving from representational fairness to recognitional justice provides better conceptual and normative tools for governing central fairness challenges in generative AI.

---

### [Co-constructing sociotechnical AI governance: participatory system mapping using algorithm registers](https://arxiv.org/pdf/2608.12166v1)
**Authors:** Íñigo de Troya, Maurus Enbergs, Neelke Doorn, Roel Dobbe | **Published:** August 12, 2026

> Algorithm registers have been championed as a means of providing transparency on the use of algorithms in public services. Yet potential publics differ in their expectations of what should be made transparent and how, as well as in their interest in and ability to parse the information currently published in the registers. Moreover, it remains unclear how these instruments can represent the sociotechnical systems in which these algorithms are embedded, and how system-level transparency can facilitate accountability. In this paper, we ask, what do algorithm registers reveal (and occlude) about the sociotechnical systems governing algorithmic systems, and how can diverse stakeholder perspectives inform a more pluralistic system-theoretic safety analysis? To do this, we probe the municipal algorithm register of a Dutch city through a case study of a decision-support tool for caseworkers' assessment of citizens' welfare benefits eligibility based on legal automation through a business rule engine. Through interviews, surveys, and participatory system mapping workshops (with municipal staff, civil society organisations, and ombudsmen, N=8), we seek to understand to what extent the register allows stakeholders to map the algorithmic system in question. These maps inform a System-Theoretic Process Analysis (STPA) that situates the register within a wider sociotechnical governance structure. Participants' contributions allow us to identify potential safety hazards which would not have been possible to see using the algorithm register alone, including benefits eligibility denial, system performance deterioration, and inability to contest wrongful decisions. By engaging both direct and indirect stakeholders, we reflect on the normative dimensions of algorithm governance efforts and how politics shape the practice of system safety analysis.

---

### [Understanding Content Moderation in Large Language Models through Restricted Books: From Refusal to Warning](https://arxiv.org/pdf/2608.11806v1)
**Authors:** Xucheng Yu, Emily Knox, Haohan Wang | **Published:** August 12, 2026

> As large language models enter everyday information pipelines, understanding how they handle sensitive topics matters as much as understanding whether they handle them at all. We study this question through a large-scale, systematic experiment using restricted versus unrestricted books as a controlled testbed: 40,800 query-response pairs, 400 books, 17 prompt designs, and six frontier models spanning six AI providers (Claude Sonnet 4.5, GPT-4o, Gemini 2.5 Flash, DeepSeek-V3, Qwen-Plus, and Grok-4.1-Fast). Our restricted set is drawn from the American Library Association's Most Challenged Books records (2000-2023); we use restricted rather than banned throughout because the ALA documents formal challenges-requests to remove or restrict access-which do not always result in outright bans. Our central finding is a zero-refusal phenomenon: modern LLMs decline to discuss restricted books in only 0.07% of cases, effectively invalidating the premise of jailbreaking research for this content class. Differentiation occurs instead through warning language (+8-15 percentage points, p < 0.001) and hesitation markers (+2-5 pp), with sexual content mention rate as the strongest individual signal (+33-52 pp). We further identify systematic differences between providers and show that prompt framing alone shifts the warning-rate gap by up to 19 pp. These results indicate that LLM content policy has shifted from binary refusal toward calibrated, context-sensitive disclosure-a finding that holds consistently across Western and Chinese AI providers.

---

### [Silent Updates: Measuring and Closing the Post-Deployment Disclosure Gap](https://arxiv.org/pdf/2608.11803v1)
**Authors:** Sophia Abraham, Ben Bucknall | **Published:** August 12, 2026

> Deployed foundation models are often not static systems, with providers able to modify system behavior through fine-tuning, classifier updates, system prompt revisions, retrieval changes, and routing changes. These updates can be made silently -- that is, without public disclosure, a version increment, or re-evaluation. Such silent updates challenge a core assumption behind current AI governance frameworks that an externally verifiable chain of custody links the model referred to in evaluation results or a system card to the model served to users. In this paper, we examine post-deployment disclosure practices across first-party API providers and inference hosts to establish the extent to which a chain of custody exists in practice. We find that providers commonly publish substantial safety documentation, including quantitative evaluations and version-specific reports, but no provider in our sample published information allowing an external party to verify that the artifact being served is the same one referred to in this documentation. We introduce the Silent Updates Scorecard, a public instrument for measuring post-deployment disclosure practices across providers and hosts, and preliminary results for a sample of nine first-party API providers and seven third-party inference hosts. We also propose a Three-Part Behavioral Trigger System for determining when post-deployment modifications to a system motivate disclosure or re-evaluation obligations.

---

### [Achieving Near-Zero-Overhead Multi-Model Hierarchical Classification in Real-Time Detection Pipelines](https://arxiv.org/pdf/2608.11770v1)
**Authors:** Vaishnav Raju | **Published:** August 12, 2026

> Edge-deployed vision systems in target recognition, surveillance, autonomous vehicles, and drone domains require hierarchical inference pipelines where a detection model identifies objects of interest and downstream classifiers provide fine-grained attribute analysis. Running all models on the GPU creates a serial bottleneck that limits real-time throughput as pipeline stages grow. Modern edge SoCs pair GPUs with dedicated neural accelerators (NPUs, DLAs) capable of concurrent execution, yet deploying custom models on these accelerators remains impractical due to strict operator constraints, quantization incompatibilities, and an undocumented end-to-end pipeline. We target NVIDIA Jetson DLA cores as the representative platform. We present a five-step methodology for zero GPU fallback DLA INT8 deployment of classification backbones, comprising architecture adaptation, manual dynamic range workaround to rescue TensorRT's implicit quantization (recovering 94.0% accuracy from implicit quantization's 75%) for rapid pipeline validation before explicit quantization, quantization-aware training, ONNX graph surgery for DLA compilation, and a concurrent GPU-detection/DLA-classification inference pipeline. We document nine engineering constraints with root-cause analysis and generalizable solutions. Validation on a dual-head person attribute classifier running on DLA alongside a GPU object detector on a Jetson Orin NX demonstrates near-zero pipeline overhead (12.5 vs. 13.3~FPS detector-only at 1080p), with dual-DLA scaling at no additional cost. The methodology is backbone-agnostic and generalizes to any detection-classification edge pipeline.

---

### [Governing Agentic AI in FinTech](https://arxiv.org/pdf/2608.11344v2)
**Authors:** Henry Han | **Published:** August 11, 2026

> Financial institutions are delegating consequential decisions to agentic AI systems that decompose goals, coordinate models and tools, and act with little oversight. Yet agentic AI governance in FinTech is under-investigated. We argue the binding governance constraint is not capability but verifiability. We define the Verifiability Gap as the shortfall between the verification delegated authority demands and the explainability and reproducibility retained after a decision. It is indexed to a verifier, evidentiary standard, and audit lag. We develop a multilevel governance theory for agentic AI and test its mechanisms in three studies over nine model versions, from a three-billion-parameter local model to a commercial frontier system. Study 1 shows that provider releases alter historical financial actions, and that the controls replay needs belong to the provider: the frontier model rejects temperature, top_p and top_k outright and exposes no random seed. Under the tightest controls each endpoint allows, a local model reproduced 320 of 320 executions, hosted models 319 of 320 and 959 of 960. Study 2 shows that orchestration is a latent policy layer. Architecture changes final actions, and no execution record repeated in any configuration at any scale. The frontier model reproduces its own actions more often than the local ones, its record no better, and loses a comparable share of its differentiation. Capability buys a higher starting point, not auditability. Study 3 shows two deterministic credit-model versions each reproduce their current action perfectly, yet the current cannot recover a historical one. We conceptualize reproducibility as a governance profile, not a scalar, yielding evidence-contingent delegation: authority is defensible only while retained evidence substantiates its exercise. Beyond finance, the framework extends to other high-stakes domains requiring auditability.

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
