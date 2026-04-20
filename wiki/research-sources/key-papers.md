---
title: Key Papers and References
type: concept
category: research-sources
tags: []
created: 2026-04-09
updated: 2026-04-20
sources: []
---

# Key Papers and References

## Overview

This article is a curated, annotated reading list of the most important papers for understanding AI research automation — from foundational theoretical work to cutting-edge systems. Papers are organized by topic to help readers build a structured understanding of how AI is transforming the research lifecycle. Each entry includes the paper's core contribution and practical relevance. This list complements [Tracking AI Research](tracking-ai-research.md), which covers *how* to discover new papers, while this article focuses on *which* papers matter most and why.

## Background / Theoretical Foundations

The field of AI research automation draws from three intellectual traditions, each represented by landmark papers in this collection:

1. **Philosophy of computational discovery** — Starting with Simon and Langley's work showing that scientific reasoning can be modeled as heuristic search, through to modern [foundation models](../core-concepts/foundation-models-for-research.md) that automate the full research cycle.[^1]
2. **Scaling and capability research** — The empirical study of how AI capabilities grow with compute, data, and parameters, establishing the predictive frameworks that underpin today's research automation systems.[^2]
3. **Agentic AI and self-improvement** — The emerging paradigm of AI systems that not only conduct research but improve their own research capabilities through [recursive self-improvement](../frontier-topics/recursive-self-improvement.md) and [agentic tree search](../methodologies/agentic-tree-search.md).[^3]

Understanding these traditions helps readers navigate the reading list strategically: foundational papers provide context, systems papers show current capabilities, and frontier papers point to where the field is heading.

## Foundational Papers

