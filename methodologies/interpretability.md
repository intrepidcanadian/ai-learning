# Interpretability

## Overview

**Interpretability** (also called **mechanistic interpretability**) is the field of research dedicated to understanding *how* and *why* neural networks produce their outputs. Rather than treating AI models as black boxes, interpretability research reverse-engineers the computational mechanisms inside trained networks — identifying circuits, features, and algorithms that emerge from training. For AI-assisted learning, interpretability is foundational: a model that can explain its reasoning is a better teacher, and understanding model internals helps detect when outputs should not be trusted (see [hallucination detection](../core-concepts/hallucination-detection.md)).

## Background / Theoretical Foundations

### From Black Box to Glass Box

The interpretability challenge arises because modern neural networks learn distributed representations where knowledge is spread across millions (or billions) of parameters with no explicit human-readable structure. Early work focused on **post-hoc explanations** — generating human-understandable rationales after the model has made a decision. But the field has shifted toward **mechanistic interpretability**: understanding the actual computations models perform, not just rationalizing their outputs.

### Superposition and Polysemanticity

A central discovery is that neural networks represent far more concepts than they have neurons, through **superposition** — encoding multiple features as nearly-orthogonal directions in activation space.[^1] This means individual neurons are **polysemantic** (responding to multiple unrelated concepts), making it impossible to understand model behavior by examining individual neurons in isolation.

This insight motivated the development of **sparse autoencoders (SAEs)** as a tool for decomposing model activations into interpretable, monosemantic features — essentially "untangling" the superposition.[^2]

### The Circuits Framework

Olah et al. (2020) proposed the **circuits framework**: neural networks can be understood as compositions of meaningful computational subgraphs (circuits) that implement specific algorithms.[^3] A circuit is a subgraph of the network's computational graph that maps specific input features to specific output behaviors. For example, an "induction head" circuit in transformers implements the algorithm: "if token A was followed by token B earlier, and token A appears again, predict token B."

## Technical Details / Key Systems

### Sparse Autoencoders (SAEs)

SAEs are the dominant tool in modern mechanistic interpretability. They work by:

1. Collecting activation vectors from a model layer across many inputs
2. Training an autoencoder with a sparsity penalty to reconstruct these activations
3. The learned dictionary elements (encoder directions) correspond to interpretable features

