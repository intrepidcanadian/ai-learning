---
title: Test-Time Compute Scaling
type: concept
category: methodologies
tags: []
created: 2026-04-09
updated: 2026-04-09
sources: []
---

# Test-Time Compute Scaling

## Overview

**Test-time compute scaling** is the practice of allocating additional computation during inference (rather than training) to improve AI model performance on individual problems. While traditional scaling laws focus on increasing model size and training data, test-time scaling demonstrates that **how much a model thinks at inference time** can be as important as how much it was trained. This paradigm shift — from "bigger models" to "more thinking per problem" — has profound implications for AI-assisted learning: a tutor that thinks longer about a difficult student question can provide a better answer without needing a larger model. Test-time scaling connects directly to [test-time compute](test-time-compute.md) (which covers the foundational techniques) and extends the analysis to the scaling laws and economic trade-offs that determine optimal compute allocation.

## Background / Theoretical Foundations

### The Inference Scaling Paradigm

Traditional AI scaling follows Chinchilla-style laws: optimal performance comes from balancing model size and training tokens for a fixed compute budget. Test-time compute scaling introduces a third dimension — **inference compute** — that can be traded off against model size and training:

| Scaling Dimension | What Increases | Cost Profile | When It Helps Most |
|-------------------|---------------|-------------|-------------------|
| Model size | Parameters (weights) | Fixed per-token cost | General capability |
| Training data | Tokens seen during training | One-time training cost | Knowledge breadth |
| Inference compute | Tokens generated per problem | Per-problem variable cost | Hard problems requiring reasoning |

The key insight: for many tasks, spending 10× more compute at inference time on a smaller model outperforms a 10× larger model with standard inference.[^1]

### From Chain-of-Thought to Compute-Optimal Reasoning

The progression of test-time compute techniques:

1. **Chain-of-thought (2022)**: Generate intermediate reasoning steps before the answer
2. **Self-consistency (2023)**: Sample multiple reasoning paths and vote on the answer
3. **Best-of-N (2024)**: Generate N candidates and select the best using a verifier
4. **Search-augmented generation (2025)**: Use tree search to explore reasoning paths systematically
5. **Train-to-test scaling laws (2026)**: Jointly optimize training and inference budgets for total compute efficiency[^2]

## Technical Details / Key Systems

### Train-to-Test (T2) Scaling Laws (2026)

Roberts et al. (2026) introduce Train-to-Test (T2) scaling laws that jointly optimize model size, training tokens, and inference samples.[^2] The key finding: **when accounting for inference cost, optimal pretraining shifts radically into overtraining regimes**. Specifically:

- A model trained for 2× longer than Chinchilla-optimal becomes more compute-efficient when test-time scaling is applied
- The optimal model is **smaller but more overtrained** than Chinchilla predicts, because smaller models are cheaper to run at inference time
- For a fixed total compute budget (training + inference), T2 laws recommend 30-50% smaller models trained on 2-3× more data

This has immediate practical implications: organizations deploying AI tutoring systems should prefer smaller, longer-trained models that can leverage test-time scaling for difficult questions.

### Reasoning Memory: Procedural Knowledge at Scale (2026)

A complementary approach to scaling test-time compute: instead of generating more reasoning tokens, **reuse prior problem-solving experience**.[^3] The Reasoning Memory framework:

1. Indexes solved problems and their reasoning traces in a retrieval database
2. At inference time, retrieves similar solved problems as context
3. The model adapts retrieved reasoning strategies to the new problem

Results: Reasoning Memory **consistently outperforms both RAG and compute-matched scaling baselines** across six math, science, and coding benchmarks. The implication is that test-time compute can be spent on *retrieval and adaptation* rather than *generation from scratch*.

This connects to [retrieval-augmented generation](../core-concepts/retrieval-augmented-generation.md) — Reasoning Memory is a specialized form of RAG where what's retrieved is not factual knowledge but *reasoning procedures*.

### AdaFuse: Adaptive Multi-Model Ensemble (2026)

Cui et al. (2026) introduce AdaFuse, which dynamically fuses multiple LLMs during generation using uncertainty-based confidence metrics.[^4] The system:

- Maintains a panel of diverse models (different sizes, architectures, training data)
- At each generation step, estimates confidence from each model
- Fuses outputs using **diversity-aware exploration** — preferring models that disagree with the current consensus when confidence is low

