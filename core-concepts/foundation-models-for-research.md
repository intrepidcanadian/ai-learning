# Foundation Models for Research

**Foundation models** -- large-scale pretrained models that can be adapted to a wide range of downstream tasks -- are the backbone of modern AI research automation. Their ability to reason, generate code, write natural language, and process visual information makes them the enabling technology behind systems like [The AI Scientist](../core-concepts/the-ai-scientist.md) and [Autoresearch](../tools-platforms/autoresearch.md).

## Overview

A foundation model learns general-purpose representations from massive datasets (text, code, images) via self-supervised learning. For research automation, the key capabilities are:

## Background / Theoretical Foundations

The concept of foundation models emerged from the convergence of three trends: **transfer learning** (reusing representations across tasks), **scaling laws** (predictable performance gains from larger models and datasets), and **self-supervised learning** (learning from unlabeled data). The term was formalized by Bommasani et al. (2021) at Stanford's Center for Research on Foundation Models (CRFM)[^1].

For research automation specifically, foundation models represent a paradigm shift from narrow, task-specific AI to general-purpose reasoning engines. Prior automated research systems required hand-engineered pipelines for each step -- hypothesis generation, experiment design, analysis, and writing were separate subsystems. Foundation models unify these under a single architecture that can be prompted or fine-tuned for each phase[^2].

Key theoretical underpinnings:

- **In-context learning** -- Models learn new tasks from examples provided in the prompt, without weight updates. This enables rapid adaptation to novel research domains[^3].
- **Emergent capabilities** -- Larger models exhibit qualitatively new abilities (chain-of-thought reasoning, tool use) that smaller models lack, enabling more sophisticated research automation[^4].
- **Scaling laws** -- Kaplan et al. (2020) and Hoffmann et al. (2022) showed that model performance scales predictably with compute, data, and parameters. This has direct implications for research quality: better models → better papers (see [Scaling Laws for Research Automation](../frontier-topics/scaling-laws-research.md))[^5].
- **World models** -- Foundation models increasingly serve as implicit world models for predictive simulation (see [Predictive Simulation Learning](../frontier-topics/predictive-simulation-learning.md)). V-JEPA 2, for instance, learns predictive representations from over 1 million hours of video[^6].

The progression from GPT-3 (2020) to GPT-4 (2023) to o3/Claude Opus (2025) has moved foundation models from "interesting but unreliable" to "capable research assistants" -- a trajectory that underpins every system described in this wiki.

## Key Capabilities

For research automation, the key capabilities are:

- **Natural language reasoning** -- Understanding and generating scientific text
- **Code generation** -- Writing, debugging, and modifying experiment code
- **Multi-modal understanding** -- Analyzing figures, plots, and visual data
- **Long-context processing** -- Working with full papers, codebases, and experimental logs
- **Tool use** -- Calling APIs, executing code, searching literature

## Models Used in Research Automation

| Model | Provider | Primary Role in Research Automation |
|-------|----------|-------------------------------------|
| GPT-4o | OpenAI | Vision-language tasks, figure analysis |
| o3 / o4-mini | OpenAI | Deep reasoning, idea generation, cost-efficient review |
| Claude Sonnet 4 / Opus | Anthropic | Code generation, agentic coding |
| Llama 3 | Meta | Open-source experimentation |
| DeepSeek-R1 | DeepSeek | Open-source reasoning |
| Gemini 2.5 | Google | Multi-modal research tasks |

## How Foundation Models Enable Research

### Idea Generation
Models are prompted to generate research hypotheses within a specified domain. Chain-of-thought reasoning and self-reflection improve idea quality. The AI Scientist uses iterative archive-building to grow and filter ideas.

### Code as the Experiment Medium
In computational ML research, the experiment *is* the code. Foundation models that can write, debug, and modify Python code effectively become autonomous experimenters. Key coding tools:
- **[Aider](../tools-platforms/aider.md)** -- Open-source AI coding assistant used by The AI Scientist (template-based mode)
- **Claude Code** -- Agentic coding environment
- **Cursor / Windsurf** -- IDE-integrated AI coding

