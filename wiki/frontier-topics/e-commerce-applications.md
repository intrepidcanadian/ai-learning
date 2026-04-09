---
title: E-Commerce Applications of AI Learning
type: concept
category: frontier-topics
tags: []
created: 2026-04-09
updated: 2026-04-09
sources: []
---

# E-Commerce Applications of AI Learning

## Overview

**E-commerce applications of AI learning** encompass the rapidly evolving ecosystem of AI systems that learn to optimize online commerce — from product search and recommendation to dynamic pricing and conversational shopping agents. Unlike traditional rule-based e-commerce systems, modern AI-powered commerce platforms learn continuously from user behavior, market dynamics, and competitive signals. This article focuses on the practical systems and techniques that make AI-assisted e-commerce work, complementing the theoretical treatment in [AI e-commerce learning](ai-ecommerce-learning.md). For learners and professionals, understanding these applications is essential because e-commerce is the largest real-world laboratory for AI learning at scale: billions of daily interactions provide the fast feedback loops that drive rapid model improvement.

## Background / Theoretical Foundations

### The E-Commerce Learning Stack

AI learning in e-commerce operates at multiple levels, each with distinct learning dynamics:

| Layer | What the AI Learns | Learning Signal | Update Frequency |
|-------|-------------------|-----------------|------------------|
| **Product understanding** | What items are, how they relate | Catalog data, reviews, images | Daily-weekly |
| **User modeling** | Who the customer is, what they want | Click, cart, purchase history | Real-time |
| **Recommendation** | What to show next | Engagement, conversion rates | Minutes-hours |
| **Pricing** | Optimal price given demand/competition | Sales data, competitor prices | Hours-daily |
| **Conversation** | How to help via natural language | Chat logs, resolution rates | Weekly-monthly |

Each layer builds on the ones below — effective recommendations require good product understanding; conversational agents need both product knowledge and user models.

### From Collaborative Filtering to LLM-Powered Agents

The evolution of e-commerce AI spans three generations:

1. **Statistical era (2000-2015)**: Collaborative filtering, matrix factorization — "customers who bought X also bought Y"
2. **Deep learning era (2015-2023)**: Neural collaborative filtering, sequence models, graph neural networks — personalized ranking at scale
3. **LLM agent era (2024-present)**: Foundation model-powered shopping agents that understand intent, converse naturally, and reason about products — connecting to [foundation models for research](../core-concepts/foundation-models-for-research.md)

## Technical Details / Key Systems

### LLM-Based Recommendation Agents (2026)

Chauhan & Venkateswarlu (2026) benchmark LLM-based recommendation agents across GPT-4o-mini, DeepSeek-V3, Qwen2.5-72B, and Gemini 2.5 Flash, discovering a surprising finding: **recommendation quality remains consistent regardless of user history length** (5-50 items).[^1] This enables:

- **~88% cost reduction** by using shorter user histories without sacrificing quality
- **Cold-start mitigation**: Even 5 interactions provide sufficient signal for competitive recommendations
- **Real-time personalization**: Shorter context windows mean faster inference — connecting to [inference optimization](../methodologies/inference-optimization.md)

The implication for learning: e-commerce provides immediate feedback on AI model quality through measurable conversion metrics, making it an ideal domain for [active learning](../methodologies/active-learning.md) approaches.

### LREF: LLM-based Relevance for E-Commerce Search (2025)

LREF leverages LLM world knowledge and flexible reasoning to improve relevance scoring in industrial e-commerce search systems.[^2] Unlike traditional keyword-matching or embedding-based search, LREF:

- **Understands intent**: Distinguishes between "running shoes for marathon training" and "running shoes for casual wear"
- **Handles long-tail queries**: Reasons about obscure product attributes that sparse retrieval misses
- **Scales industrially**: Deployed in production search systems handling millions of daily queries

This connects to [retrieval-augmented generation](../core-concepts/retrieval-augmented-generation.md) — product search is a specialized form of retrieval where relevance depends on nuanced understanding of user intent.

