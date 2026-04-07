# Open-Ended Discovery

**Open-Ended Discovery** refers to AI systems that explore without predefined boundaries -- continuously generating novel, increasingly complex artifacts (ideas, code, environments, research) without converging to a fixed point or requiring human guidance for each new direction.

## Overview

Most AI systems optimize toward a fixed goal. Open-ended systems, by contrast, are designed to **endlessly innovate** -- producing an unbounded stream of novel and interesting outputs, much like biological evolution or the open-ended nature of human creativity.

This concept is central to the long-term vision of [automated scientific discovery](../core-concepts/automated-scientific-discovery.md): a system that doesn't just run one experiment but continuously discovers new research directions, each building on the last.

## Background / Theoretical Foundations

### Why Open-Endedness Matters for AI Learning

Open-ended discovery is not merely an academic curiosity — it represents a fundamental shift in how AI systems can support learning. Traditional AI tutoring and recommendation systems operate within bounded solution spaces: a finite set of answers, products, or lesson plans. Open-ended systems, by contrast, can generate **entirely new learning materials, research questions, and conceptual connections** that no human designer anticipated.[^8] This makes them powerful tools for subjects where the knowledge frontier is expanding faster than curricula can be updated — precisely the situation in AI research itself.

For real-world applications, open-ended discovery principles are being adapted to:
- **Personalized education** — generating novel practice problems tailored to individual learning gaps
- **E-commerce product innovation** — discovering untapped product categories through open-ended market exploration (see [AI E-Commerce Learning](ai-ecommerce-learning.md))
- **Scientific research training** — teaching students to formulate novel research questions rather than just answering known ones

### Artificial Life and Open-Endedness

The concept originates from artificial life research, where researchers sought to create simulated environments that exhibit the same kind of open-ended innovation seen in biological evolution[^1]:

- **Tierra** (Ray, 1991) -- Self-replicating programs that evolve in a digital ecosystem
- **Avida** (Lenski et al., 2003) -- Digital organisms evolving novel functions
- **NEAT/HyperNEAT** (Stanley, 2002) -- Evolving neural network topologies

### The Open-Endedness Problem

A system is truly open-ended if it can:
1. **Continuously produce novelty** -- Not converge to a fixed set of solutions
2. **Generate increasing complexity** -- Not just random variation but structured innovation
3. **Build on itself** -- New discoveries serve as stepping stones for future discoveries
4. **Surprise** -- Produce outputs that weren't predictable from the system's initial conditions

## Open-Ended AI Research Systems

### OMNI-EPIC
Faldor et al. (2025) introduced OMNI-EPIC, which uses models of human interestingness to generate environments programmed in code[^2]. The system continuously creates novel, interesting environments without human supervision, demonstrating that open-ended generation can be guided by learned notions of what humans find engaging.

### Automated Capability Discovery
Lu, Hu & Clune (2025) demonstrated that AI systems can discover their own new capabilities through self-exploration, expanding the frontier of what they can do without human-specified objectives[^3]. This work bridges open-ended discovery with [automated scientific discovery](../core-concepts/automated-scientific-discovery.md) by showing that the search for novel capabilities itself can be automated.

### Automated Design of Agentic Systems
Hu, Lu & Clune (2025) achieved meta-level open-endedness: an AI system that designs new AI agent architectures, which themselves can be more capable[^4]. This creates a recursive loop where better agents design even better agents — a concrete implementation of the [recursive self-improvement](recursive-self-improvement.md) paradigm.

### The AI Scientist (Template-Free Mode)
[The AI Scientist](../core-concepts/the-ai-scientist.md) in template-free mode approximates open-ended research: it generates its own ideas, explores them via [Agentic Tree Search](../methodologies/agentic-tree-search.md), and the archive of explored ideas grows over time[^5]. The v2 system (Lu et al., 2026) demonstrated that template-free exploration can produce workshop-quality research papers across diverse ML subfields.

### Autoresearch
[Autoresearch](../tools-platforms/autoresearch.md) exhibits a simpler form: the agent continuously proposes and tests modifications, accumulating improvements that compound over time.

### Open-Ended Learning in Foundation Models
Recent work (2025-2026) has shown that foundation models themselves exhibit open-ended learning behaviors when given appropriate environments. Gao et al. (2025) demonstrated that LLM agents placed in open-ended sandbox environments spontaneously develop novel problem-solving strategies not present in their training data[^9]. This suggests that the capacity for open-ended discovery may be an emergent property of sufficient model scale combined with rich interaction environments.

