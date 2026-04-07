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

### Connection to AI Learning

For AI-assisted learning, interpretability enables:

1. **Explainable tutoring**: Models that can show *why* they believe an answer, not just what the answer is — connecting to [curriculum learning](curriculum-learning.md) principles
2. **Trust calibration**: Learners can assess model confidence by examining which features activate for a given response
3. **Debugging misconceptions**: Identifying features that encode incorrect beliefs, enabling targeted correction through [recursive self-improvement](../frontier-topics/recursive-self-improvement.md)

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
