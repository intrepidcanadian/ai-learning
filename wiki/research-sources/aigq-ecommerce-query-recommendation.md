---
title: "AIGQ: End-to-End Hybrid Generative Query Recommendation (Xu et al. 2026)"
type: source-summary
category: research-sources
tags: [e-commerce, query-recommendation, llm-agents, grpo, hybrid-deployment, taobao]
created: 2026-04-09
updated: 2026-04-09
sources: [raw/2603.19710v1.pdf]
---

# AIGQ: An End-to-End Hybrid Generative Architecture for E-commerce Query Recommendation

**Citation:** Xu, J., Zou, J., Yang, R., Geng, Z., Liu, Q., & Tang, H. (2026). "AIGQ: An End-to-End Hybrid Generative Architecture for E-commerce Query Recommendation." Alibaba Taobao/Tmall + UESTC. [arXiv:2603.19710](https://arxiv.org/abs/2603.19710) (20 March 2026, 10pp).

**Source file:** [`raw/2603.19710v1.pdf`](../../raw/2603.19710v1.pdf)

## What it is

AIGQ is the first end-to-end generative framework for **pre-search query recommendation** in e-commerce — the suggestions a user sees on the homepage *before* they type anything. Deployed in production at Taobao/Tmall, it replaces an embedding-based retrieval (EBR) pipeline with two LLM variants that generate candidate queries directly from user state.

## Architecture

Two specialised LLM variants share a Qwen3-30B-A3B (MoE) base:

| Variant | Input | Output | Deployment |
|---------|-------|--------|------------|
| **AIGQ-Direct** | User profile + behaviour sequence | Personalised query list | **Online**, per-request |
| **AIGQ-Think** | Trigger query (e.g. last clicked item) | Query list with CoT rationale | **Offline**, cached |

The hybrid offline–online split is the most reusable methodology contribution: expensive reasoning (Think) runs in batch jobs and is keyed by trigger to a lookup table; the cheaper, latency-critical Direct model runs in the request path. This is a generalisable pattern for serving large LLMs under tight tail latency.

## Training: IL-SFT → IL-GRPO

Training is two-stage **Imitation Learning** from production logs:

1. **IL-SFT** — supervised fine-tuning on (user-state, query) pairs distilled from real Taobao impression/click logs. Establishes the surface form of good queries.
2. **IL-GRPO** — Group Relative Policy Optimization with **dual-level rewards**:
   - **Query-level** reward: aggregated CTR of the generated query when it appeared in production
   - **Token-level** reward: distributes credit to individual tokens of the query string, addressing the credit-assignment problem in short-output RL
   The reward model is **retrained daily** on fresh CTR data, keeping the policy aligned with shifting user intent.

## Headline numbers

**Offline:** Zero-shot frontier LLMs (no fine-tuning) already beat the production EBR baseline by **50%+** on relevance metrics — a striking signal that LLM world knowledge has already overtaken specialised retrieval models for query suggestion.

**Online A/B (Taobao production):**
- **+10.31% orders**
- **+10.68% GMV**
- **+3.73% LT-7** (7-day retention)

These are unusually large numbers for a mature production surface and suggest pre-search query suggestion was significantly under-served by traditional retrieval.

## Prompt compression

Because the Direct variant must run online at Taobao QPS, the team uses **special tokens for structured fields** in the prompt — single tokens stand in for fixed schema slots (user demographics, category history, time-of-day) instead of natural-language scaffolding. This is a concrete prompt-engineering technique for reducing token cost without hurting model comprehension when the prompt template is fixed.

## Why this paper matters for the wiki

It is the first **production-deployed** generative query recommender at hyperscale, and it reports several non-obvious findings the wiki should track:

1. Zero-shot LLMs beat embedding-based retrieval out of the box on a heavily-optimised surface — material for [LLM Persuasion in Commerce](../frontier-topics/e-commerce-applications.md) and the LLM-vs-pipeline narrative in [AI E-Commerce Learning](../frontier-topics/ai-ecommerce-learning.md).
2. **Hybrid offline–online deployment** is a reusable serving pattern for large LLMs under tight latency budgets — belongs in [Inference Optimization](../methodologies/inference-optimization.md), not just an e-commerce footnote.
3. **Dual-level rewards in GRPO** address short-output credit assignment, a generalisable RL technique relevant to [Recursive Self-Improvement](../frontier-topics/recursive-self-improvement.md) and any agent that emits short structured outputs.
4. **Prompt compression via special tokens** for fixed-schema prompts — a [Prompt Engineering](../methodologies/prompt-engineering.md) technique not previously covered.
5. Daily reward-model retraining is a concrete instance of the [continuous learning loop](../frontier-topics/ai-ecommerce-learning.md) the wiki claims is e-commerce's competitive advantage.

## Limitations and caveats

- Reported only on a single platform (Taobao) — generalisation to Western e-commerce surfaces is untested.
- The CTR-based reward optimises for clicks, not user satisfaction or long-term outcomes; the +3.73% LT-7 number is partial reassurance but not a full answer.
- No public release of model weights or training data.
- The IL-SFT training set is curated from production logs and inherits any popularity/exposure biases of the existing system — connecting to [LLM recommendation bias](../frontier-topics/e-commerce-applications.md).

## Pages updated by this ingest

- [AI E-Commerce Learning](../frontier-topics/ai-ecommerce-learning.md) — deepened the existing AIGQ section (it was a paragraph; now covers IL-SFT/IL-GRPO, hybrid deployment, A/B numbers)
- [Inference Optimization](../methodologies/inference-optimization.md) — added hybrid offline–online deployment as a serving pattern
- [Prompt Engineering](../methodologies/prompt-engineering.md) — added special-token prompt compression
- [Key Papers](key-papers.md) — added to the AI for E-Commerce reading list
- [Index](../../index.md) — new entry under Research Sources
- [Log](../../log.md) — ingest entry

## See Also

- [AI E-Commerce Learning](../frontier-topics/ai-ecommerce-learning.md)
- [E-Commerce Applications of AI Learning](../frontier-topics/e-commerce-applications.md)
- [Inference Optimization](../methodologies/inference-optimization.md)
- [Prompt Engineering](../methodologies/prompt-engineering.md)
- [Recursive Self-Improvement](../frontier-topics/recursive-self-improvement.md)
- [Key Papers](key-papers.md)