### Scientific Writing
Models generate LaTeX manuscripts section by section, with iterative refinement passes. Quality scales with model capability -- stronger models produce better introductions, more coherent arguments, and fewer hallucinated citations.

### Literature Search and Synthesis
Models act as agents that:
1. Generate search queries for [Semantic Scholar](../tools-platforms/semantic-scholar-api.md) or [HuggingFace Papers](../tools-platforms/huggingface-papers-api.md)
2. Read and summarize retrieved papers
3. Generate citation justifications
4. Weave references into the manuscript

## Taxonomy of FM Roles in Scientific Discovery

A comprehensive framework by Liu et al. (2025) identifies three levels of foundation model involvement in scientific discovery, each with different autonomy and risk profiles[^11]:

### Level 1: FM as Tool
The model augments human researchers by performing specific, well-defined tasks under direct supervision. Examples include literature summarization via [Semantic Scholar](../tools-platforms/semantic-scholar-api.md), code generation via [Aider](../tools-platforms/aider.md), and statistical analysis assistance. This level is widely deployed and relatively low-risk.

### Level 2: FM as Analyst
The model exhibits greater autonomy in processing complex information — synthesizing multi-paper literature reviews, identifying research gaps, and proposing experimental modifications. [AIDE](../tools-platforms/aide.md) operates at this level, exploring the space of ML solutions with minimal human oversight[^12].

### Level 3: FM as Scientist
The model autonomously conducts major research stages: hypothesis generation, experimental design, execution, and manuscript preparation. [The AI Scientist](the-ai-scientist.md) and its successors represent this frontier. Liang et al. (2025) survey the transition from automation to autonomy, finding that current systems still require human oversight for novelty assessment and ethical review[^13].

### Embodied FM Research Agents
The newest development extends FMs into physical laboratories. Liu et al. (2026) demonstrated FMs generating Python control scripts for scientific instruments — translating user-specified objectives into directly executable lab protocols[^14]. This connects foundation models to real-world [predictive simulation](../frontier-topics/predictive-simulation-learning.md), where the model's predictions are tested against physical outcomes.

## FM Taxonomy for Scientific Discovery

