# Research Institutions and Labs

## Overview

The landscape of AI research automation spans academic labs, industry research divisions, infrastructure providers, independent researchers, and safety organizations. This article catalogs the key players advancing automated scientific discovery, their focus areas, notable contributions, and the collaborative networks that connect them. Understanding who is building what — and why — is essential for navigating the rapidly evolving field of AI-driven research.[^1]

## Background / Historical Context

Institutional AI research has evolved through distinct phases. Early work (1960s–1990s) was concentrated in a handful of university labs — Stanford, MIT, Carnegie Mellon — focused on symbolic AI and expert systems.[^2] The deep learning revolution (2012–2020) shifted gravity toward industry labs (Google Brain, DeepMind, FAIR) with the compute resources to train large models. Since 2023, a new wave of organizations has emerged specifically targeting *research automation* — using AI not just as a tool but as an autonomous research agent. This includes startups like Sakana AI, university groups like UBC's Clune Lab, and infrastructure providers like Hugging Face that enable the broader ecosystem.[^3]

The trend toward open-source models (Llama, OLMo, Mistral) has democratized access, allowing smaller labs and independent researchers to participate in frontier research. Meanwhile, the rise of AI safety organizations reflects growing awareness that autonomous research systems require careful evaluation and governance.[^4]

## AI Research Automation Leaders