Results: AdaFuse improves QA, reasoning, and translation tasks while providing a natural mechanism for scaling test-time compute — adding more models to the panel increases inference compute and performance.

### Parallel Test-Time Scaling for Latent Reasoning (2026)

You et al. (2026) extend test-time scaling to **latent reasoning models** where intermediate reasoning unfolds in continuous vector spaces rather than explicit chain-of-thought tokens.[^5] Key innovations:

- **Parallel scaling**: Multiple reasoning trajectories are explored simultaneously rather than sequentially
- **Latent space reasoning**: Internal representations undergo iterative refinement without generating text tokens
- **Efficiency gains**: Latent reasoning avoids the token generation bottleneck, enabling 3-5× more reasoning paths for the same compute budget

This represents a fundamental shift: test-time compute scaling need not produce visible "thinking" — the model can think deeply in its internal representations.

### Adaptive Compute Allocation via Verifier Guidance (2026)

Li et al. (2026) propose treating test-time compute allocation as an **adaptive per-prompt decision** guided by a Process Reward Model (PRM).[^7] The framework:

- Uses a PRM as a unified control signal for both pruning (stopping unpromising paths early) and expansion (allocating more compute to promising ones)
- Dynamically adjusts the number of reasoning steps based on problem difficulty — easy problems get minimal compute, hard problems get extensive search
- Achieves the same accuracy as uniform Best-of-64 sampling with only **8-12 average samples per problem**

This is directly relevant for AI-assisted learning: an adaptive tutoring system could spend 10× more compute generating explanations for concepts a student is struggling with, while providing quick answers to straightforward questions — connecting to [curriculum learning](curriculum-learning.md).

### Recurrent-Depth for Vision-Language-Action Models (2026)

RD-VLA (Chen et al., 2026) extends test-time scaling to **embodied AI** through latent iterative refinement with a recurrent, weight-tied action head.[^8] Key results:

- Tasks that failed with single-iteration inference exceeded **90% success rate with four iterations** of latent reasoning
- The recurrent depth approach enables computational adaptivity without modifying the base model architecture
- Demonstrates that test-time compute scaling generalizes beyond text — applicable to robotics, autonomous navigation, and physical simulation

This bridges [predictive simulation learning](../frontier-topics/predictive-simulation-learning.md) and test-time scaling: the model simulates outcomes through iterative latent refinement before committing to an action.

### Budget-Aware Inference: Plan and Budget (2025-2026)

The Budget Allocation Model (BAM) by Zhang et al. (2025) introduces **budget-aware test-time scaling** that decomposes complex queries into sub-questions and allocates token budgets based on estimated complexity.[^9] The approach:

- Estimates the difficulty of each sub-problem before allocating compute
- Produces a "reasoning plan" that allocates token budgets proportionally to sub-problem complexity
- Achieves comparable accuracy to unconstrained reasoning while using **40-60% fewer tokens**

For educational applications, this means AI tutors can provide detailed step-by-step explanations within a fixed compute budget — making high-quality AI tutoring economically viable at scale. This connects to [computational cost](computational-cost.md) — budget-aware inference makes test-time scaling practical for cost-sensitive deployments.

### Deep-Thinking Tokens (2026)

Lu et al. (2026) identify **deep-thinking tokens** — positions in the generation where internal predictions undergo significant revisions in deeper layers.[^6] These tokens mark moments of genuine cognitive effort rather than routine generation. The Think@n strategy:

- Identifies deep-thinking tokens during generation
- Allocates additional compute (more layers, broader search) at these positions
- Matches self-consistency performance while **significantly reducing total inference cost**

The insight: not all tokens require equal compute. Concentrating resources where the model is "thinking hardest" is more efficient than uniform compute allocation.