### Self-Evolving Agents
A comprehensive survey by Wang et al. (2025) documents the emergence of **self-evolving agents** — systems that adaptively reason, act, and evolve in real time within open-ended interactive environments[^11]. The survey identifies three evolution dimensions: what evolves (knowledge, skills, architecture), when evolution occurs (online vs. offline), and how evolution is driven (intrinsic curiosity vs. external feedback). This taxonomy provides a framework for understanding how open-ended discovery can be systematically engineered rather than merely hoped for.

### Curiosity-Driven Open-Ended Exploration
Curiosity as a driver of open-endedness has received renewed attention. Niu et al. (2025) introduced **Curiosity-Driven RLHF (CD-RLHF)**, incorporating intrinsic curiosity rewards into reinforcement learning from human feedback to optimize both diversity and alignment quality in text generation[^12]. Meanwhile, a scalable curiosity-driven game-theoretic framework (2026) demonstrated that moderate curiosity achieves maximum performance in data mining tasks, establishing scaling principles for curiosity-guided exploration[^13]. These results suggest that curiosity is not just a metaphor but a quantifiable algorithmic ingredient for open-endedness.

### Quality-Diversity Self-Play (QDSP)
The **QDSP** algorithm (2025) combines quality-diversity optimization with foundation model self-play, introducing a dimensionless MAP-Elites variant that discovers diverse sophisticated strategies without manually specifying behavioral dimensions[^14]. This is significant because traditional QD algorithms require human-designed feature spaces — QDSP eliminates this bottleneck by having the foundation model propose and evaluate its own diversity dimensions, enabling truly open-ended strategy discovery.

## The Archive Mechanism

A key architectural pattern in open-ended systems is the **archive** -- a growing collection of discovered artifacts that serves as the substrate for future exploration:

```
Idea Archive
├── Explored ideas (with results)
├── Discarded ideas (with reasons)
├── Active ideas (in progress)
└── Generated ideas (waiting for exploration)

Each new idea is generated in the context of the full archive,
enabling the system to build on past work and avoid repetition.
```

The AI Scientist uses this pattern: it iteratively grows an archive of research directions, with each new idea informed by what has already been tried.

## Quality-Diversity Optimization

A key algorithmic family for open-ended search:

- **MAP-Elites** -- Maintain a map of diverse, high-quality solutions across behavioral dimensions[^10]
- **Quality-Diversity (QD) algorithms** -- Optimize for both quality and diversity simultaneously
- **Novelty Search** -- Explicitly reward novelty rather than fitness[^1]

These algorithms prevent the "collapse to monoculture" problem where AI systems converge on a single solution type. The Darwin Godel Machine[^6] and Hyperagents[^7] both use QD-inspired approaches to evolve diverse agent populations, showing that these algorithms scale to the agent design space itself.

### Application to Real-World Learning

Quality-diversity principles have direct implications for AI-powered education and e-commerce:

- **Diverse learning paths**: Rather than optimizing for a single "best" curriculum, QD algorithms can generate a diverse archive of effective learning sequences, each suited to different learner profiles[^10]
- **Product discovery**: In e-commerce, QD approaches can explore the space of product recommendations to surface novel, diverse suggestions rather than converging on popularity-based monoculture (see [AI E-Commerce Learning](ai-ecommerce-learning.md))
- **Research exploration**: Scientists using QD-powered tools can explore a broader set of experimental approaches, reducing the risk of missing important research directions

## Challenges

1. **Defining interestingness** -- What makes a discovery "interesting" enough to pursue?
2. **Evaluation at scale** -- How to assess quality of open-ended outputs without human review
3. **Compute cost** -- Open-ended exploration is expensive by definition
4. **Safety** -- Unbounded exploration can produce harmful or dangerous discoveries
5. **Degenerate solutions** -- Systems that exploit their evaluation metric without genuine innovation
6. **Knowledge accumulation** -- How to ensure each generation builds meaningfully on the last

### Improvisation and Open-Endedness
Drawing parallels between human creativity and artificial open-endedness, Bown et al. (2025) explored how insights from musical improvisation — real-time generation of novel, contextually appropriate responses — can inform the design of open-ended AI systems[^15]. Their key insight: human improvisation succeeds not by random exploration but by maintaining a repertoire of patterns that can be recombined in context-sensitive ways. This suggests that open-ended AI systems should maintain structured archives of reusable components rather than searching from scratch.

## The Scaling Hypothesis

A central bet in open-ended discovery: as [foundation models](../core-concepts/foundation-models-for-research.md) improve, the quality and creativity of AI-generated research will improve correspondingly. The AI Scientist paper notes: "once a new capability starts to work, it becomes superhuman surprisingly soon."