### Sakana AI
- **Location:** Tokyo, Japan
- **Focus:** Automated scientific discovery, open-ended AI, nature-inspired intelligence
- **Key Work:** [The AI Scientist](../core-concepts/the-ai-scientist.md) — first AI system to produce a peer-reviewed paper; pioneered both template-based and [template-free research](../methodologies/template-free-research.md) modes[^5]
- **People:** David Ha (CEO), Jeff Clune, Cong Lu, Chris Lu, Yutaro Yamada
- **Links:** [sakana.ai](https://sakana.ai/), [GitHub](https://github.com/SakanaAI)

### University of British Columbia (UBC) — Clune Lab
- **Location:** Vancouver, Canada
- **Focus:** Open-ended AI, automated design of AI systems, quality-diversity algorithms
- **Key Work:** OMNI-EPIC, Automated Design of Agentic Systems, [The AI Scientist](../core-concepts/the-ai-scientist.md), Darwin Gödel Machine[^6]
- **People:** Jeff Clune, Shengran Hu, Cong Lu, Jenny Zhang, Robert Lange
- **Notable:** The Darwin Gödel Machine (2025) demonstrated open-ended self-improving agents that boosted SWE-bench performance from 20.0% to 50.0% through autonomous self-modification[^6]

### University of Oxford — FLAIR
- **Location:** Oxford, UK
- **Focus:** Multi-agent systems, game theory, foundation model agents
- **Key Work:** AI Scientist (template-based mode), research automation, multi-agent coordination
- **People:** Jakob Foerster, Chris Lu

### Google DeepMind — AI for Science
- **Location:** London, UK / Mountain View, CA
- **Focus:** Scientific AI, protein folding, materials discovery, weather prediction
- **Key Work:** AlphaFold (protein structure prediction)[^7], GNoME (380,000 novel stable materials)[^8], GraphCast (weather forecasting), LearnLM (AI tutoring — 2 additional months of academic progress in RCT)[^9]
- **Education research:** Their LearnLM team conducted an RCT with 165 students across 5 UK schools demonstrating significant learning gains from AI tutoring[^9]
- **Links:** [deepmind.google](https://deepmind.google/)

## Foundation Model Providers

| Organization | Key Models | Relevance to Research Automation |
|-------------|-----------|--------------------------------|
| **Anthropic** | Claude 4 family | Claude Sonnet used for code generation in AI Scientist template-free mode; Claude Code for agentic development |
| **OpenAI** | GPT-4o, o3, o4-mini | o3 for idea generation, GPT-4o for [VLM tasks](../methodologies/vlm-integration.md), o4-mini for [automated review](../core-concepts/automated-peer-review.md) |
| **Meta AI (FAIR)** | Llama family, ESM | Open-source models enabling democratized research; ESM for protein language modeling |
| **Mistral AI** | Mistral, Mixtral | Open-weight models for European research ecosystem |
| **Google** | Gemini family | Multimodal capabilities for scientific document understanding |

## Research Infrastructure Providers

### Hugging Face
- **Focus:** Open ML platform, model/dataset hosting, community-driven research
- **Relevance:** [Papers API](../tools-platforms/huggingface-papers-api.md) for tracking new research, Hub for dataset access in [The AI Scientist](../core-concepts/the-ai-scientist.md), Spaces for interactive demos
- **Scale:** 500,000+ models, 100,000+ datasets hosted
- **Links:** [huggingface.co](https://huggingface.co/)

### Allen Institute for AI (AI2)
- **Focus:** Open research, NLP, scientific AI
- **Key Work:** [Semantic Scholar](../tools-platforms/semantic-scholar-api.md) (200M+ paper corpus), OLMo (fully open language models), S2ORC (open research corpus)
- **Links:** [allenai.org](https://allenai.org/)

### Papers With Code
- **Focus:** Linking papers to implementations and benchmarks
- **Relevance:** Essential for finding reproducible research; tracks state-of-the-art across 6,000+ benchmarks
- **Links:** [paperswithcode.com](https://paperswithcode.com/)

## Independent Researchers

### Andrej Karpathy
- **Affiliation:** Independent (formerly OpenAI, Tesla)
- **Key Work:** [Autoresearch](../tools-platforms/autoresearch.md) — autonomous ML experimentation framework
- **Impact:** Demonstrated that a single researcher with AI tools can match small team output
- **Links:** [karpathy.ai](https://karpathy.ai/), [GitHub](https://github.com/karpathy)

### Paul Gauthier
- **Key Work:** [Aider](../tools-platforms/aider.md) — AI coding assistant used in The AI Scientist
- **Impact:** Aider's edit-format and git integration became a reference implementation for AI-assisted coding in research pipelines
- **Links:** [GitHub](https://github.com/paul-gauthier/aider)

## Decentralized Science (DeSci)

| Organization | Focus | Status (2026) |
|-------------|-------|---------------|
| ResearchHub | Token-incentivized scientific discussion | Active, growing community |
| Molecule / VitaDAO | Decentralized drug discovery and longevity research | $4M+ in research funded |
| LabDAO | Decentralized laboratory services | Connecting wet labs globally |
| DeSci Labs | On-chain research publishing | dpub protocol in beta |

See [Blockchain for AI Optimization](../frontier-topics/blockchain-ai-optimization.md) for details on how blockchain intersects with AI research.

## AI Safety Organizations

| Organization | Focus | Relevance to Research Automation |
|-------------|-------|--------------------------------|
| METR | Measuring AI task completion capabilities | Evaluates autonomous research agent capabilities |
| Center for AI Safety (CAIS) | Research on catastrophic AI risks | Studies risks of [recursive self-improvement](../frontier-topics/recursive-self-improvement.md) |
| Alignment Research Center (ARC) | Evaluating advanced AI capabilities | Tests for deceptive alignment in research agents |
| UK AI Safety Institute | Government AI evaluation | Policy framework for autonomous research systems |
| Partnership on AI | Multi-stakeholder AI governance | Guidelines for responsible AI research automation |

See [AI Safety in Research](../frontier-topics/ai-safety-in-research.md) for a detailed analysis of safety considerations.

## Emerging Trends (2025–2026)

1. **Lab-startup convergence** — University researchers increasingly co-found startups (e.g., Sakana AI from UBC/Oxford alumni) while maintaining academic positions
2. **Open-source acceleration** — AI2's OLMo, Meta's Llama, and Mistral models enable smaller institutions to do frontier research
3. **Education integration** — DeepMind's LearnLM and platforms like Open TutorAI[^10] are bridging the gap between research and educational application
4. **Safety-capability co-development** — Organizations increasingly pair capability research with safety evaluation (e.g., METR evaluating AI Scientist)

## Limitations / Challenges

- **Geographic concentration** — Most leading AI labs remain in North America and Western Europe, with notable exceptions (Sakana AI in Tokyo)
- **Compute inequality** — Industry labs have 10–100× more compute than academic labs, creating a growing research divide[^4]
- **Talent competition** — Top researchers frequently move between academia and industry, disrupting long-term research programs
- **Reproducibility gaps** — Not all organizations share code and data, making independent verification difficult

## See Also

- [Key Papers and References](../research-sources/key-papers.md)
- [Tracking AI Research](../research-sources/tracking-ai-research.md)
- [The AI Scientist](../core-concepts/the-ai-scientist.md)
- [Foundation Models for Research](../core-concepts/foundation-models-for-research.md)
- [Automated Scientific Discovery](../core-concepts/automated-scientific-discovery.md)
- [Predictive Simulation Learning](../frontier-topics/predictive-simulation-learning.md)
- [Agentic Tree Search](../methodologies/agentic-tree-search.md)

## References

[^1]: Lu, C. et al. (2026). "Towards end-to-end automation of AI research." *Nature*, 651(8107).
[^2]: Langley, P., Simon, H.A., Bradshaw, G.L. & Zytkow, J.M. (1987). *Scientific Discovery: Computational Explorations of the Creative Process*. MIT Press.
[^3]: Merchant, A. et al. (2023). "Scaling deep learning for materials discovery." *Nature*, 624, 80–85.
[^4]: Besiroglu, T. et al. (2024). "The compute divide in machine learning: A threat to academic contribution." arXiv:2401.02452.
[^5]: Yamada, Y. et al. (2025). "AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery." *ICLR 2025*.
[^6]: Zhang, J., Hu, S., Lu, C., Lange, R. & Clune, J. (2025). "Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents." arXiv:2505.22954.
[^7]: Jumper, J. et al. (2021). "Highly accurate protein structure prediction with AlphaFold." *Nature*, 596, 583–589.
[^8]: Merchant, A. et al. (2023). "Scaling deep learning for materials discovery." *Nature*, 624, 80–85.
[^9]: Jurenka, I., Mohamed, S. et al. (2025). "AI tutoring can safely and effectively support students: An exploratory RCT in UK classrooms." arXiv:2512.23633.
[^10]: Open TutorAI contributors (2026). "Open TutorAI: An Open-source Platform for Personalized and Immersive Learning with Generative AI." arXiv:2602.07176.