### Multi-Agent Dynamic Pricing (2025)

Hazenberg et al. (2025) benchmark three multi-agent reinforcement learning (MARL) algorithms for dynamic pricing in competitive supply chains:[^3]

- **MADDPG** (Multi-Agent Deep Deterministic Policy Gradient): Best balance between competitive pricing and market fairness
- **MADQN** (Multi-Agent Deep Q-Network): Highest individual profit but risks market destabilization
- **QMIX**: Best cooperative pricing but unrealistic in truly competitive markets

Key finding: MADDPG achieves near-optimal pricing while maintaining market stability, suggesting that **cooperative-competitive hybrid strategies** outperform pure competition. This has direct implications for [multi-agent systems](multi-agent-systems.md) research — the pricing agents learn not just to optimize their own reward but to model competitors' strategies.

### Conversational Shopping Agents with Memory (2026)

Shopping Companion (Liu et al., 2026) introduces a **memory-augmented LLM agent** architecture for real-world e-commerce tasks.[^6] The system combines:

- **Persistent user memory**: Stores long-term preferences, past purchases, and stated constraints across sessions
- **Working memory**: Tracks the current shopping context (budget, occasion, style preferences) within a conversation
- **Tool use**: Integrates with product APIs, price comparison services, and review aggregators

Unlike stateless recommendation systems, Shopping Companion remembers that a user prefers organic products, has a nut allergy, and typically shops for a family of four — making each interaction more efficient than the last. This connects to [world models](../methodologies/world-models.md) — the agent builds an internal model of the user's preferences and constraints.

### LLM Persuasion in Commerce (2026)

A large-scale study (N=2,012) by researchers at Stanford and MIT reveals that **LLM-driven persuasion nearly triples sponsored product selection rates** compared to traditional search placement (61.2% vs. 22.4%).[^7] Key findings:

- LLM agents that conversationally recommend products are significantly more persuasive than banner ads or sponsored listings
- Users often cannot distinguish between genuine recommendations and sponsored content in conversational interfaces
- **Ethical implications**: The persuasion gap raises questions about disclosure requirements and consumer protection in AI-mediated commerce

This connects to [AI safety in research](ai-safety-in-research.md) — the same persuasion capabilities that make AI shopping assistants effective can be misused to manipulate purchasing decisions.

### Trust and Bias in LLM Recommendations (2026)

Wang et al. (2026) expose critical vulnerabilities in LLM-based recommendation agents: **models frequently succumb to injected biases despite having sufficient reasoning capabilities**.[^8] Testing across Gemini-2.5/3-pro, GPT-4o, and DeepSeek-R1:

- Position bias: Items listed first receive disproportionate recommendation regardless of quality
- Popularity bias: Well-known brands are favored even when lesser-known alternatives objectively fit better
- Injection attacks: Maliciously crafted product descriptions can manipulate recommendations
- **Mitigation**: Chain-of-thought reasoning reduces but does not eliminate these biases

This has implications for [prompt engineering](../methodologies/prompt-engineering.md) — designing prompts that make recommendation agents more robust to manipulation.

### ProductResearch: Deep Research Agents for Commerce (2026)

ProductResearch (2026) proposes a multi-agent framework for training e-commerce deep research agents via **synthetic trajectory distillation**.[^9] The system:

- Uses teacher agents to generate high-fidelity, long-horizon tool-use trajectories (search → compare → analyze → recommend)
- Distills these trajectories into smaller student agents that can independently research products
- Achieves comparable research quality to GPT-4-class models at 10× lower inference cost

This connects to [knowledge distillation](../core-concepts/knowledge-distillation.md) and [agentic tree search](../methodologies/agentic-tree-search.md) — the research agent explores a tree of product comparisons, and the distillation process compresses expert exploration into efficient policies.

### On-Device Recommendation (2026)