```svg
<svg viewBox="0 0 750 480" xmlns="http://www.w3.org/2000/svg" font-family="monospace" font-size="11">
  <defs>
    <marker id="arrowFM" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#555"/>
    </marker>
  </defs>

  <text x="375" y="22" text-anchor="middle" font-size="14" font-weight="bold" fill="#1a1a2e">Foundation Model Roles in Scientific Discovery</text>

  <!-- Level 1: FM as Tool -->
  <rect x="30" y="50" width="210" height="130" rx="10" fill="#e3f2fd" stroke="#1565C0" stroke-width="2"/>
  <text x="135" y="72" text-anchor="middle" font-weight="bold" fill="#1565C0" font-size="12">Level 1: FM as Tool</text>
  <text x="135" y="92" text-anchor="middle" font-size="9" fill="#333">Human-directed, task-specific</text>
  <line x1="50" y1="100" x2="220" y2="100" stroke="#1565C0" stroke-width="0.5"/>
  <text x="45" y="118" font-size="9" fill="#555">• Literature summarization</text>
  <text x="45" y="133" font-size="9" fill="#555">• Code generation</text>
  <text x="45" y="148" font-size="9" fill="#555">• Statistical analysis</text>
  <text x="45" y="163" font-size="9" fill="#555">• Data visualization</text>

  <!-- Level 2: FM as Analyst -->
  <rect x="270" y="50" width="210" height="130" rx="10" fill="#fff3e0" stroke="#E65100" stroke-width="2"/>
  <text x="375" y="72" text-anchor="middle" font-weight="bold" fill="#E65100" font-size="12">Level 2: FM as Analyst</text>
  <text x="375" y="92" text-anchor="middle" font-size="9" fill="#333">Semi-autonomous reasoning</text>
  <line x1="290" y1="100" x2="460" y2="100" stroke="#E65100" stroke-width="0.5"/>
  <text x="285" y="118" font-size="9" fill="#555">• Multi-paper synthesis</text>
  <text x="285" y="133" font-size="9" fill="#555">• Research gap identification</text>
  <text x="285" y="148" font-size="9" fill="#555">• Experimental modification</text>
  <text x="285" y="163" font-size="9" fill="#555">• AIDE-style ML exploration</text>

  <!-- Level 3: FM as Scientist -->
  <rect x="510" y="50" width="210" height="130" rx="10" fill="#e8f5e9" stroke="#2E7D32" stroke-width="2"/>
  <text x="615" y="72" text-anchor="middle" font-weight="bold" fill="#2E7D32" font-size="12">Level 3: FM as Scientist</text>
  <text x="615" y="92" text-anchor="middle" font-size="9" fill="#333">Fully autonomous research</text>
  <line x1="530" y1="100" x2="700" y2="100" stroke="#2E7D32" stroke-width="0.5"/>
  <text x="525" y="118" font-size="9" fill="#555">• Hypothesis generation</text>
  <text x="525" y="133" font-size="9" fill="#555">• Experiment design + execution</text>
  <text x="525" y="148" font-size="9" fill="#555">• Manuscript preparation</text>
  <text x="525" y="163" font-size="9" fill="#555">• AI Scientist v2 / Nature</text>

  <!-- Arrows between levels -->
  <line x1="245" y1="115" x2="265" y2="115" stroke="#555" stroke-width="1.5" marker-end="url(#arrowFM)"/>
  <line x1="485" y1="115" x2="505" y2="115" stroke="#555" stroke-width="1.5" marker-end="url(#arrowFM)"/>

  <!-- Modalities row -->
  <text x="375" y="210" text-anchor="middle" font-size="12" font-weight="bold" fill="#333">Cross-Cutting Capabilities</text>

  <rect x="30" y="225" width="155" height="75" rx="8" fill="#f3e5f5" stroke="#9C27B0" stroke-width="1.5"/>
  <text x="107" y="245" text-anchor="middle" font-weight="bold" font-size="10" fill="#6A1B9A">Multi-Modal</text>
  <text x="107" y="260" text-anchor="middle" font-size="8">Text + vision + code</text>
  <text x="107" y="275" text-anchor="middle" font-size="8">Gemini 2.5, Intern-S1</text>
  <text x="107" y="290" text-anchor="middle" font-size="8">V-JEPA 2 (video)</text>

  <rect x="205" y="225" width="155" height="75" rx="8" fill="#e0f2f1" stroke="#00695C" stroke-width="1.5"/>
  <text x="282" y="245" text-anchor="middle" font-weight="bold" font-size="10" fill="#00695C">Reasoning</text>
  <text x="282" y="260" text-anchor="middle" font-size="8">Chain-of-thought, search</text>
  <text x="282" y="275" text-anchor="middle" font-size="8">o3, DeepSeek-R1</text>
  <text x="282" y="290" text-anchor="middle" font-size="8">Tree-of-thought scaling</text>

  <rect x="380" y="225" width="155" height="75" rx="8" fill="#fce4ec" stroke="#C62828" stroke-width="1.5"/>
  <text x="457" y="245" text-anchor="middle" font-weight="bold" font-size="10" fill="#C62828">Embodied</text>
  <text x="457" y="260" text-anchor="middle" font-size="8">Lab instrument control</text>
  <text x="457" y="275" text-anchor="middle" font-size="8">Robot planning</text>
  <text x="457" y="290" text-anchor="middle" font-size="8">FOUNDER world models</text>

  <rect x="555" y="225" width="165" height="75" rx="8" fill="#fff8e1" stroke="#F57F17" stroke-width="1.5"/>
  <text x="637" y="245" text-anchor="middle" font-weight="bold" font-size="10" fill="#F57F17">Domain-Specific</text>
  <text x="637" y="260" text-anchor="middle" font-size="8">Biology: BioArc, AlphaFold3</text>
  <text x="637" y="275" text-anchor="middle" font-size="8">Materials: GNOME</text>
  <text x="637" y="290" text-anchor="middle" font-size="8">Science: Intern-S1 (241B)</text>

  <!-- Application domains -->
  <text x="375" y="330" text-anchor="middle" font-size="12" font-weight="bold" fill="#333">Application Domains</text>

  <rect x="30" y="345" width="130" height="55" rx="6" fill="#e8eaf6" stroke="#3F51B5" stroke-width="1"/>
  <text x="95" y="363" text-anchor="middle" font-weight="bold" font-size="9" fill="#283593">Drug Discovery</text>
  <text x="95" y="378" text-anchor="middle" font-size="8">LLM hypothesis →</text>
  <text x="95" y="390" text-anchor="middle" font-size="8">lab validation</text>

  <rect x="175" y="345" width="130" height="55" rx="6" fill="#e8eaf6" stroke="#3F51B5" stroke-width="1"/>
  <text x="240" y="363" text-anchor="middle" font-weight="bold" font-size="9" fill="#283593">Materials Science</text>
  <text x="240" y="378" text-anchor="middle" font-size="8">Property prediction</text>
  <text x="240" y="390" text-anchor="middle" font-size="8">+ synthesis planning</text>

  <rect x="320" y="345" width="130" height="55" rx="6" fill="#e8eaf6" stroke="#3F51B5" stroke-width="1"/>
  <text x="385" y="363" text-anchor="middle" font-weight="bold" font-size="9" fill="#283593">E-Commerce</text>
  <text x="385" y="378" text-anchor="middle" font-size="8">Product understanding</text>
  <text x="385" y="390" text-anchor="middle" font-size="8">+ recommendation</text>

  <rect x="465" y="345" width="130" height="55" rx="6" fill="#e8eaf6" stroke="#3F51B5" stroke-width="1"/>
  <text x="530" y="363" text-anchor="middle" font-weight="bold" font-size="9" fill="#283593">Education</text>
  <text x="530" y="378" text-anchor="middle" font-size="8">Personalized tutoring</text>
  <text x="530" y="390" text-anchor="middle" font-size="8">+ concept mapping</text>

  <rect x="610" y="345" width="115" height="55" rx="6" fill="#e8eaf6" stroke="#3F51B5" stroke-width="1"/>
  <text x="667" y="363" text-anchor="middle" font-weight="bold" font-size="9" fill="#283593">Simulation</text>
  <text x="667" y="378" text-anchor="middle" font-size="8">Predictive world</text>
  <text x="667" y="390" text-anchor="middle" font-size="8">models + planning</text>

  <!-- Footer -->
  <text x="375" y="435" text-anchor="middle" font-size="9" fill="#888">Increasing autonomy →</text>
  <line x1="100" y1="440" x2="650" y2="440" stroke="#ccc" stroke-width="1" stroke-dasharray="4"/>
  <text x="100" y="460" font-size="8" fill="#aaa">Human-in-the-loop</text>
  <text x="555" y="460" font-size="8" fill="#aaa">Autonomous discovery</text>
</svg>
```