```svg
<svg viewBox="0 0 720 420" xmlns="http://www.w3.org/2000/svg" font-family="monospace" font-size="12">
  <text x="360" y="25" text-anchor="middle" font-size="15" font-weight="bold" fill="#1a1a2e">Test-Time Compute Scaling: From Uniform to Adaptive</text>

  <!-- Traditional approach -->
  <rect x="20" y="50" width="330" height="160" rx="10" fill="#FFF3E0" stroke="#FF9800" stroke-width="2"/>
  <text x="185" y="72" text-anchor="middle" font-size="12" font-weight="bold" fill="#E65100">Traditional: Uniform Compute</text>

  <!-- Token bars - uniform -->
  <rect x="40" y="90" width="20" height="60" rx="3" fill="#FFB74D"/>
  <rect x="70" y="90" width="20" height="60" rx="3" fill="#FFB74D"/>
  <rect x="100" y="90" width="20" height="60" rx="3" fill="#FFB74D"/>
  <rect x="130" y="90" width="20" height="60" rx="3" fill="#FFB74D"/>
  <rect x="160" y="90" width="20" height="60" rx="3" fill="#FFB74D"/>
  <rect x="190" y="90" width="20" height="60" rx="3" fill="#FFB74D"/>
  <rect x="220" y="90" width="20" height="60" rx="3" fill="#FFB74D"/>
  <rect x="250" y="90" width="20" height="60" rx="3" fill="#FFB74D"/>
  <rect x="280" y="90" width="20" height="60" rx="3" fill="#FFB74D"/>
  <rect x="310" y="90" width="20" height="60" rx="3" fill="#FFB74D"/>

  <text x="185" y="170" text-anchor="middle" font-size="9">Each token gets same compute</text>
  <text x="185" y="185" text-anchor="middle" font-size="9" fill="#E65100">Wasteful on easy tokens, insufficient on hard ones</text>
  <text x="185" y="200" text-anchor="middle" font-size="8" fill="#888">Self-consistency, Best-of-N</text>

  <!-- Adaptive approach -->
  <rect x="370" y="50" width="330" height="160" rx="10" fill="#E8F5E9" stroke="#2E7D32" stroke-width="2"/>
  <text x="535" y="72" text-anchor="middle" font-size="12" font-weight="bold" fill="#2E7D32">Adaptive: Compute Where It Matters</text>

  <!-- Token bars - adaptive -->
  <rect x="390" y="125" width="20" height="25" rx="3" fill="#81C784"/>
  <rect x="420" y="120" width="20" height="30" rx="3" fill="#81C784"/>
  <rect x="450" y="80" width="20" height="70" rx="3" fill="#2E7D32"/>
  <text x="460" y="78" text-anchor="middle" font-size="7" fill="#2E7D32">deep</text>
  <rect x="480" y="115" width="20" height="35" rx="3" fill="#81C784"/>
  <rect x="510" y="130" width="20" height="20" rx="3" fill="#A5D6A7"/>
  <rect x="540" y="75" width="20" height="75" rx="3" fill="#2E7D32"/>
  <text x="550" y="73" text-anchor="middle" font-size="7" fill="#2E7D32">deep</text>
  <rect x="570" y="125" width="20" height="25" rx="3" fill="#81C784"/>
  <rect x="600" y="130" width="20" height="20" rx="3" fill="#A5D6A7"/>
  <rect x="630" y="85" width="20" height="65" rx="3" fill="#2E7D32"/>
  <text x="640" y="83" text-anchor="middle" font-size="7" fill="#2E7D32">deep</text>
  <rect x="660" y="120" width="20" height="30" rx="3" fill="#81C784"/>

  <text x="535" y="170" text-anchor="middle" font-size="9">More compute on deep-thinking tokens [6]</text>
  <text x="535" y="185" text-anchor="middle" font-size="9" fill="#2E7D32">Same accuracy, significantly lower total cost</text>
  <text x="535" y="200" text-anchor="middle" font-size="8" fill="#888">Think@n, T2 scaling laws</text>

  <!-- Scaling law comparison -->
  <text x="360" y="235" text-anchor="middle" font-size="13" font-weight="bold" fill="#333">Scaling Law Evolution</text>

  <rect x="20" y="250" width="220" height="80" rx="8" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.5"/>
  <text x="130" y="270" text-anchor="middle" font-size="10" font-weight="bold" fill="#1565C0">Chinchilla (2022)</text>
  <text x="130" y="288" text-anchor="middle" font-size="9">Optimal: balance model</text>
  <text x="130" y="302" text-anchor="middle" font-size="9">size and training data</text>
  <text x="130" y="320" text-anchor="middle" font-size="8" fill="#1565C0">Only training compute</text>

  <line x1="245" y1="290" x2="255" y2="290" stroke="#333" stroke-width="1.5"/>
  <polygon points="253,285 263,290 253,295" fill="#333"/>

  <rect x="260" y="250" width="220" height="80" rx="8" fill="#FFF8E1" stroke="#F57F17" stroke-width="1.5"/>
  <text x="370" y="270" text-anchor="middle" font-size="10" font-weight="bold" fill="#F57F17">Inference Scaling (2024)</text>
  <text x="370" y="288" text-anchor="middle" font-size="9">More inference compute</text>
  <text x="370" y="302" text-anchor="middle" font-size="9">improves reasoning</text>
  <text x="370" y="320" text-anchor="middle" font-size="8" fill="#F57F17">Training OR inference</text>

  <line x1="485" y1="290" x2="495" y2="290" stroke="#333" stroke-width="1.5"/>
  <polygon points="493,285 503,290 493,295" fill="#333"/>

  <rect x="500" y="250" width="200" height="80" rx="8" fill="#E8F5E9" stroke="#2E7D32" stroke-width="1.5"/>
  <text x="600" y="270" text-anchor="middle" font-size="10" font-weight="bold" fill="#2E7D32">T2 Laws (2026) [2]</text>
  <text x="600" y="288" text-anchor="middle" font-size="9">Joint optimization of</text>
  <text x="600" y="302" text-anchor="middle" font-size="9">train + inference compute</text>
  <text x="600" y="320" text-anchor="middle" font-size="8" fill="#2E7D32">Training AND inference</text>

  <!-- Learning application -->
  <rect x="20" y="345" width="680" height="60" rx="8" fill="#EDE7F6" stroke="#4527A0" stroke-width="1.5"/>
  <text x="360" y="367" text-anchor="middle" font-size="12" font-weight="bold" fill="#4527A0">Impact on AI-Assisted Learning</text>
  <text x="360" y="387" text-anchor="middle" font-size="10">Smaller, cheaper models that "think harder" on difficult student questions</text>
  <text x="360" y="401" text-anchor="middle" font-size="10">= democratized access to high-quality AI tutoring without large model costs</text>
</svg>
```