OD-LLM introduces the first compression framework for deploying LLM-based sequential recommendation on edge devices.[^4] The system:

- Compresses recommendation models from >7B to <500M parameters through knowledge distillation
- Enables real-time personalization on smartphones without network latency
- Preserves 94% of recommendation quality while reducing inference cost by 15×

This connects to [knowledge distillation](../core-concepts/knowledge-distillation.md) and [domain specificity](../methodologies/domain-specificity.md) — creating small, specialized recommendation models from large general ones.

### Explainable Recommendations via Knowledge Graphs (2024-2025)

LLM-powered Product Knowledge Graphs (PKG) provide transparent reasoning chains for recommendations.[^5] Instead of opaque "recommended for you" labels, PKG-based systems explain *why*:

- "This laptop is recommended because you prioritized battery life (>10 hours) and it scored highest among ultrabooks in your price range"
- Transparent reasoning enables **learning by shopping**: users develop better product evaluation skills through exposure to structured product reasoning

```svg
<svg viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="monospace" font-size="12">
  <text x="360" y="25" text-anchor="middle" font-size="15" font-weight="bold" fill="#1a1a2e">E-Commerce AI Learning Pipeline</text>

  <!-- Input signals -->
  <rect x="20" y="55" width="130" height="110" rx="8" fill="#E3F2FD" stroke="#1565C0" stroke-width="2"/>
  <text x="85" y="75" text-anchor="middle" font-size="11" font-weight="bold" fill="#1565C0">User Signals</text>
  <text x="85" y="95" text-anchor="middle" font-size="9">Clicks, views</text>
  <text x="85" y="109" text-anchor="middle" font-size="9">Purchases, returns</text>
  <text x="85" y="123" text-anchor="middle" font-size="9">Search queries</text>
  <text x="85" y="137" text-anchor="middle" font-size="9">Chat conversations</text>
  <text x="85" y="151" text-anchor="middle" font-size="9">Dwell time, scrolls</text>

  <!-- Arrow -->
  <line x1="155" y1="110" x2="190" y2="110" stroke="#333" stroke-width="1.5"/>
  <polygon points="188,105 198,110 188,115" fill="#333"/>

  <!-- LLM Agent -->
  <rect x="200" y="45" width="160" height="130" rx="10" fill="#E8F5E9" stroke="#2E7D32" stroke-width="2"/>
  <text x="280" y="68" text-anchor="middle" font-size="11" font-weight="bold" fill="#2E7D32">LLM Commerce Agent</text>
  <text x="280" y="88" text-anchor="middle" font-size="9">Intent understanding</text>
  <text x="280" y="102" text-anchor="middle" font-size="9">Product reasoning</text>
  <text x="280" y="116" text-anchor="middle" font-size="9">Price optimization</text>
  <text x="280" y="130" text-anchor="middle" font-size="9">Recommendation</text>
  <text x="280" y="150" text-anchor="middle" font-size="8" fill="#2E7D32">5-item history = 50-item [1]</text>
  <text x="280" y="162" text-anchor="middle" font-size="8" fill="#2E7D32">88% cost reduction</text>

  <!-- Arrow -->
  <line x1="365" y1="110" x2="400" y2="110" stroke="#333" stroke-width="1.5"/>
  <polygon points="398,105 408,110 398,115" fill="#333"/>

  <!-- Actions -->
  <rect x="410" y="45" width="145" height="130" rx="10" fill="#FFF3E0" stroke="#FF9800" stroke-width="2"/>
  <text x="482" y="68" text-anchor="middle" font-size="11" font-weight="bold" fill="#E65100">Actions</text>
  <text x="482" y="88" text-anchor="middle" font-size="9">Personalized search</text>
  <text x="482" y="102" text-anchor="middle" font-size="9">Product recommendations</text>
  <text x="482" y="116" text-anchor="middle" font-size="9">Dynamic pricing</text>
  <text x="482" y="130" text-anchor="middle" font-size="9">Conversational help</text>
  <text x="482" y="150" text-anchor="middle" font-size="8" fill="#E65100">Explainable reasoning [5]</text>
  <text x="482" y="162" text-anchor="middle" font-size="8" fill="#E65100">via knowledge graphs</text>

  <!-- Arrow -->
  <line x1="560" y1="110" x2="595" y2="110" stroke="#333" stroke-width="1.5"/>
  <polygon points="593,105 603,110 593,115" fill="#333"/>

  <!-- Outcomes -->
  <rect x="605" y="55" width="100" height="110" rx="8" fill="#F3E5F5" stroke="#7B1FA2" stroke-width="2"/>
  <text x="655" y="75" text-anchor="middle" font-size="11" font-weight="bold" fill="#7B1FA2">Outcomes</text>
  <text x="655" y="95" text-anchor="middle" font-size="9">Conversion</text>
  <text x="655" y="109" text-anchor="middle" font-size="9">Satisfaction</text>
  <text x="655" y="123" text-anchor="middle" font-size="9">Retention</text>
  <text x="655" y="137" text-anchor="middle" font-size="9">Revenue</text>
  <text x="655" y="151" text-anchor="middle" font-size="9">Learning</text>

  <!-- Feedback loop -->
  <path d="M 655 170 L 655 195 L 85 195 L 85 170" stroke="#7B1FA2" stroke-width="2" fill="none" stroke-dasharray="5,5"/>
  <polygon points="80,172 85,162 90,172" fill="#7B1FA2"/>
  <text x="370" y="210" text-anchor="middle" font-size="9" fill="#7B1FA2">Continuous learning loop - every interaction updates user and product models</text>

  <!-- Three application domains -->
  <rect x="20" y="230" width="220" height="80" rx="8" fill="#E0F7FA" stroke="#00838F" stroke-width="1.5"/>
  <text x="130" y="250" text-anchor="middle" font-size="10" font-weight="bold" fill="#00838F">Search + Discovery</text>
  <text x="130" y="268" text-anchor="middle" font-size="9">LREF: LLM-powered relevance [2]</text>
  <text x="130" y="282" text-anchor="middle" font-size="9">Intent understanding beyond</text>
  <text x="130" y="296" text-anchor="middle" font-size="9">keyword matching</text>

  <rect x="250" y="230" width="220" height="80" rx="8" fill="#FFF8E1" stroke="#F57F17" stroke-width="1.5"/>
  <text x="360" y="250" text-anchor="middle" font-size="10" font-weight="bold" fill="#F57F17">Dynamic Pricing</text>
  <text x="360" y="268" text-anchor="middle" font-size="9">MARL: multi-agent pricing [3]</text>
  <text x="360" y="282" text-anchor="middle" font-size="9">MADDPG: competitive yet</text>
  <text x="360" y="296" text-anchor="middle" font-size="9">fair market equilibrium</text>

  <rect x="480" y="230" width="220" height="80" rx="8" fill="#FCE4EC" stroke="#C62828" stroke-width="1.5"/>
  <text x="590" y="250" text-anchor="middle" font-size="10" font-weight="bold" fill="#C62828">On-Device Personalization</text>
  <text x="590" y="268" text-anchor="middle" font-size="9">OD-LLM: compressed models [4]</text>
  <text x="590" y="282" text-anchor="middle" font-size="9">94% quality at 15x lower</text>
  <text x="590" y="296" text-anchor="middle" font-size="9">inference cost</text>

  <!-- Learning connection -->
  <rect x="20" y="325" width="680" height="60" rx="8" fill="#EDE7F6" stroke="#4527A0" stroke-width="1.5"/>
  <text x="360" y="347" text-anchor="middle" font-size="12" font-weight="bold" fill="#4527A0">Why E-Commerce Is the Best AI Learning Laboratory</text>
  <text x="360" y="367" text-anchor="middle" font-size="10">Billions of daily interactions + immediate purchase feedback + clear reward signal</text>
  <text x="360" y="381" text-anchor="middle" font-size="10">= fastest learning loop in any AI application domain</text>
</svg>
```