## Hypothesis Generation and Lab Validation

A critical frontier for foundation models is generating scientifically valid, testable hypotheses — and having those hypotheses survive laboratory validation. This represents the strongest evidence that FMs can contribute to genuine discovery rather than just text generation.

### LLM-Generated Hypotheses in Biomedicine

Abdel-Rehim et al. (2025) conducted a landmark study where GPT-4 generated hypotheses about synergistic drug combinations for breast cancer treatment using FDA-approved non-cancer drugs. Of 12 LLM-proposed drug pairs, 3 showed synergy scores exceeding positive controls in laboratory assays — a 25% hit rate that compares favorably to traditional high-throughput screening[^19]. This study provides the first published evidence of LLM-generated hypotheses being validated in wet-lab experiments, establishing a new paradigm for AI-accelerated drug discovery.

### Hypothesis Generation Taxonomy

Alkan et al. (2025) provide a comprehensive taxonomy of LLM-based hypothesis generation methods, ranging from simple zero-shot prompting to complex multi-agent frameworks[^20]:

| Method | Approach | Strengths | Limitations |
|--------|----------|-----------|-------------|
| Zero-shot prompting | Direct hypothesis request | Simple, fast | Low novelty, generic |
| Chain-of-thought | Step-by-step reasoning | Better logical structure | May hallucinate reasoning steps |
| Retrieval-augmented | [RAG](retrieval-augmented-generation.md)-grounded generation | Factual grounding | Bounded by retrieval quality |
| Multi-agent debate | Multiple LLMs critique each other | Higher novelty, self-correction | Expensive, slow |
| Evolutionary search | Iterative hypothesis refinement | Explores hypothesis space | Requires fitness function |