```svg
<svg viewBox="0 0 700 350" xmlns="http://www.w3.org/2000/svg" font-family="monospace" font-size="12">
  <defs>
    <marker id="arrowI" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#333"/>
    </marker>
  </defs>

  <!-- Title -->
  <text x="350" y="25" text-anchor="middle" font-size="16" font-weight="bold" fill="#1a1a2e">Sparse Autoencoder for Mechanistic Interpretability</text>

  <!-- Model activations (input) -->
  <rect x="30" y="100" width="120" height="160" rx="8" fill="#e8f4f8" stroke="#2196F3" stroke-width="2"/>
  <text x="90" y="85" text-anchor="middle" font-size="11" fill="#1565C0">Model Layer</text>
  <text x="90" y="140" text-anchor="middle" font-size="10">Polysemantic</text>
  <text x="90" y="155" text-anchor="middle" font-size="10">Activations</text>
  <text x="90" y="175" text-anchor="middle" font-size="10" fill="#666">(d = 768)</text>
  <rect x="50" y="195" width="80" height="8" rx="4" fill="#2196F3" opacity="0.6"/>
  <rect x="50" y="210" width="80" height="8" rx="4" fill="#2196F3" opacity="0.4"/>
  <rect x="50" y="225" width="80" height="8" rx="4" fill="#2196F3" opacity="0.8"/>

  <!-- Encoder arrow -->
  <line x1="155" y1="180" x2="225" y2="180" stroke="#333" stroke-width="2" marker-end="url(#arrowI)"/>
  <text x="190" y="170" text-anchor="middle" font-size="10" fill="#555">Encode</text>

  <!-- Sparse features (hidden) -->
  <rect x="230" y="60" width="140" height="240" rx="8" fill="#fff3e0" stroke="#FF9800" stroke-width="2"/>
  <text x="300" y="45" text-anchor="middle" font-size="11" fill="#E65100">Sparse Features</text>
  <text x="300" y="80" text-anchor="middle" font-size="10" fill="#666">(d_sae = 16384)</text>

  <!-- Feature bars - mostly zero, few active -->
  <rect x="250" y="95" width="5" height="8" rx="2" fill="#FF9800" opacity="0.9"/>
  <rect x="260" y="95" width="5" height="8" rx="2" fill="#ddd"/>
  <rect x="270" y="95" width="5" height="8" rx="2" fill="#ddd"/>
  <rect x="280" y="95" width="5" height="8" rx="2" fill="#FF9800" opacity="0.7"/>
  <rect x="290" y="95" width="5" height="8" rx="2" fill="#ddd"/>
  <rect x="300" y="95" width="5" height="8" rx="2" fill="#ddd"/>
  <rect x="310" y="95" width="5" height="8" rx="2" fill="#ddd"/>
  <rect x="320" y="95" width="5" height="8" rx="2" fill="#FF9800" opacity="0.5"/>
  <rect x="330" y="95" width="5" height="8" rx="2" fill="#ddd"/>
  <rect x="340" y="95" width="5" height="8" rx="2" fill="#ddd"/>

  <!-- Monosemantic labels -->
  <text x="300" y="130" text-anchor="middle" font-size="10">Monosemantic</text>
  <text x="300" y="145" text-anchor="middle" font-size="10">Features:</text>
  <rect x="250" y="160" width="100" height="20" rx="4" fill="#FFF8E1" stroke="#FFB74D"/>
  <text x="300" y="174" text-anchor="middle" font-size="9">"Python code"</text>
  <rect x="250" y="185" width="100" height="20" rx="4" fill="#FFF8E1" stroke="#FFB74D"/>
  <text x="300" y="199" text-anchor="middle" font-size="9">"Golden Gate Bridge"</text>
  <rect x="250" y="210" width="100" height="20" rx="4" fill="#FFF8E1" stroke="#FFB74D"/>
  <text x="300" y="224" text-anchor="middle" font-size="9">"Deception"</text>
  <rect x="250" y="235" width="100" height="20" rx="4" fill="#FFF8E1" stroke="#FFB74D"/>
  <text x="300" y="249" text-anchor="middle" font-size="9">"Medical advice"</text>
  <text x="300" y="278" text-anchor="middle" font-size="9" fill="#888">~95% features = 0</text>

  <!-- Decoder arrow -->
  <line x1="375" y1="180" x2="445" y2="180" stroke="#333" stroke-width="2" marker-end="url(#arrowI)"/>
  <text x="410" y="170" text-anchor="middle" font-size="10" fill="#555">Decode</text>

  <!-- Reconstructed activations -->
  <rect x="450" y="100" width="120" height="160" rx="8" fill="#e8f5e9" stroke="#4CAF50" stroke-width="2"/>
  <text x="510" y="85" text-anchor="middle" font-size="11" fill="#2E7D32">Reconstructed</text>
  <text x="510" y="140" text-anchor="middle" font-size="10">Activations</text>
  <text x="510" y="155" text-anchor="middle" font-size="10" fill="#666">(d = 768)</text>
  <rect x="470" y="195" width="80" height="8" rx="4" fill="#4CAF50" opacity="0.6"/>
  <rect x="470" y="210" width="80" height="8" rx="4" fill="#4CAF50" opacity="0.4"/>
  <rect x="470" y="225" width="80" height="8" rx="4" fill="#4CAF50" opacity="0.8"/>

  <!-- Loss label -->
  <text x="510" y="280" text-anchor="middle" font-size="10" fill="#C62828">Loss = Reconstruction</text>
  <text x="510" y="295" text-anchor="middle" font-size="10" fill="#C62828">+ λ · Sparsity</text>

  <!-- Key insight -->
  <rect x="30" y="310" width="570" height="30" rx="6" fill="#f3e5f5" stroke="#9C27B0" stroke-width="1"/>
  <text x="315" y="330" text-anchor="middle" font-size="11" fill="#6A1B9A">Key: Sparse features are interpretable → each corresponds to a human-understandable concept</text>
</svg>
```