```svg
<svg viewBox="0 0 720 300" xmlns="http://www.w3.org/2000/svg" font-family="monospace" font-size="12">
  <text x="360" y="25" text-anchor="middle" font-size="15" font-weight="bold" fill="#1a1a2e">Budget-Aware Inference: Adaptive Compute Allocation</text>

  <!-- Problem decomposition -->
  <rect x="20" y="50" width="150" height="80" rx="8" fill="#E3F2FD" stroke="#1565C0" stroke-width="2"/>
  <text x="95" y="72" text-anchor="middle" font-size="11" font-weight="bold" fill="#1565C0">Complex Query</text>
  <text x="95" y="92" text-anchor="middle" font-size="9">"Explain why</text>
  <text x="95" y="106" text-anchor="middle" font-size="9">transformers use</text>
  <text x="95" y="120" text-anchor="middle" font-size="9">multi-head attention"</text>

  <line x1="175" y1="90" x2="210" y2="90" stroke="#333" stroke-width="1.5"/>
  <polygon points="208,85 218,90 208,95" fill="#333"/>

  <!-- Sub-problems with budgets -->
  <rect x="220" y="40" width="200" height="30" rx="5" fill="#C8E6C9" stroke="#2E7D32" stroke-width="1.5"/>
  <text x="320" y="60" text-anchor="middle" font-size="9" fill="#2E7D32">Sub-Q1: What is attention? [easy, 50 tokens]</text>

  <rect x="220" y="78" width="200" height="30" rx="5" fill="#FFF9C4" stroke="#F57F17" stroke-width="1.5"/>
  <text x="320" y="98" text-anchor="middle" font-size="9" fill="#F57F17">Sub-Q2: Why multi-head? [medium, 150 tokens]</text>

  <rect x="220" y="116" width="200" height="30" rx="5" fill="#FFCDD2" stroke="#C62828" stroke-width="1.5"/>
  <text x="320" y="136" text-anchor="middle" font-size="9" fill="#C62828">Sub-Q3: Math proof? [hard, 400 tokens]</text>

  <line x1="425" y1="90" x2="460" y2="90" stroke="#333" stroke-width="1.5"/>
  <polygon points="458,85 468,90 458,95" fill="#333"/>

  <!-- Budget allocation -->
  <rect x="470" y="45" width="230" height="105" rx="8" fill="#EDE7F6" stroke="#4527A0" stroke-width="2"/>
  <text x="585" y="65" text-anchor="middle" font-size="11" font-weight="bold" fill="#4527A0">Budget Allocation [9]</text>
  <rect x="485" y="78" width="30" height="12" rx="3" fill="#C8E6C9"/>
  <text x="525" y="88" font-size="8">8% budget → quick answer</text>
  <rect x="485" y="98" width="80" height="12" rx="3" fill="#FFF9C4"/>
  <text x="575" y="108" font-size="8">25% budget → moderate detail</text>
  <rect x="485" y="118" width="190" height="12" rx="3" fill="#FFCDD2"/>
  <text x="575" y="138" font-size="8">67% budget → deep reasoning</text>

  <!-- Comparison bar -->
  <rect x="20" y="175" width="680" height="50" rx="8" fill="#F5F5F5" stroke="#999" stroke-width="1"/>
  <text x="360" y="195" text-anchor="middle" font-size="11" font-weight="bold">Efficiency: Same accuracy, 40-60% fewer tokens than uniform allocation</text>
  <text x="360" y="212" text-anchor="middle" font-size="9" fill="#666">PRM-guided [7] + BAM [9] + Deep-thinking tokens [6] = compute-optimal inference</text>

  <!-- Learning application -->
  <rect x="100" y="240" width="520" height="50" rx="8" fill="#E0F7FA" stroke="#00838F" stroke-width="1.5"/>
  <text x="360" y="260" text-anchor="middle" font-size="12" font-weight="bold" fill="#00838F">For AI Tutoring: Spend More on Hard Concepts, Less on Easy Ones</text>
  <text x="360" y="278" text-anchor="middle" font-size="10">Democratizes high-quality tutoring — same quality at lower per-student cost</text>
</svg>
```