The key insight for learning applications: these same methods can teach students how to formulate research questions — the AI's hypothesis generation process mirrors the structured thinking that researchers develop over years of practice.

### LLMs Across the Full Scientific Method

Zhang et al. (2025) published in *Nature npj AI* a comprehensive review of how LLMs are transforming every stage of the scientific method — from hypothesis generation through experimental design, data analysis, and discovery[^21]. They identify a critical gap: while LLMs excel at generating plausible hypotheses and writing papers, the experimental validation loop remains the weakest link. This motivates the integration of FMs with [predictive simulation](../frontier-topics/predictive-simulation-learning.md) to pre-validate hypotheses computationally before expensive lab work.

## Multi-Modal and Domain-Specific Scientific FMs

### Scientific Multi-Modal Models

A new class of foundation models is purpose-built for scientific reasoning across modalities. **Intern-S1** (Bai et al., 2025) is a Mixture-of-Experts model with 28B activated parameters (241B total), continually pre-trained on 5 trillion tokens including 2.5T+ scientific tokens[^22]. It achieves state-of-the-art on scientific reasoning benchmarks in both text-only and multi-modal settings, demonstrating that domain-specific pretraining data dramatically improves scientific capabilities.

Key architectural innovations in scientific FMs:
- **MoE routing** — Expert specialization allows different parameter subsets to handle chemistry vs. physics vs. biology
- **Scientific tokenization** — Custom tokenizers for mathematical notation, chemical formulae, and protein sequences
- **Multi-modal fusion** — Joint processing of text, figures, tables, and molecular structures

### Domain-Specific Architecture Search

Rather than adapting general-purpose architectures, **BioArc** (ICLR 2026) demonstrates that domain-specific neural architecture search produces biological foundation models that significantly outperform adapted Transformers[^23]. This challenges the "one architecture fits all" assumption and suggests that the next wave of scientific FMs will be architecturally specialized.

### Grounding FMs in World Models

**FOUNDER** (Wang et al., 2025) integrates foundation model knowledge with world model dynamics for embodied decision-making[^24]. The system learns a mapping that grounds FM representations in the world model's state space, enabling goal-conditioned policy learning through imagination — without reward signals. For research applications, this means FMs can "simulate" experimental outcomes by grounding their predictions in learned physical dynamics, connecting to [predictive simulation learning](../frontier-topics/predictive-simulation-learning.md) and [world models](../methodologies/world-models.md).

### Materials Discovery

Foundation models for materials science represent one of the most commercially impactful applications. Pyzer-Knapp et al. (2025) review how FMs are applied to property prediction, synthesis planning, and molecular generation[^25]. The integration of language models with physics-based simulation creates a feedback loop: FMs propose candidate materials → simulations predict properties → results refine FM predictions. This cycle exemplifies how foundation models learn from simulation outcomes for real-world application.