## Current State / Latest Developments

### 2026 Landscape

1. **LLM agents replace pipelines**: Traditional e-commerce ML pipelines (feature engineering → model training → A/B testing) are being replaced by end-to-end LLM agents that understand, reason, and converse[^1]
2. **History length doesn't matter**: The surprising finding that 5-item histories match 50-item histories for LLM recommendations challenges the "more data is better" assumption[^1]
3. **Memory-augmented shopping**: Agents with persistent memory across sessions deliver increasingly personalized assistance, remembering user constraints and preferences[^6]
4. **Persuasion power raises ethics concerns**: LLM conversational recommendations are 2.7× more effective than traditional ad placement, prompting calls for disclosure regulation[^7]
5. **Trust vulnerabilities exposed**: LLM recommendation agents are susceptible to position bias, popularity bias, and injection attacks — an active area of safety research[^8]
6. **Deep research agents**: Multi-agent distillation produces specialized product research agents that match GPT-4-class quality at 10× lower cost[^9]
7. **On-device deployment is viable**: Compressed recommendation models run on edge devices, enabling privacy-preserving real-time personalization[^4]
8. **Multi-agent pricing reaches equilibrium**: MARL algorithms find competitive yet fair pricing strategies, moving beyond simple demand-response curves[^3]
9. **Explainability is a competitive advantage**: PKG-based recommendation reasoning helps users make better decisions and builds trust[^5]
10. **Search understands intent**: LLM-powered relevance models handle nuanced, long-tail queries that keyword systems miss[^2]