## Current State / Latest Developments

### 2026 Landscape

1. **Joint train-test optimization**: T2 scaling laws unify training and inference budgets, showing that overtraining smaller models is compute-optimal when inference is considered[^2]
2. **Retrieval beats generation**: Reasoning Memory outperforms compute-matched generation by reusing prior reasoning traces, suggesting that AI tutors should build experience databases[^3]
3. **Multi-model fusion**: AdaFuse demonstrates that ensembling diverse models at inference time provides natural test-time scaling with uncertainty estimation[^4]
4. **Latent reasoning**: Parallel test-time scaling in continuous vector spaces achieves 3-5× more reasoning paths per compute dollar than explicit chain-of-thought[^5]
5. **Adaptive compute allocation**: Deep-thinking tokens enable targeted compute investment, matching uniform scaling performance at lower cost[^6]
6. **Verifier-guided pruning**: PRM-based adaptive frameworks achieve Best-of-64 quality with only 8-12 samples on average[^7]
7. **Embodied test-time scaling**: RD-VLA shows that latent iterative refinement enables 90%+ success rates in robotic tasks that fail with single-iteration inference[^8]
8. **Budget-aware inference**: BAM-style systems decompose problems and allocate compute proportionally, saving 40-60% of tokens while maintaining accuracy[^9]
9. **Test-time learning convergence**: Multiple independent groups discover that continuing to learn during deployment produces dramatically better outcomes — connecting to [recursive self-improvement](../frontier-topics/recursive-self-improvement.md)[^1]

### Key Metrics

| System | Year | Key Result |
|--------|------|-----------|
| T2 Scaling Laws | 2026 | 30-50% smaller models via joint train-test optimization[^2] |
| Reasoning Memory | 2026 | Outperforms RAG and compute-matched baselines on 6 benchmarks[^3] |
| AdaFuse | 2026 | Multi-model fusion improves QA, reasoning, and translation[^4] |
| Parallel Latent Scaling | 2026 | 3-5× more reasoning paths at same compute cost[^5] |
| Think@n | 2026 | Matches self-consistency at significantly reduced cost[^6] |
| PRM-Guided Allocation | 2026 | Best-of-64 quality with 8-12 average samples[^7] |
| RD-VLA | 2026 | 90%+ success via iterative latent refinement in robotics[^8] |
| BAM | 2025 | 40-60% token savings via budget-aware decomposition[^9] |

## Limitations / Challenges

1. **Latency**: More inference compute means longer response times — critical for interactive applications like tutoring where students expect quick feedback
2. **Cost unpredictability**: Variable inference compute makes cost forecasting difficult; a "hard" question may cost 100× more than an "easy" one
3. **Diminishing returns**: Test-time scaling shows diminishing returns — doubling compute rarely doubles accuracy, especially on problems near the model's capability frontier
4. **Verification bottleneck**: Many test-time scaling strategies require a verifier to select among candidates, but training reliable verifiers is itself a challenging problem
5. **Benchmark overfitting**: Current test-time scaling techniques are often evaluated on math/coding benchmarks; generalization to open-ended reasoning (e.g., essay writing, creative problem-solving) is unclear
6. **Energy costs**: Spending 10-100× more compute per problem raises sustainability concerns at scale