## Scaling Properties

Research quality correlates with model capability. Key observations from The AI Scientist:

- **Stronger models = better papers** -- Paper quality improves with each generation of foundation model
- **Reasoning models excel at idea generation** -- o3 outperforms non-reasoning models at hypothesis formation
- **Specialized models for specialized tasks** -- Using different models for different phases (reasoning for ideas, coding models for implementation, vision models for figures) outperforms using a single model
- **Capability density doubling** -- The "Densing Law" shows FM capability per parameter doubles every ~3.5 months, meaning research automation becomes more accessible over time[^15]

This suggests that as foundation models continue to improve, research automation quality will improve correspondingly. See [Scaling Laws for Research Automation](../frontier-topics/scaling-laws-research.md).

## Agentic Patterns

Foundation models alone are not sufficient -- they must be orchestrated using agentic patterns:

- **Few-shot prompting** -- Providing examples of desired output format
- **Self-reflection** -- Models critique and improve their own output
- **Tool use** -- Models call APIs, execute code, search the web
- **Memory** -- Experimental journals and note-taking for long-running research
- **Tree search** -- Exploring multiple experimental directions in parallel (see [Agentic Tree Search](../methodologies/agentic-tree-search.md))

## Current State / Latest Developments

As of early 2026, foundation models for research have seen several significant advances:

- **Reasoning models mature**: OpenAI's o3 and o4-mini models (2025) introduced extended chain-of-thought reasoning that dramatically improves hypothesis generation quality. The AI Scientist v2 uses o3 specifically for idea generation, finding it produces more novel and theoretically grounded proposals than non-reasoning models[^2][^7].

- **Claude model family expansion**: Anthropic's Claude Sonnet 4 and Opus 4 (2025) set new benchmarks for agentic coding tasks, making them the preferred choice for experiment implementation in automated research systems[^8]. Claude's 200K context window enables processing entire codebases and paper collections.

- **Open-source parity**: DeepSeek-R1 (2025) and Llama 3.3 demonstrated that open-source models can approach frontier performance on research tasks, reducing cost barriers for academic labs[^9]. This democratization is critical for ensuring AI research automation isn't limited to well-funded industry labs.

- **Multi-modal foundation models**: Google's Gemini 2.5 and Meta's V-JEPA 2 (2025) expand the modalities that foundation models can process, enabling research automation in vision-heavy domains like materials science and biology[^6].

- **AI for learning applications**: Foundation models are increasingly used as personalized tutoring engines. Systems like Khanmigo (Khan Academy + GPT-4) and Duolingo Max demonstrate that the same models powering research automation can accelerate human learning across subjects[^10]. The key insight is that models capable of generating research can also explain it — making complex topics accessible to learners at any level.

- **Rapid growth in scientific use**: A large-scale analysis by Chen et al. (2025) tracking FM usage across scientific publications found that foundation model adoption in science grew 340% between 2023-2025, with biology and materials science showing the fastest uptake after computer science[^16]. This validates the foundation model thesis: general-purpose models transfer effectively to specialized scientific domains.

- **FM for e-commerce research**: Foundation models are transforming [AI e-commerce learning](../frontier-topics/ai-ecommerce-learning.md) through multi-modal product understanding, personalized recommendation generation, and automated market analysis. A 2025 comprehensive review of recommender systems shows that FM-based approaches now dominate both retrieval and ranking stages of modern recommendation pipelines[^17].

- **Foundation models for temporal processes**: Bae et al. (2025) introduced foundation models specifically for temporal point processes — a key tool for modeling event sequences in scientific experiments, user behavior analysis, and clinical trial monitoring[^18].

- **5th paradigm of science**: Liu et al. (2025) argue that FMs are not merely enhancing existing scientific methodologies but catalyzing a transition toward a new "5th paradigm" of science — beyond empirical, theoretical, computational, and data-driven paradigms — where AI autonomously generates and tests hypotheses[^11].