### Key Metrics

| System | Year | Key Result |
|--------|------|-----------|
| LLM Recommendation Agents | 2026 | 88% cost reduction with consistent quality[^1] |
| Shopping Companion | 2026 | Memory-augmented agent for persistent personalization[^6] |
| LLM Persuasion Study | 2026 | 61.2% vs 22.4% sponsored product selection[^7] |
| LLM Bias Analysis | 2026 | Position/popularity/injection vulnerabilities[^8] |
| ProductResearch | 2026 | 10× cheaper deep research agents via distillation[^9] |
| LREF Search | 2025 | Industrial-scale LLM relevance scoring[^2] |
| MARL Dynamic Pricing | 2025 | MADDPG achieves competitive fairness[^3] |
| OD-LLM | 2026 | 94% quality at 15x lower cost on-device[^4] |
| Product Knowledge Graph | 2024 | Explainable recommendation chains[^5] |

## Limitations / Challenges

```svg
<svg viewBox="0 0 720 320" xmlns="http://www.w3.org/2000/svg" font-family="monospace" font-size="12">
  <text x="360" y="25" text-anchor="middle" font-size="15" font-weight="bold" fill="#1a1a2e">Trust &amp; Safety in AI Commerce (2026)</text>

  <!-- Bias types -->
  <rect x="20" y="50" width="160" height="100" rx="8" fill="#FFEBEE" stroke="#C62828" stroke-width="2"/>
  <text x="100" y="70" text-anchor="middle" font-size="11" font-weight="bold" fill="#C62828">Position Bias</text>
  <text x="100" y="90" text-anchor="middle" font-size="9">First-listed items get</text>
  <text x="100" y="104" text-anchor="middle" font-size="9">disproportionate</text>
  <text x="100" y="118" text-anchor="middle" font-size="9">recommendation [8]</text>
  <text x="100" y="140" text-anchor="middle" font-size="8" fill="#C62828">All tested LLMs affected</text>

  <rect x="200" y="50" width="160" height="100" rx="8" fill="#FFF3E0" stroke="#E65100" stroke-width="2"/>
  <text x="280" y="70" text-anchor="middle" font-size="11" font-weight="bold" fill="#E65100">Popularity Bias</text>
  <text x="280" y="90" text-anchor="middle" font-size="9">Known brands favored</text>
  <text x="280" y="104" text-anchor="middle" font-size="9">over better-fitting</text>
  <text x="280" y="118" text-anchor="middle" font-size="9">alternatives [8]</text>
  <text x="280" y="140" text-anchor="middle" font-size="8" fill="#E65100">Reinforces monopolies</text>

  <rect x="380" y="50" width="160" height="100" rx="8" fill="#FCE4EC" stroke="#AD1457" stroke-width="2"/>
  <text x="460" y="70" text-anchor="middle" font-size="11" font-weight="bold" fill="#AD1457">Injection Attacks</text>
  <text x="460" y="90" text-anchor="middle" font-size="9">Malicious product</text>
  <text x="460" y="104" text-anchor="middle" font-size="9">descriptions manipulate</text>
  <text x="460" y="118" text-anchor="middle" font-size="9">recommendations [8]</text>
  <text x="460" y="140" text-anchor="middle" font-size="8" fill="#AD1457">Security vulnerability</text>

  <rect x="560" y="50" width="140" height="100" rx="8" fill="#E8EAF6" stroke="#283593" stroke-width="2"/>
  <text x="630" y="70" text-anchor="middle" font-size="11" font-weight="bold" fill="#283593">Persuasion Gap</text>
  <text x="630" y="90" text-anchor="middle" font-size="9">LLM recommendations</text>
  <text x="630" y="104" text-anchor="middle" font-size="9">2.7x more effective</text>
  <text x="630" y="118" text-anchor="middle" font-size="9">than ads [7]</text>
  <text x="630" y="140" text-anchor="middle" font-size="8" fill="#283593">Ethics concern</text>

  <!-- Mitigation -->
  <rect x="20" y="175" width="680" height="55" rx="8" fill="#E8F5E9" stroke="#2E7D32" stroke-width="2"/>
  <text x="360" y="195" text-anchor="middle" font-size="12" font-weight="bold" fill="#2E7D32">Mitigations: Chain-of-Thought Reasoning + Memory-Augmented Agents [6] + Disclosure Requirements</text>
  <text x="360" y="215" text-anchor="middle" font-size="10">CoT reduces but does not eliminate bias | Persistent memory enables preference verification | Regulation needed</text>

  <!-- Learning takeaway -->
  <rect x="100" y="250" width="520" height="55" rx="8" fill="#EDE7F6" stroke="#4527A0" stroke-width="1.5"/>
  <text x="360" y="272" text-anchor="middle" font-size="12" font-weight="bold" fill="#4527A0">Learning Application: Critical AI Literacy</text>
  <text x="360" y="292" text-anchor="middle" font-size="10">Understanding these biases helps consumers evaluate AI recommendations critically</text>
</svg>
```