### End-to-End Research Automation
| Paper | Year | Core Contribution |
|-------|------|-------------------|
| **Lu et al. "Towards end-to-end automation of AI research"** | 2026 | First AI system to produce a peer-reviewed paper. Introduces The AI Scientist and Automated Reviewer. [Nature](https://doi.org/10.1038/s41586-026-10265-5) |
| **Jiang et al. "AIDE: AI-driven exploration in the space of code"** | 2025 | Treats program space as the search domain for ML experimentation. [arXiv:2502.13138](https://arxiv.org/abs/2502.13138) |
| **Huang et al. "MLAgentBench"** | 2024 | Benchmark for evaluating AI agents on ML experimentation tasks. [ICML 2024](https://arxiv.org/abs/2310.03302) |

### Foundation Models
| Paper | Year | Core Contribution |
|-------|------|-------------------|
| **Anthropic. "The Claude 3 Model Family"** | 2024 | Opus, Sonnet, Haiku model family used in AI Scientist |
| **Grattafiori et al. "The Llama 3 herd of models"** | 2024 | Open-source foundation models. [arXiv:2407.21783](https://arxiv.org/abs/2407.21783) |
| **OpenAI. "GPT-5 System Card"** | 2025 | Advances in reducing hallucination |
| **Bommasani et al. "On the Opportunities and Risks of Foundation Models"** | 2021 | Seminal analysis of foundation model landscape. [arXiv:2108.07258](https://arxiv.org/abs/2108.07258) |

### Open-Ended Discovery
| Paper | Year | Core Contribution |
|-------|------|-------------------|
| **Faldor et al. "OMNI-EPIC"** | 2025 | Open-endedness via models of human interestingness. [ICLR 2025](https://arxiv.org/abs/2405.15568) |
| **Lu, Hu & Clune. "Automated capability discovery"** | 2025 | AI discovering its own capabilities through self-exploration. [arXiv:2502.07577](https://arxiv.org/abs/2502.07577) |
| **Hu, Lu & Clune. "Automated design of agentic systems"** | 2025 | Meta-level: AI designing better AI agents. [ICLR 2025](https://arxiv.org/abs/2408.08435) |
| **Stanley & Lehman. *Why Greatness Cannot Be Planned*** | 2015 | The intellectual foundation for objective-free search |

### AI for Scientific Discovery
| Paper | Year | Core Contribution |
|-------|------|-------------------|
| **Jumper et al. "AlphaFold"** | 2021 | Protein structure prediction breakthrough. [Nature](https://doi.org/10.1038/s41586-021-03819-2) |
| **Merchant et al. "Scaling deep learning for materials discovery"** | 2023 | GNoME: 2.2M new stable materials. [Nature](https://doi.org/10.1038/s41586-023-06735-9) |
| **Szymanski et al. "Autonomous laboratory"** | 2023 | A-Lab: robotic synthesis of novel materials. [Nature](https://doi.org/10.1038/s41586-023-06734-w) |
| **Waltz & Buchanan. "Automating science"** | 2009 | Early vision for computational scientific discovery. [Science](https://doi.org/10.1126/science.1172781) |

### Agentic AI Patterns
| Paper | Year | Core Contribution |
|-------|------|-------------------|
| **Baek et al. "ResearchAgent"** | 2025 | Iterative idea generation over literature. [NAACL 2025](https://arxiv.org/abs/2404.07738) |
| **Wang et al. "AutoSurvey"** | 2024 | LLMs writing survey papers. [NeurIPS 2024](https://arxiv.org/abs/2306.10870) |

### Predictive Simulation and World Models
| Paper | Year | Core Contribution |
|-------|------|-------------------|
| **Zheng et al. "Can We Predict Before Executing Machine Learning Agents?"** | 2026 | ForeAgent: predict-then-verify loop achieving 6× convergence acceleration for ML agents. [arXiv:2601.05930](https://arxiv.org/abs/2601.05930) |
| **Richens et al. "General Agents Need World Models"** | 2025 | Formal proof that generalization requires world models. [arXiv:2506.01622](https://arxiv.org/abs/2506.01622) |
| **Hafner et al. "DreamerV3"** | 2025 | General world-model agent mastering 150+ tasks via imagination. [Nature](https://www.nature.com/articles/s41586-025-08744-2) |
| **Assran et al. "V-JEPA 2"** | 2025 | Video world models transferring to zero-shot robotic manipulation. [arXiv:2506.09985](https://arxiv.org/abs/2506.09985) |
| **Alonso et al. "DIAMOND"** | 2024 | Diffusion world models for RL, 46% above human on Atari. [arXiv:2405.12399](https://arxiv.org/abs/2405.12399) |
| **Guan et al. "Computer-Using World Model"** | 2026 | Predicting UI state changes for desktop software agents. [arXiv:2602.17365](https://arxiv.org/abs/2602.17365) |
| **Zhang et al. "World-in-World"** | 2025 | First closed-loop benchmark for world models. [arXiv:2510.18135](https://arxiv.org/abs/2510.18135) |
| **Yu et al. "Dyna-Think"** | 2025 | Framework integrating planning with internal world models alongside reasoning and acting. [arXiv:2506.00320](https://arxiv.org/abs/2506.00320) |
| **Yu et al. "Dyna-Mind"** | 2025 | Two-stage training teaching agents to simulate environments, with Dyna-GRPO for long-horizon planning. [arXiv:2510.09577](https://arxiv.org/abs/2510.09577) |
| **OpenWorldLib (DataFlow Team)** | 2026 | Unified definition and open codebase for world models research. [arXiv:2604.04707](https://arxiv.org/abs/2604.04707) |

### Recursive Self-Improvement
| Paper | Year | Core Contribution |
|-------|------|-------------------|
| **Zhang et al. "Darwin Godel Machine"** | 2025 | Self-improving coding agent via evolutionary self-rewriting. [arXiv:2505.22954](https://arxiv.org/abs/2505.22954) |
| **Zhang et al. "Hyperagents"** | 2026 | Meta-level self-improvement: improving the improvement process. [arXiv:2603.19461](https://arxiv.org/abs/2603.19461) |
| **Simonds & Yoshiyama. "LADDER"** | 2025 | Recursive problem decomposition for self-improving LLMs. [arXiv:2503.00735](https://arxiv.org/abs/2503.00735) |
| **Zhuang et al. "Test-time Recursive Thinking"** | 2026 | Self-improvement at inference time, 100% on AIME. [arXiv:2602.03094](https://arxiv.org/abs/2602.03094) |
| **Liu & van der Schaar. "Intrinsic Metacognitive Learning"** | 2025 | Position paper: true self-improvement needs metacognition. [arXiv:2506.05109](https://arxiv.org/abs/2506.05109) |
| **Ishibashi et al. "Self-Developing"** | 2025 | LLMs discovering their own improvement algorithms. [arXiv:2410.15639](https://arxiv.org/abs/2410.15639) |
| **Godel Agent** | 2025 | Self-referential framework enabling agents to recursively modify their own logic via LLMs. [arXiv:2410.04444](https://arxiv.org/abs/2410.04444) |
| **Singh et al. "Self-Improving AI through Self-Play"** | 2025 | Formalizes recursive self-improvement as Generator-Verifier-Updater operator. [arXiv:2512.02731](https://arxiv.org/abs/2512.02731) |
| **MARS "Learn Like Humans"** | 2026 | Meta-cognitive reflection for efficient self-improvement in a single recurrence cycle. [arXiv:2601.11974](https://arxiv.org/abs/2601.11974) |

### AI-Augmented Learning
| Paper | Year | Core Contribution |
|-------|------|-------------------|
| **Goel et al. "A4L: An Architecture for AI-Augmented Learning"** | 2025 | Data architecture for bidirectional feedback between learners, teachers, and AI agents. [arXiv:2505.06314](https://arxiv.org/abs/2505.06314) |
| **Wei et al. "Agentic-MME"** | 2026 | Process-verified benchmark for multimodal agentic capabilities with 2,000+ stepwise checkpoints. [arXiv:2604.03016](https://arxiv.org/abs/2604.03016) |

### AI for E-Commerce
| Paper | Year | Core Contribution |
|-------|------|-------------------|
| **Yu et al. "Shopping Companion"** | 2026 | Memory-augmented LLM agent for persistent shopping assistance. [arXiv:2603.14864](https://arxiv.org/abs/2603.14864) |
| **Allouah et al. "ACES"** | 2025 | Auditing AI shopping agent biases across frontier models. [arXiv:2508.02630](https://arxiv.org/abs/2508.02630) |
| **Wang et al. "ShoppingBench"** | 2025 | Real-world intent-grounded shopping benchmark, 2.5M+ products. [arXiv:2508.04266](https://arxiv.org/abs/2508.04266) |
| **Qi et al. "Supply Chain Planning Agent"** | 2025 | Production LLM agent at JD.com: 40% faster planning. [arXiv:2509.03811](https://arxiv.org/abs/2509.03811) |
| **Fang et al. "GenAI and Firm Productivity"** | 2025 | Field experiments: AI impact varies by e-commerce workflow. [arXiv:2510.12049](https://arxiv.org/abs/2510.12049) |
| **LREF "LLM-based Relevance Framework"** | 2025 | LLM-based search relevance with supervised fine-tuning and DPO de-biasing for e-commerce. [arXiv:2503.09223](https://arxiv.org/abs/2503.09223) |
| **ShopSimulator** | 2026 | Large-scale RL benchmark for LLM shopping agents; best models achieve <40% success. [arXiv:2601.18225](https://arxiv.org/abs/2601.18225) |
| **Xu et al. "AIGQ"** | 2026 | First end-to-end generative pre-search query recommender; deployed at Taobao with hybrid offline–online split, IL-GRPO with dual-level rewards, +10.31% orders / +10.68% GMV in production A/B. Full summary: [aigq-ecommerce-query-recommendation.md](aigq-ecommerce-query-recommendation.md). [arXiv:2603.19710](https://arxiv.org/abs/2603.19710) |
| **Hybrid CF-MF-RL Framework** | 2026 | Scalable hybrid combining collaborative filtering, matrix factorisation, and RL for unified recommendation + pricing + supply chain. [DOI: 10.1038/s41598-026-37437-7](https://www.nature.com/articles/s41598-026-37437-7) |
| **Greeven et al. "China AI Agents"** | 2026 | HBR analysis of delegation-first commerce via Meituan Xiaomei; AI as autonomous executor, not assistant. *Harvard Business Review*, April 2026. |

### World Models and Simulation
| Paper | Year | Core Contribution |
|-------|------|-------------------|
| **Zheng et al. "FOREAGENT"** | 2026 | Predict-then-verify loop for ML agents; 6× convergence acceleration, +6% over execution baselines. *ACL 2026*. [arXiv:2601.05930](https://arxiv.org/abs/2601.05930) |
| **Wang et al. "Agent World Model"** | 2026 | 1,000 synthetic environments with 35K tools for agentic RL; OOD generalization from purely synthetic training. [arXiv:2602.10090](https://arxiv.org/abs/2602.10090) |
| **Hafner et al. "Dreamer 4"** | 2025 | First agent to obtain Minecraft diamonds from offline video alone; real-time inference on single GPU. [arXiv:2509.24527](https://arxiv.org/abs/2509.24527) |
| **Li et al. "Simia"** | 2025 | LLMs simulate environments for agent training; fine-tuned open models exceed GPT-4o and approach o1-mini on τ²-Bench. [arXiv:2511.01824](https://arxiv.org/abs/2511.01824) |
| **Li et al. "SpatialEvo"** | 2026 | Self-evolving spatial reasoning via deterministic geometric environments; highest scores at 3B/7B scales across 9 benchmarks. [arXiv:2604.14144](https://arxiv.org/abs/2604.14144) |

### AI for Personalized Learning
| Paper | Year | Core Contribution |
|-------|------|-------------------|
| **Chen "AI-Driven Medical Learning"** | 2025 | RCT showing Cohen's d=0.72 improvement with AI personalization for medical students; strong equity effect for weak-baseline learners. [PMC12465117](https://pmc.ncbi.nlm.nih.gov/articles/PMC12465117/) |
| **Venkatraman et al. "RSA"** | 2025 | Recursive Self-Aggregation: 4B model matches DeepSeek-R1/o3-mini via iterative population refinement; near top of ARC-AGI-2 leaderboard. [arXiv:2509.26626](https://arxiv.org/abs/2509.26626) |
| **Ma et al. "SkillClaw"** | 2026 | Collective skill evolution across users via agentic evolver; cross-user discoveries propagate system-wide. [arXiv:2604.08377](https://arxiv.org/abs/2604.08377) |
| **Zhuang et al. "TRT"** | 2026 | Test-time Recursive Thinking: 100% AIME accuracy via self-improvement without external feedback. [arXiv:2602.03094](https://arxiv.org/abs/2602.03094) |

### AI Safety in Research
| Paper | Year | Core Contribution |
|-------|------|-------------------|
| **Korbak et al. "AI Researchers' Perspectives on Automating R&D"** | 2026 | 20/25 AI researchers identify automated R&D as most severe/urgent risk. [arXiv:2603.03338](https://arxiv.org/abs/2603.03338) |
| **International AI Safety Report** | 2026 | Comprehensive international report; 12 companies updated safety frameworks in 2025. [arXiv:2602.21012](https://arxiv.org/abs/2602.21012) |
| **AI Agent Index** | 2026 | Systematic safety feature documentation across deployed agent systems. [arXiv:2602.17753](https://arxiv.org/abs/2602.17753) |
| **ForesightSafety Bench** | 2026 | Governance and evaluation framework for frontier AI risks. [arXiv:2602.14135](https://arxiv.org/abs/2602.14135) |
| **Chen et al. "Agentic AI for Scientific Discovery"** | 2025 | Survey of LLM-driven agents for literature, experimentation, and reporting. [arXiv:2503.08979](https://arxiv.org/abs/2503.08979) |

### Independent Evaluations
| Paper | Year | Core Contribution |
|-------|------|-------------------|
| **Gabryel et al. "Evaluating Sakana's AI Scientist"** | 2025 | Critical assessment: "resembles a rushed undergraduate paper" but acknowledges real progress. [arXiv:2502.14297](https://arxiv.org/abs/2502.14297) |

### Scaling Laws
| Paper | Year | Core Contribution |
|-------|------|-------------------|
| **Kaplan et al. "Scaling Laws for Neural Language Models"** | 2020 | Power-law relationships between compute/data/params and performance. [arXiv:2001.08361](https://arxiv.org/abs/2001.08361) |
| **Hoffmann et al. "Chinchilla"** | 2022 | Compute-optimal training ratios. [arXiv:2203.15556](https://arxiv.org/abs/2203.15556) |
| **Kwa et al. "Measuring AI ability to complete long tasks"** | 2025 | Task complexity doubling every ~7 months. [METR Blog](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/) |

## How to Read This List

- **Start with** Lu et al. (2026) -- the Nature paper that ties everything together
- **For context**, read Waltz & Buchanan (2009) and Bommasani et al. (2021)
- **For tools**, read AIDE (Jiang et al.) and check [Autoresearch](../tools-platforms/autoresearch.md) on GitHub
- **For open-endedness**, start with Stanley & Lehman (2015), then OMNI-EPIC
- **For world models**, start with Richens et al. (2025) for theory, then DreamerV3 for practice, then ForeAgent for applied predict-then-verify
- **For AI-augmented learning**, start with A4L for architecture, then Agentic-MME for evaluation
- **For recursive self-improvement**, start with the Darwin Godel Machine, then Hyperagents
- **For e-commerce AI**, start with ACES for bias awareness, then Shopping Companion for agent design
- **For AI safety**, start with the International AI Safety Report for landscape, then AI Researchers' Perspectives for risk assessment
- **For critique**, read Gabryel et al. (2025) alongside the Nature paper

## See Also

- [Tracking AI Research](tracking-ai-research.md) -- How to discover new papers
- [Research Institutions and Labs](institutions-and-labs.md) -- Who is publishing what
- [The AI Scientist](../core-concepts/the-ai-scientist.md)
- [Automated Scientific Discovery](../core-concepts/automated-scientific-discovery.md)
- [Automated Peer Review](../core-concepts/automated-peer-review.md)
- [Agentic Tree Search](../methodologies/agentic-tree-search.md)
- [Template-Free Research](../methodologies/template-free-research.md)
- [VLM Integration](../methodologies/vlm-integration.md)
- [Automated Experiment Design](../methodologies/automated-experiment-design.md)
- [Predictive Simulation Learning](../frontier-topics/predictive-simulation-learning.md)
- [Recursive Self-Improvement](../frontier-topics/recursive-self-improvement.md)
- [AI for E-Commerce Learning](../frontier-topics/ai-ecommerce-learning.md)
- [HuggingFace Papers API](../tools-platforms/huggingface-papers-api.md)
- [Semantic Scholar API](../tools-platforms/semantic-scholar-api.md)

## Updating This List

This list should be updated as new landmark papers are published. Use the [HuggingFace Papers API](../tools-platforms/huggingface-papers-api.md) and [Semantic Scholar API](../tools-platforms/semantic-scholar-api.md) to discover candidates.

## References

[^1]: Langley, P., Simon, H.A., Bradshaw, G.L. & Zytkow, J.M. (1987). *Scientific Discovery: Computational Explorations of the Creative Process*. MIT Press.
[^2]: Kaplan, J. et al. (2020). "Scaling Laws for Neural Language Models." [arXiv:2001.08361](https://arxiv.org/abs/2001.08361)
[^3]: Zhang, J. et al. (2025). "Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents." [arXiv:2505.22954](https://arxiv.org/abs/2505.22954)