- **Lab-validated LLM hypotheses**: The first published evidence of LLM-generated hypotheses validated in wet-lab experiments emerged in 2025, with GPT-4-proposed drug combinations showing synergy in breast cancer assays[^19]. This moves foundation models from "generating plausible text" to "generating actionable science."

- **Scientific MoE models**: Intern-S1, a 241B-parameter scientific MoE model trained on 2.5T+ scientific tokens, achieves SOTA on scientific reasoning benchmarks, demonstrating that domain-focused pretraining dramatically outperforms general-purpose models on scientific tasks[^22].

## Current Limitations

1. **Hallucination** -- Models confidently generate incorrect results, fake citations, and flawed reasoning
2. **Context window limits** -- Even 200K-token windows struggle with full codebases and paper collections
3. **Reliability** -- Non-deterministic outputs make reproducibility challenging
4. **Cost** -- Advanced reasoning models (o3) are expensive at scale
5. **Domain knowledge gaps** -- Models trained primarily on text struggle with specialized scientific domains
6. **Evaluation difficulty** -- Measuring whether a foundation model is "good enough" for research remains an open problem; benchmarks don't fully capture the nuanced skills needed for scientific discovery[^4]

## See Also

- [The AI Scientist](../core-concepts/the-ai-scientist.md)
- [Automated Scientific Discovery](../core-concepts/automated-scientific-discovery.md)
- [Automated Peer Review](../core-concepts/automated-peer-review.md)
- [Vision-Language Model Integration](../methodologies/vlm-integration.md)
- [Agentic Tree Search](../methodologies/agentic-tree-search.md)
- [Scaling Laws for Research Automation](../frontier-topics/scaling-laws-research.md)
- [Predictive Simulation Learning](../frontier-topics/predictive-simulation-learning.md)
- [Recursive Self-Improvement](../frontier-topics/recursive-self-improvement.md)
- [Key Papers and References](../research-sources/key-papers.md)
- [Tracking AI Research](../research-sources/tracking-ai-research.md)
- [AI E-Commerce Learning](../frontier-topics/ai-ecommerce-learning.md) — FM applications in e-commerce
- [Cross-Cutting Connections](../frontier-topics/cross-cutting-connections.md) — How FMs connect research domains
- [AIDE](../tools-platforms/aide.md) — FM as analyst in ML experimentation
- [Aider](../tools-platforms/aider.md) — FM as coding tool for research
- [HuggingFace Papers API](../tools-platforms/huggingface-papers-api.md) — Tracking FM research papers
- [Institutions and Labs](../research-sources/institutions-and-labs.md) — Labs developing foundation models

## References