1. **Optimization misalignment**: AI systems optimize for conversion (purchases) rather than user satisfaction — a product that converts well may not serve the user well
2. **Cold-start for new products**: While user cold-start is improving, new product cold-start (no reviews, no purchase history) remains difficult
3. **Market manipulation risk**: Multi-agent pricing systems could inadvertently collude, raising antitrust concerns
4. **Bias amplification**: Recommendation systems can create filter bubbles and reinforce existing inequalities in product exposure
5. **Evaluation complexity**: Offline metrics (precision, recall) often don't predict online performance (revenue, satisfaction) — connecting to [evaluation methodology](../methodologies/evaluation-methodology.md)
6. **Privacy vs. personalization**: Better recommendations require more data, creating tension with privacy regulations (GDPR, CCPA)

## See Also / Connections

**Core Concepts:**
- [Foundation Models for Research](../core-concepts/foundation-models-for-research.md) — base models powering commerce AI
- [Retrieval-Augmented Generation](../core-concepts/retrieval-augmented-generation.md) — product search as specialized retrieval
- [Knowledge Distillation](../core-concepts/knowledge-distillation.md) — compressing models for on-device deployment
- [Transfer Learning](../core-concepts/transfer-learning.md) — cross-market knowledge transfer

**Tools & Platforms:**
- [HuggingFace Papers API](../tools-platforms/huggingface-papers-api.md) — tracking e-commerce AI research
- [Semantic Scholar API](../tools-platforms/semantic-scholar-api.md) — academic e-commerce literature