## Connections to Emerging Topics

Open-ended discovery intersects with several rapidly developing areas:

- **Recursive self-improvement** -- [Recursive Self-Improvement](recursive-self-improvement.md) can be viewed as open-ended discovery applied to the agent's own architecture. The Darwin Godel Machine (Zhang et al., 2025) and Hyperagents (Zhang et al., 2026) evolve agent codebases using quality-diversity principles that parallel MAP-Elites.[^6][^7]
- **Predictive simulation** -- [Predictive Simulation Learning](predictive-simulation-learning.md) enables open-ended systems to evaluate candidate ideas before committing compute, improving exploration efficiency.
- **E-commerce application** -- The product and trend space in e-commerce is effectively unbounded, making [AI for E-Commerce Learning](ai-ecommerce-learning.md) a natural domain for open-ended discovery principles.

## See Also

- [The AI Scientist](../core-concepts/the-ai-scientist.md)
- [Automated Scientific Discovery](../core-concepts/automated-scientific-discovery.md)
- [Foundation Models for Research](../core-concepts/foundation-models-for-research.md)
- [Template-Free Research](../methodologies/template-free-research.md)
- [Agentic Tree Search](../methodologies/agentic-tree-search.md)
- [HuggingFace Papers API](../tools-platforms/huggingface-papers-api.md)
- [Scaling Laws for Research Automation](scaling-laws-research.md)
- [AI Safety in Automated Research](ai-safety-in-research.md)
- [Recursive Self-Improvement](recursive-self-improvement.md)
- [Predictive Simulation Learning](predictive-simulation-learning.md)
- [Key Papers and References](../research-sources/key-papers.md)
- [Tracking AI Research](../research-sources/tracking-ai-research.md)
- [Institutions and Labs](../research-sources/institutions-and-labs.md)

## References

[^1]: Stanley, K.O. & Lehman, J. (2015). *Why Greatness Cannot Be Planned: The Myth of the Objective*. Springer.
[^2]: Faldor, M. et al. (2025). "OMNI-EPIC: open-endedness via models of human notions of interestingness with environments programmed in code." *ICLR 2025*. [arXiv:2408.01399](https://arxiv.org/abs/2408.01399)
[^3]: Lu, C., Hu, S. & Clune, J. (2025). "Automated capability discovery via model self-exploration." [arXiv:2502.07577](https://arxiv.org/abs/2502.07577)
[^4]: Hu, S., Lu, C. & Clune, J. (2025). "Automated design of agentic systems." *ICLR 2025*. [arXiv:2408.08435](https://arxiv.org/abs/2408.08435)
[^5]: Lu, C. et al. (2026). "Towards end-to-end automation of AI research." *Nature*, 651(8107). [doi:10.1038/s41586-025-08865-0](https://doi.org/10.1038/s41586-025-08865-0)
[^6]: Zhang, J. et al. (2025). "Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents." [arXiv:2505.22954](https://arxiv.org/abs/2505.22954)
[^7]: Zhang, J. et al. (2026). "Hyperagents." [arXiv:2603.19461](https://arxiv.org/abs/2603.19461)
[^8]: Clune, J. (2019). "AI-Generating Algorithms, an Alternate Paradigm for Producing General Artificial Intelligence." [arXiv:1905.10985](https://arxiv.org/abs/1905.10985)
[^9]: Gao, L. et al. (2025). "Emergent Open-Ended Behavior in LLM Agent Sandboxes." [arXiv:2503.14847](https://arxiv.org/abs/2503.14847)
[^10]: Mouret, J.-B. & Clune, J. (2015). "Illuminating search spaces by mapping elites." [arXiv:1504.04909](https://arxiv.org/abs/1504.04909)
[^11]: Wang, Z. et al. (2025). "A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve." [arXiv:2507.21046](https://arxiv.org/abs/2507.21046)
[^12]: Niu, Y. et al. (2025). "Curiosity-Driven Reinforcement Learning from Human Feedback." [arXiv:2501.11463](https://arxiv.org/abs/2501.11463)
[^13]: Various (2026). "A Scalable Curiosity-Driven Game-Theoretic Framework." [arXiv:2602.15330](https://arxiv.org/abs/2602.15330)
[^14]: Various (2025). "Open-Ended Strategy Innovation via Foundation Models (QDSP)." RLC 2025.
[^15]: Bown, O. et al. (2025). "On Improvisation and Open-Endedness: Insights for Experiential AI." [arXiv:2511.00529](https://arxiv.org/abs/2511.00529)