[^1]: Bommasani, R. et al. (2021). "On the Opportunities and Risks of Foundation Models." [arXiv:2108.07258](https://arxiv.org/abs/2108.07258)
[^2]: Lu, C. et al. (2026). "Towards end-to-end automation of AI research." *Nature*, 651(8107). [doi:10.1038/s41586-025-08865-0](https://doi.org/10.1038/s41586-025-08865-0)
[^3]: Brown, T. et al. (2020). "Language Models are Few-Shot Learners." NeurIPS 2020. [arXiv:2005.14165](https://arxiv.org/abs/2005.14165)
[^4]: Wei, J. et al. (2022). "Emergent Abilities of Large Language Models." TMLR. [arXiv:2206.07682](https://arxiv.org/abs/2206.07682)
[^5]: Hoffmann, J. et al. (2022). "Training Compute-Optimal Large Language Models." NeurIPS 2022. [arXiv:2203.15556](https://arxiv.org/abs/2203.15556)
[^6]: Assran, M. et al. (2025). "V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning." [arXiv:2506.09985](https://arxiv.org/abs/2506.09985)
[^7]: Yamada, Y. et al. (2025). "AI Scientist v2: Workshop-Level Automated Scientific Discovery." [arXiv:2504.08066](https://arxiv.org/abs/2504.08066)
[^8]: Anthropic. (2025). "Claude Sonnet 4 Model Card." Anthropic.
[^9]: DeepSeek AI. (2025). "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning." [arXiv:2501.12948](https://arxiv.org/abs/2501.12948)
[^10]: Khan Academy. (2025). "Khanmigo: Scaling Personalized Tutoring with Foundation Models." Khan Academy Research.

[^11]: Liu, Z. et al. (2025). "Foundation Models for Scientific Discovery: From Paradigm Enhancement to Paradigm Transition." [arXiv:2510.15280](https://arxiv.org/abs/2510.15280)

[^12]: Jiang, Z. et al. (2025). "AIDE: AI-driven exploration in the space of code." [arXiv:2502.13138](https://arxiv.org/abs/2502.13138)

[^13]: Liang, X. et al. (2025). "From Automation to Autonomy: A Survey on Large Language Models in Scientific Discovery." [arXiv:2505.13259](https://arxiv.org/abs/2505.13259)

[^14]: Liu, Y. et al. (2026). "Grounding LLMs in Scientific Discovery via Embodied Actions." [arXiv:2602.20639](https://arxiv.org/abs/2602.20639)

[^15]: Li, C. et al. (2025). "Densing Law of LLMs." *Nature Machine Intelligence*. [doi:10.1038/s42256-025-01137-0](https://doi.org/10.1038/s42256-025-01137-0)

[^16]: Chen, X. et al. (2025). "The Rapid Growth of AI Foundation Model Usage in Science." [arXiv:2511.21739](https://arxiv.org/abs/2511.21739)

[^17]: He, Z. et al. (2024). "A Comprehensive Review of Recommender Systems: Transitioning from Theory to Practice." [arXiv:2407.13699](https://arxiv.org/abs/2407.13699)

[^18]: Bae, J. et al. (2025). "On Foundation Models for Temporal Point Processes to Accelerate Scientific Discovery." [arXiv:2510.12640](https://arxiv.org/abs/2510.12640)

[^19]: Abdel-Rehim, A. et al. (2025). "Scientific Hypothesis Generation by Large Language Models: Laboratory Validation in Breast Cancer Treatment." *Journal of The Royal Society Interface*, 22(227). [doi:10.1098/rsif.2024.0674](https://doi.org/10.1098/rsif.2024.0674)

[^20]: Alkan, A. K. et al. (2025). "A Survey on Hypothesis Generation for Scientific Discovery in the Era of Large Language Models." [arXiv:2504.05496](https://arxiv.org/abs/2504.05496)

[^21]: Zhang, Y. et al. (2025). "Exploring the Role of Large Language Models in the Scientific Method: From Hypothesis to Discovery." *npj Artificial Intelligence*, 1(1). [doi:10.1038/s44387-025-00019-5](https://doi.org/10.1038/s44387-025-00019-5)

[^22]: Bai, L. et al. (2025). "Intern-S1: A Scientific Multimodal Foundation Model." [arXiv:2508.15763](https://arxiv.org/abs/2508.15763)

[^23]: BioArc Authors. (2026). "BioArc: Discovering Optimal Neural Architectures for Biological Foundation Models." *ICLR 2026*. [arXiv:2512.00283](https://arxiv.org/abs/2512.00283)

[^24]: Wang, Y. et al. (2025). "FOUNDER: Grounding Foundation Models in World Models for Open-Ended Embodied Decision Making." [arXiv:2507.12496](https://arxiv.org/abs/2507.12496)

[^25]: Pyzer-Knapp, E. O. et al. (2025). "Foundation Models for Materials Discovery — Current State and Future Directions." *npj Computational Materials*. [doi:10.1038/s41524-025-01538-0](https://doi.org/10.1038/s41524-025-01538-0)