Tang et al. (2025) provided the first unified theoretical analysis of SAEs, proving that the loss landscape is **piecewise biconvex** and characterizing when and why training produces polysemantic features and dead neurons.[^4] This theoretical grounding helps practitioners choose hyperparameters that minimize these failure modes.

### Sparse Attention Post-Training

Draye et al. (2025) introduced a method to make transformer attention sparse *after training* without sacrificing performance.[^5] By reducing attention connectivity to approximately 0.4% of edges on models up to 7B parameters, this approach makes attention patterns human-readable — enabling researchers to trace how information flows through the network for any given input.

### Open Problems

Sharkey et al. (2025) mapped out the field's key open problems in a comprehensive roadmap:[^6]

| Problem Area | Core Question | Why It Matters |
|-------------|--------------|---------------|
| Feature completeness | Do SAEs find *all* important features? | Missing features = blind spots |
| Composition | How do features interact across layers? | Understanding multi-step reasoning |
| Scalability | Can methods work on frontier models? | Interpretability must keep pace with capabilities |
| Evaluation | How do we verify interpretations are correct? | Avoiding "just-so stories" |
| Causal understanding | Do identified circuits *cause* behavior? | Correlation ≠ mechanism |

## Current State / Latest Developments

### 2025-2026 Progress

The field has accelerated dramatically:

- **Anthropic's feature mapping** (2024-2025): Identified millions of interpretable features in Claude models using SAEs, including features for deception, bias, and safety-relevant behaviors[^2]
- **Circuit discovery at scale**: Automated methods now identify circuits in billion-parameter models, moving beyond small toy models
- **Steering via features**: Discovered features can be artificially activated or suppressed to control model behavior — e.g., amplifying a "code quality" feature improves code generation
- **Transcoders**: An alternative to SAEs that maps between MLP inputs and outputs, potentially capturing a broader class of features[^4]

### Attribution Patching at Scale (2026)

Conmy et al. (2026) introduced **attribution patching**, a scalable technique for identifying which model components are responsible for specific behaviors.[^7] Unlike activation patching (which requires exponentially many forward passes), attribution patching uses gradient-based approximations to identify causal circuits in a single backward pass. Applied to GPT-4-class models, the method identified circuits responsible for:
- Factual recall (knowledge retrieval heads in layers 15-22)
- Instruction following (attention patterns in early layers)
- Code generation (specialized MLP neurons in mid-layers)

**Learning application:** Attribution patching enables AI tutors to explain *which parts of the model's knowledge* are being used for a given answer, making model reasoning transparent to learners.

### 2026 Advances in Mechanistic Interpretability

- **MI for LLM Alignment** (January 2026): A comprehensive survey of mechanistic interpretability techniques specifically for alignment — covering circuit discovery, feature visualization, activation steering, and causal intervention. Identifies scaling sparse autoencoder approaches to the largest models as a near-term priority, with direct implications for making [AI safety in research](../frontier-topics/ai-safety-in-research.md) more tractable.[^10]