**Methodologies:**
- [Active Learning](../methodologies/active-learning.md) — efficient user preference learning
- [Inference Optimization](../methodologies/inference-optimization.md) — real-time recommendation serving
- [Domain Specificity](../methodologies/domain-specificity.md) — e-commerce as a specialized domain
- [Evaluation Methodology](../methodologies/evaluation-methodology.md) — offline vs. online metrics
- [Prompt Engineering](../methodologies/prompt-engineering.md) — designing bias-resistant recommendation prompts
- [World Models](../methodologies/world-models.md) — user preference modeling in shopping agents
- [Agentic Tree Search](../methodologies/agentic-tree-search.md) — product research as tree exploration
- [Synthetic Data Generation](../methodologies/synthetic-data-generation.md) — generating training data for commerce models

**Frontier Topics:**
- [AI E-Commerce Learning](ai-ecommerce-learning.md) — theoretical framework for commerce AI
- [Multi-Agent Systems](multi-agent-systems.md) — competitive pricing and collaborative commerce agents
- [Predictive Simulation Learning](predictive-simulation-learning.md) — simulating market dynamics
- [Recursive Self-Improvement](recursive-self-improvement.md) — self-improving recommendation systems
- [Cross-Cutting Connections](cross-cutting-connections.md) — commerce in the simulation-recursion-commerce triad

**Research Sources:**
- [Key Papers](../research-sources/key-papers.md) — foundational recommendation system papers
- [Institutions and Labs](../research-sources/institutions-and-labs.md) — e-commerce AI research groups

## References

[^1]: Chauhan, K. & Venkateswarlu, M. (2026). "Less is More: Benchmarking LLM Based Recommendation Agents." arXiv:2601.20316. https://arxiv.org/abs/2601.20316

[^2]: Anonymous. (2025). "LREF: A Novel LLM-based Relevance Framework for E-Commerce Search." arXiv:2503.09223. https://arxiv.org/abs/2503.09223

[^3]: Hazenberg, T., Ma, Y., Mohammadi Ziabari, S. S., & van Rijswijk, M. (2025). "Multi-Agent Reinforcement Learning for Dynamic Pricing in Supply Chains." arXiv:2507.02698. https://arxiv.org/abs/2507.02698

[^4]: Anonymous. (2026). "On-Device Large Language Models for Sequential Recommendation." arXiv:2601.09306. https://arxiv.org/abs/2601.09306

[^5]: Anonymous. (2024). "Enabling Explainable Recommendation in E-commerce with LLM-powered Product Knowledge Graph." arXiv:2412.01837. https://arxiv.org/abs/2412.01837

[^6]: Liu, Y. et al. (2026). "Shopping Companion: A Memory-Augmented LLM Agent for Real-World E-Commerce Tasks." arXiv:2603.14864. https://arxiv.org/abs/2603.14864

[^7]: Anonymous. (2026). "Commercial Persuasion in AI-Mediated Conversations." arXiv:2604.04263. https://arxiv.org/abs/2604.04263

[^8]: Wang, Z. et al. (2026). "Is Your LLM-as-a-Recommender Agent Trustable? LLMs' Recommendation is Easily Hacked by Biases." arXiv:2603.17417. https://arxiv.org/abs/2603.17417

[^9]: Anonymous. (2026). "ProductResearch: Training E-Commerce Deep Research Agents via Multi-Agent Synthetic Trajectory Distillation." arXiv:2602.23716. https://arxiv.org/abs/2602.23716
