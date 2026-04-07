# The AI Scientist

**The AI Scientist** is the first comprehensive system designed to autonomously conduct the entire machine learning research lifecycle — from idea generation to peer-reviewed publication. Developed by [Sakana AI](https://sakana.ai/) in collaboration with researchers from the University of Oxford and the University of British Columbia, it was published in *Nature* (Volume 651, Issue 8107, 2026).[^1]

## Overview

The AI Scientist automates five sequential phases of scientific research:

1. **Idea Generation** — Iteratively grows an archive of research directions and hypotheses within a user-specified ML subfield. Each idea includes a title, reasoning, and experimental plan.
2. **Novelty Filtering** — Connects to the [Semantic Scholar API](../tools-platforms/semantic-scholar-api.md) and web search to discard ideas that too closely resemble existing literature.
3. **Experimentation** — Writes code, runs experiments, collects results, and takes structured notes in the style of an experimental journal.
4. **Manuscript Generation** — Fills a LaTeX conference template section by section, queries literature for citations (up to 20 search rounds), and auto-corrects compilation errors.
5. **Automated Peer Review** — Evaluates the scientific quality of the generated paper using [The Automated Reviewer](automated-peer-review.md).

## Background / Theoretical Foundations

The AI Scientist builds on decades of work in [automated scientific discovery](automated-scientific-discovery.md). Three intellectual threads converge in its design:

### From Expert Systems to Foundation Models
Early automated science systems like DENDRAL (1965) and BACON (1978) used hand-coded heuristics to make discoveries in narrow domains.[^4] The AI Scientist replaces these brittle rules with [foundation models](foundation-models-for-research.md) that can read papers, write code, and reason about experiments using natural language — a qualitative leap in flexibility and scope.

### The Open-Ended Search Paradigm
Jeff Clune's work on open-endedness — systems that continually generate novel artifacts of increasing complexity — directly inspired the AI Scientist's idea generation mechanism.[^5] Rather than optimizing a fixed objective, the system maintains a growing archive of diverse research directions, selecting underexplored areas for investigation. This connects to broader work on [recursive self-improvement](../frontier-topics/recursive-self-improvement.md), where the Darwin Gödel Machine (from the same research group) later demonstrated open-ended agent self-improvement.[^6]

### Agentic Coding as Scientific Method
The system's experimentation phase treats coding as a form of scientific inquiry. By combining AI code generation ([Aider](../tools-platforms/aider.md), Claude Sonnet) with structured experiment design, the AI Scientist implements the scientific method computationally: hypothesize (idea generation), test (code + run), analyze (metrics + [VLM critique](../methodologies/vlm-integration.md)), and communicate (manuscript).[^1]

## Two Operating Modes

### Template-Based Mode
The system extends human-provided code templates as initial scaffolds. The experiment execution proceeds through four stages:
- **Preliminary investigation** — Baseline runs
- **Hyperparameter tuning** — Systematic optimization
- **Research agenda execution** — Core experiments
- **Ablation studies** — Isolating contributions of individual components

Uses [Aider](../tools-platforms/aider.md) as the coding assistant.

### Template-Free Mode
Operates with minimal prior guidance, generating initial code from scratch. Key differences:
- Uses [Agentic Tree Search](../methodologies/agentic-tree-search.md) for experiment exploration
- Leverages multiple specialized models: OpenAI o3 for idea generation, Claude Sonnet 4 for code generation, GPT-4o for vision-language tasks, o4-mini for review
- Includes [VLM integration](../methodologies/vlm-integration.md) for figure critique
- Dynamically accesses datasets from [HuggingFace Hub](../tools-platforms/huggingface-papers-api.md)

See [Template-Free Research](../methodologies/template-free-research.md) for a deep dive.

## Key Results

### Peer Review Milestone
Three AI-generated manuscripts were submitted to the **ICBINB workshop at ICLR 2025** (acceptance rate: 70%). One was accepted with scores of 6, 7, and 6 (weak accept, accept, weak accept), ranking in the top 45% of submissions.[^1]

This represents the first known instance of a fully AI-generated paper passing standard peer review at a top-tier ML conference workshop.

### Automated Reviewer Performance
The Automated Reviewer achieved **69% balanced accuracy** in predicting human reviewer decisions, comparable to inter-human agreement measured in the NeurIPS 2021 consistency study (66% balanced accuracy).[^1]

| Metric | Human (NeurIPS) | Automated Reviewer |
|--------|------------------|--------------------|
| Balanced Accuracy | 0.66 | 0.69 +/- 0.04 |
| F1 Score | 0.49 | 0.62 +/- 0.09 |
| AUC | 0.65 | 0.69 +/- 0.09 |

### Cost
Generating a full research paper costs **$6–$15** and requires approximately **3.5 hours** of human involvement.[^1]

## Current State / Latest Developments (2025–2026)

- **Nature publication (2026):** The AI Scientist v2 paper was published in *Nature* Volume 651, marking a milestone for autonomous AI research systems[^1]
- **Self-improving descendants:** The Darwin Gödel Machine, from the same UBC/Sakana research group, extends the open-ended paradigm to agent self-modification, achieving 50% on SWE-bench through autonomous evolution[^6]
- **VLM-enhanced pipelines:** Multi-agent systems now use VLM-as-a-judge to evaluate scientific figures, achieving 0.7–0.8 pass rates in domain-specific evaluation[^7]
- **World model integration:** Emerging work on [predictive simulation learning](../frontier-topics/predictive-simulation-learning.md) suggests future AI Scientists could learn through simulated environments rather than direct experimentation[^8]
- **ICLR 2026 Workshop on Recursive Self-Improvement:** A dedicated workshop at ICLR 2026 examined how AI systems can recursively improve their own capabilities — directly extending the open-ended paradigm that the AI Scientist pioneered[^9]. Topics included experience-based learning, synthetic data pipelines, and weak-to-strong generalization.
- **Self-evolving agent frameworks:** A comprehensive survey (2025) formalized the taxonomy of self-evolving AI agents, categorizing systems like the AI Scientist under "experience-driven evolution" — agents that improve through accumulated experimental results rather than explicit retraining[^10]
- **Educational applications:** The AI Scientist's methodology is being adapted for teaching research skills — students can observe how an AI conducts research and learn the scientific method by analogy (see [AI E-Commerce Learning](../frontier-topics/ai-ecommerce-learning.md) for applied learning contexts)

### The Emerging AI Scientist Ecosystem

The AI Scientist catalyzed a broader ecosystem of autonomous research systems in 2025-2026:

- **AlphaEvolve (Google DeepMind, 2025):** An evolutionary coding agent that uses LLMs to discover novel algorithms, demonstrating that AI-generated code can outperform hand-crafted solutions on mathematical optimization problems[^11]. While the AI Scientist generates research *papers*, AlphaEvolve generates research *algorithms* — complementary approaches to automating discovery.
- **From AI-for-Science to Agentic Science:** A 2025 survey documented the shift from AI as a passive tool (running simulations, analyzing data) to AI as an active agent that designs and conducts experiments autonomously[^12]. The AI Scientist is positioned as the archetype of this transition.
- **Multi-agent research teams:** Emerging systems deploy multiple specialized AI agents (planner, coder, reviewer, editor) that collaborate on research tasks, mirroring human research group dynamics. This extends the AI Scientist's single-agent pipeline toward collaborative [automated scientific discovery](automated-scientific-discovery.md).

### Practical Applications for Learning

The AI Scientist demonstrates a transferable framework for learning any research-oriented subject:

1. **Hypothesis generation as study technique** — Students can learn to formulate testable hypotheses by studying how the AI Scientist generates and filters research ideas
2. **Iterative experimentation** — The system's four-stage experiment pipeline (baseline → tuning → core → ablation) provides a template for structured inquiry in any domain
3. **Literature-informed thinking** — The novelty filtering step (using [Semantic Scholar](../tools-platforms/semantic-scholar-api.md)) teaches the critical skill of situating new ideas within existing knowledge
4. **Self-critique and revision** — The automated peer review phase models the discipline of evaluating one's own work against objective criteria

## Limitations

- Generates naive or underdeveloped ideas lacking deep methodological rigor
- ~42% of experiments fail due to coding errors (per independent evaluation)[^3]
- Susceptible to hallucinations: inaccurate citations, duplicated figures
- Shallow literature review (median 5 citations per paper)
- Currently limited to **computational ML experiments only**
- Cannot yet consistently meet main conference standards (32% acceptance rate at ICLR 2025 main)

An independent evaluation (Gabryel et al., arXiv:2502.14297) described output quality as resembling "a rushed undergraduate paper," while acknowledging the system as genuine progress toward Artificial Research Intelligence.[^3]

## Ethical Considerations

The Sakana AI team:
- Obtained **IRB approval** before submitting to peer review
- **Withdrew the accepted submission** after acceptance to avoid undisclosed AI content in the literature
- **Watermarks all AI-generated papers** for transparency
- Collaborated with ICLR 2025 leadership and workshop organizers

## Technology Stack

| Component | Model/Tool |
|-----------|------------|
| Idea generation (template-free) | OpenAI o3 |
| Code generation | Claude Sonnet 4, Aider |
| Vision-language tasks | GPT-4o |
| Cost-efficient reasoning | OpenAI o4-mini |
| Literature search | Semantic Scholar API |
| Dataset access | HuggingFace Hub |

## See Also

- [Automated Scientific Discovery](automated-scientific-discovery.md)
- [Automated Peer Review](automated-peer-review.md)
- [Foundation Models for Research](foundation-models-for-research.md)
- [Agentic Tree Search](../methodologies/agentic-tree-search.md)
- [Template-Free Research](../methodologies/template-free-research.md)
- [VLM Integration](../methodologies/vlm-integration.md)
- [Autoresearch (Karpathy)](../tools-platforms/autoresearch.md)
- [Recursive Self-Improvement](../frontier-topics/recursive-self-improvement.md)
- [Predictive Simulation Learning](../frontier-topics/predictive-simulation-learning.md)
- [Institutions and Labs](../research-sources/institutions-and-labs.md)
- [Key Papers and References](../research-sources/key-papers.md)

## References

[^1]: Lu, C., Lu, C., Lange, R.T., Yamada, Y., Hu, S., Foerster, J., Ha, D. & Clune, J. (2026). "Towards end-to-end automation of AI research." *Nature*, 651(8107). [DOI: 10.1038/s41586-026-10265-5](https://doi.org/10.1038/s41586-026-10265-5)
[^2]: Sakana AI. "The AI Scientist: Now Published in Nature." [sakana.ai/ai-scientist-nature](https://sakana.ai/ai-scientist-nature/)
[^3]: Gabryel, M. et al. (2025). "Evaluating Sakana's AI Scientist." [arXiv:2502.14297](https://arxiv.org/abs/2502.14297)
[^4]: Langley, P., Simon, H.A., Bradshaw, G.L. & Zytkow, J.M. (1987). *Scientific Discovery: Computational Explorations of the Creative Process*. MIT Press.
[^5]: Clune, J. (2019). "AI-Generating Algorithms, an Alternate Paradigm for Producing General Artificial Intelligence." arXiv:1905.10985.
[^6]: Zhang, J., Hu, S., Lu, C., Lange, R. & Clune, J. (2025). "Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents." arXiv:2505.22954. https://arxiv.org/abs/2505.22954
[^7]: Enhancing Agentic Autonomous Scientific Discovery authors (2025). "Enhancing Agentic Autonomous Scientific Discovery with Vision-Language Model Capabilities." arXiv:2511.14631. https://arxiv.org/abs/2511.14631
[^8]: Yang, S. (2026). "World Models as an Intermediary between Agents and the Real World." arXiv:2602.00785. https://arxiv.org/abs/2602.00785
[^9]: ICLR 2026 Workshop on AI with Recursive Self-Improvement. [openreview.net/forum?id=OsPQ6zTQXV](https://openreview.net/forum?id=OsPQ6zTQXV)
[^10]: Tao, Z. et al. (2025). "A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve." [arXiv:2507.21046](https://arxiv.org/abs/2507.21046)
[^11]: Novikov, A. et al. (2025). "AlphaEvolve: A Coding Agent for Scientific and Algorithmic Discovery." [arXiv:2506.13131](https://arxiv.org/abs/2506.13131)
[^12]: Lu, Y. et al. (2025). "From AI for Science to Agentic Science." [arXiv:2508.14111](https://arxiv.org/abs/2508.14111)