## See Also / Connections

**Core Concepts:**
- [Foundation Models for Research](../core-concepts/foundation-models-for-research.md) — base models that benefit from test-time scaling
- [Retrieval-Augmented Generation](../core-concepts/retrieval-augmented-generation.md) — Reasoning Memory as specialized RAG
- [Knowledge Distillation](../core-concepts/knowledge-distillation.md) — creating efficient models for test-time scaling

**Tools & Platforms:**
- [HuggingFace Papers API](../tools-platforms/huggingface-papers-api.md) — tracking scaling law research
- [Semantic Scholar API](../tools-platforms/semantic-scholar-api.md) — scaling laws literature

**Methodologies:**
- [Test-Time Compute](test-time-compute.md) — foundational techniques (chain-of-thought, self-consistency)
- [Inference Optimization](inference-optimization.md) — making test-time compute efficient
- [Computational Cost](computational-cost.md) — economics of compute allocation and budget-aware inference
- [Curriculum Learning](curriculum-learning.md) — adaptive difficulty connects to adaptive compute allocation
- [Evaluation Methodology](evaluation-methodology.md) — measuring scaling law effectiveness
- [Prompt Engineering](prompt-engineering.md) — prompt design for compute-efficient reasoning
- [World Models](world-models.md) — internal representations for latent reasoning

**Frontier Topics:**
- [Recursive Self-Improvement](../frontier-topics/recursive-self-improvement.md) — test-time learning as self-improvement during deployment
- [Predictive Simulation Learning](../frontier-topics/predictive-simulation-learning.md) — simulation as a form of test-time compute
- [Scaling Laws Research](../frontier-topics/scaling-laws-research.md) — broader scaling law context
- [Cross-Cutting Connections](../frontier-topics/cross-cutting-connections.md) — test-time learning as convergence point

**Research Sources:**
- [Key Papers](../research-sources/key-papers.md) — foundational scaling law papers
- [Tracking AI Research](../research-sources/tracking-ai-research.md) — monitoring compute scaling research

## References

[^1]: Snell, C., Lee, J., Xu, K., & Kumar, A. (2024). "Scaling LLM Test-Time Compute Optimally Can Be More Effective Than Scaling Model Parameters." arXiv:2408.03314. https://arxiv.org/abs/2408.03314

[^2]: Roberts, N., Cho, S., Gao, Z., Huang, T.-H., Wu, A., et al. (2026). "Test-Time Scaling Makes Overtraining Compute-Optimal." arXiv:2604.01411. https://arxiv.org/abs/2604.01411

[^3]: Anonymous. (2026). "Procedural Knowledge at Scale Improves Reasoning." arXiv:2604.01348. https://arxiv.org/abs/2604.01348

[^4]: Cui, C., Wei, T., Chen, Z., Qiu, R., Zeng, Z., et al. (2026). "AdaFuse: Adaptive Ensemble Decoding with Test-Time Scaling for LLMs." arXiv:2601.06022. https://arxiv.org/abs/2601.06022

[^5]: You, R. et al. (2026). "Parallel Test-Time Scaling for Latent Reasoning Models." arXiv:2510.07745. https://arxiv.org/abs/2510.07745

[^6]: Lu, H. A. et al. (2026). "Think Deep, Not Just Long: Measuring LLM Reasoning Effort via Deep-Thinking Tokens." arXiv preprint.

[^7]: Li, Z. et al. (2026). "What If We Allocate Test-Time Compute Adaptively?" arXiv:2602.01070. https://arxiv.org/abs/2602.01070

[^8]: Chen, H. et al. (2026). "Recurrent-Depth VLA: Implicit Test-Time Compute Scaling of Vision-Language-Action Models via Latent Iterative Reasoning." arXiv:2602.07845. https://arxiv.org/abs/2602.07845

[^9]: Zhang, Y. et al. (2025). "Plan and Budget: Effective and Efficient Test-Time Scaling on Reasoning Large Language Models." arXiv:2505.16122. https://arxiv.org/abs/2505.16122