- **WeightLens & CircuitLens** (ICLR 2026): Two complementary methods that go beyond activation-based analysis. WeightLens interprets features directly from learned weights (no forward pass required); CircuitLens captures how feature activations arise from component interactions, revealing circuit-level dynamics invisible to activation-only methods.[^11] This advances the [circuits framework](#the-circuits-framework) from descriptive to mechanistic.

- **Unified Attribution Framework** (January 2026): A position paper arguing that feature attribution (XAI), data attribution (data-centric AI), and component attribution (mechanistic interpretability) share fundamental mathematical similarities. A unified view enables cross-pollination: techniques developed for explaining individual predictions can inform circuit discovery, and vice versa.[^12]

- **Internal States for Hallucination Detection** (January 2026): Addresses the "Detection Dilemma" — probing internal states excels at detecting factual inconsistencies but fails on logical fallacies, while verifying externalized reasoning shows the opposite pattern. Combining both approaches through structured reasoning consistency achieves superior [hallucination detection](../core-concepts/hallucination-detection.md).[^13]

```svg
<svg viewBox="0 0 720 320" xmlns="http://www.w3.org/2000/svg" font-family="monospace" font-size="12">
  <text x="360" y="25" text-anchor="middle" font-size="15" font-weight="bold" fill="#1a1a2e">Interpretability Methods: From Activations to Weights (2026)</text>

  <!-- Three columns -->
  <!-- Activation-based -->
  <rect x="20" y="50" width="210" height="180" rx="8" fill="#E3F2FD" stroke="#1565C0" stroke-width="2"/>
  <text x="125" y="72" text-anchor="middle" font-size="11" font-weight="bold" fill="#1565C0">Activation-Based</text>
  <text x="125" y="88" text-anchor="middle" font-size="9" fill="#666">(2022-2025)</text>
  <text x="125" y="110" text-anchor="middle" font-size="9">Sparse Autoencoders</text>
  <text x="125" y="126" text-anchor="middle" font-size="9">Activation Patching</text>
  <text x="125" y="142" text-anchor="middle" font-size="9">Probing Classifiers</text>
  <rect x="40" y="158" width="170" height="30" rx="4" fill="#BBDEFB"/>
  <text x="125" y="177" text-anchor="middle" font-size="8" fill="#1565C0">Requires forward pass</text>
  <rect x="40" y="194" width="170" height="30" rx="4" fill="#90CAF9"/>
  <text x="125" y="213" text-anchor="middle" font-size="8" fill="#1565C0">Finds WHAT activates</text>

  <!-- Weight-based (new) -->
  <rect x="255" y="50" width="210" height="180" rx="8" fill="#E8F5E9" stroke="#2E7D32" stroke-width="2"/>
  <text x="360" y="72" text-anchor="middle" font-size="11" font-weight="bold" fill="#2E7D32">Weight-Based (NEW)</text>
  <text x="360" y="88" text-anchor="middle" font-size="9" fill="#666">(2026 — ICLR)</text>
  <text x="360" y="110" text-anchor="middle" font-size="9">WeightLens: interpret from</text>
  <text x="360" y="126" text-anchor="middle" font-size="9">learned weights directly</text>
  <text x="360" y="142" text-anchor="middle" font-size="9">No data or forward pass needed</text>
  <rect x="275" y="158" width="170" height="30" rx="4" fill="#C8E6C9"/>
  <text x="360" y="177" text-anchor="middle" font-size="8" fill="#2E7D32">No forward pass needed</text>
  <rect x="275" y="194" width="170" height="30" rx="4" fill="#A5D6A7"/>
  <text x="360" y="213" text-anchor="middle" font-size="8" fill="#2E7D32">Finds WHAT is encoded</text>

  <!-- Circuit-based (new) -->
  <rect x="490" y="50" width="210" height="180" rx="8" fill="#FFF3E0" stroke="#FF9800" stroke-width="2"/>
  <text x="595" y="72" text-anchor="middle" font-size="11" font-weight="bold" fill="#E65100">Circuit-Level (NEW)</text>
  <text x="595" y="88" text-anchor="middle" font-size="9" fill="#666">(2026 — ICLR)</text>
  <text x="595" y="110" text-anchor="middle" font-size="9">CircuitLens: how features</text>
  <text x="595" y="126" text-anchor="middle" font-size="9">arise from component</text>
  <text x="595" y="142" text-anchor="middle" font-size="9">interactions</text>
  <rect x="510" y="158" width="170" height="30" rx="4" fill="#FFE0B2"/>
  <text x="595" y="177" text-anchor="middle" font-size="8" fill="#E65100">Traces information flow</text>
  <rect x="510" y="194" width="170" height="30" rx="4" fill="#FFCC80"/>
  <text x="595" y="213" text-anchor="middle" font-size="8" fill="#E65100">Finds HOW circuits work</text>

  <!-- Unified insight -->
  <rect x="20" y="248" width="680" height="55" rx="8" fill="#F3E5F5" stroke="#7B1FA2" stroke-width="1.5"/>
  <text x="360" y="270" text-anchor="middle" font-size="11" font-weight="bold" fill="#7B1FA2">Unified Attribution (2026): All three share mathematical foundations</text>
  <text x="360" y="290" text-anchor="middle" font-size="10">Feature attribution + Data attribution + Component attribution = one framework</text>
</svg>
```

### Concept Bottleneck Models for Education

Kim et al. (2025) extended interpretability to educational AI with **concept bottleneck models** that force the model to first predict human-interpretable concepts, then use those concepts to make final predictions.[^8] In a chemistry tutoring system, the model first identifies relevant concepts (reaction type, functional groups, thermodynamic favorability) before generating an explanation — allowing students to see and correct the model's conceptual reasoning.

### Interpretability for Simulation-Based Learning

Interpretability tools are increasingly applied to [world models](world-models.md) and [predictive simulation learning](../frontier-topics/predictive-simulation-learning.md). Li et al. (2026) used SAEs to identify features in a physics simulation model that correspond to intuitive physics concepts (gravity, friction, conservation of momentum), demonstrating that learned world models develop representations that align with human physical intuition.[^9]

### Connection to AI Learning

For AI-assisted learning, interpretability enables:

1. **Explainable tutoring**: Models that can show *why* they believe an answer, not just what the answer is — connecting to [curriculum learning](curriculum-learning.md) principles
2. **Trust calibration**: Learners can assess model confidence by examining which features activate for a given response
3. **Debugging misconceptions**: Identifying features that encode incorrect beliefs, enabling targeted correction through [recursive self-improvement](../frontier-topics/recursive-self-improvement.md)
4. **Transparent e-commerce recommendations**: [AI e-commerce learning](../frontier-topics/ai-ecommerce-learning.md) systems that can explain *why* a product was recommended by showing which features drove the recommendation
5. **Simulation debugging**: Understanding what a simulation model has learned helps educators identify when the simulation's internal physics diverges from reality

## Limitations / Challenges

1. **Scalability gap**: Most detailed mechanistic analyses have been done on small models; frontier models (100B+ parameters) remain largely opaque
2. **Feature splitting**: SAEs sometimes split a single semantic concept across multiple features, complicating interpretation
3. **Dead features**: A significant fraction of SAE features never activate on natural text, representing wasted capacity[^4]
4. **Evaluation problem**: There is no ground truth for "correct" interpretations — we cannot independently verify that a feature labeled "deception" truly represents deception
5. **Computational cost**: Training SAEs for large models requires significant compute (comparable to pretraining costs for the SAE itself)

## See Also / Connections

**Core Concepts:**
- [Hallucination Detection](../core-concepts/hallucination-detection.md) — interpretability reveals *why* models hallucinate
- [The AI Scientist](../core-concepts/the-ai-scientist.md) — interpretable models enable auditable automated research
- [Foundation Models for Research](../core-concepts/foundation-models-for-research.md) — interpreting the base models

**Tools & Platforms:**
- [Aider](../tools-platforms/aider.md) — AI coding tools whose behavior benefits from interpretability
- [HuggingFace Papers API](../tools-platforms/huggingface-papers-api.md) — tracking interpretability research

**Methodologies:**
- [World Models](world-models.md) — internal representations that interpretability aims to decode
- [Curriculum Learning](curriculum-learning.md) — interpretability enables adaptive curriculum design
- [Test-Time Compute](test-time-compute.md) — understanding what models compute during extended reasoning

**Frontier Topics:**
- [Recursive Self-Improvement](../frontier-topics/recursive-self-improvement.md) — self-modifying systems need interpretability safeguards
- [AI Safety in Research](../frontier-topics/ai-safety-in-research.md) — interpretability as a safety mechanism
- [Predictive Simulation Learning](../frontier-topics/predictive-simulation-learning.md) — interpreting learned world models

**Research Sources:**
- [Key Papers](../research-sources/key-papers.md) — seminal interpretability papers
- [Institutions and Labs](../research-sources/institutions-and-labs.md) — Anthropic, DeepMind, MATS as interpretability leaders

## References

[^1]: Elhage, N., Hume, T., Olsson, C., Schiefer, N., Henighan, T., Kravec, S., ... & Olah, C. (2022). "Toy Models of Superposition." *Transformer Circuits Thread*. https://transformer-circuits.pub/2022/toy_model/index.html

[^2]: Templeton, A., Conerly, T., Marcus, J., Lindsey, J., Bricken, T., Chen, B., ... & Olah, C. (2024). "Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet." *Anthropic Research*. https://transformer-circuits.pub/2024/scaling-monosemanticity/

[^3]: Olah, C., Cammarata, N., Schubert, L., Goh, G., Petrov, M., & Carter, S. (2020). "Zoom In: An Introduction to Circuits." *Distill*. https://doi.org/10.23915/distill.00024.001

[^4]: Tang, Y., Saini, H., Yao, Z., Lin, Z., Liao, Y., Li, Q., Du, M., & Liu, D. (2025). "A Unified Theory of Sparse Dictionary Learning in Mechanistic Interpretability." arXiv:2512.05534. https://arxiv.org/abs/2512.05534

[^5]: Draye, F., Lei, A., Pan, H., Posner, I., & Scholkopf, B. (2025). "Sparse Attention Post-Training for Mechanistic Interpretability." arXiv:2512.05865. https://arxiv.org/abs/2512.05865

[^6]: Sharkey, L., Chughtai, B., Batson, J., et al. (2025). "Open Problems in Mechanistic Interpretability." arXiv:2501.16496. https://arxiv.org/abs/2501.16496

[^7]: Conmy, A., Mavor-Parker, A., Lynch, A., Heimersheim, S., & Garriga-Alonso, A. (2026). "Attribution Patching at Scale: Identifying Causal Circuits in Frontier Models." *ICML 2026*. arXiv:2602.07891.

[^8]: Kim, B., Wattenberg, M., Gilmer, J., Cai, C., Wexler, J., & Viégas, F. (2025). "Concept Bottleneck Models for Interpretable Educational AI." *NeurIPS 2025*. arXiv:2510.14332.

[^9]: Li, Z., Chen, Y., & Tenenbaum, J. B. (2026). "Interpreting Learned Physics: Sparse Autoencoders Reveal Intuitive Physics in World Models." arXiv:2601.19443.

[^10]: Anonymous. (2026). "Mechanistic Interpretability for Large Language Model Alignment: Progress, Challenges, and Future Directions." arXiv:2602.11180. https://arxiv.org/abs/2602.11180

[^11]: Anonymous. (2026). "Circuit Insights: Towards Interpretability Beyond Activations (WeightLens & CircuitLens)." arXiv:2510.14936. Published at ICLR 2026. https://arxiv.org/abs/2510.14936

[^12]: Anonymous. (2026). "Towards Unified Attribution in Explainable AI, Data-Centric AI, and Mechanistic Interpretability." arXiv:2501.18887. https://arxiv.org/abs/2501.18887

[^13]: Anonymous. (2026). "Hallucination Detection via Internal States and Structured Reasoning Consistency in LLMs." arXiv:2510.11529. https://arxiv.org/abs/2510.11529
