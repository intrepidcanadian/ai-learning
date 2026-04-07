# Wiki Quality Benchmarking

## Overview

This wiki uses an automated benchmarking system to measure and improve article quality over time. Every article is scored across seven dimensions by [`benchmark_wiki.py`](../benchmark_wiki.py), producing a composite quality score out of 100. The scores drive an experiment-based improvement loop: each edit is a hypothesis tested against the benchmark, and the results inform future edits.

The core idea is borrowed from the wiki's own subject matter — **recursive self-improvement** applied to the knowledge base itself. The benchmark acts as the verifier, the editing agent proposes improvements, and the experiment log captures what works.

## Background / Theoretical Foundations

Automated quality assessment of knowledge bases draws on several established research traditions:

**Wikipedia quality assessment.** Wikipedia's own quality grading system (Stub → Start → C → B → GA → FA) has been studied extensively as a machine learning problem. Warncke-Wang et al. (2015) showed that structural features (section count, citation density, link density) predict article quality class with ~80% accuracy [^4]. This wiki's benchmark follows the same principle: measuring quality through observable structural and sourcing features rather than semantic evaluation.

**Automated scientific review.** The [Automated Peer Review](../core-concepts/automated-peer-review.md) literature demonstrates that LLMs can evaluate research quality along specific dimensions (novelty, correctness, significance). This wiki's benchmark is a simplified analog — evaluating articles along dimensions like sourcing, currency, and structural completeness without requiring an LLM in the loop [^5].

**Continuous integration for documentation.** The DevOps practice of continuous integration — automated testing on every code change — extends naturally to documentation. Tools like Vale (prose linting), markdownlint, and link checkers automate quality checks for technical writing [^6]. This wiki's benchmark applies the same philosophy: every edit triggers a quality re-evaluation, and the scores drive the next improvement.

**Self-improving systems.** The benchmark loop is a concrete instance of the [Recursive Self-Improvement](../frontier-topics/recursive-self-improvement.md) pattern: a system that uses its own output (scores) to guide its own improvement (edits). The experiment log adds a meta-learning layer, allowing the improvement process itself to improve over time based on which strategies produce the largest score gains.

**Practical application for learning.** For anyone building a knowledge base — whether for personal study, team onboarding, or course material — this benchmarking approach provides a template. By defining measurable quality dimensions and automating their evaluation, you create a feedback loop that systematically improves the resource over time. The key insight is that *measurability drives improvement*: dimensions you track will improve faster than dimensions you don't.

## How Scoring Works

Each article is evaluated on seven dimensions, weighted by importance:

| Dimension | Weight | What It Measures |
|-----------|--------|-----------------|
| **Structural Completeness** | 15% | Does the article follow the [template](../README.md)? Checks for Overview, Background, Technical Details, Current State, Challenges, See Also, and References sections. |
| **Depth** | 15% | Substantive content — subsection count, rich content (code blocks, blockquotes, tables), learning application annotations, diagrams. |
| **Currency** | 15% | Recency of references. Rewards 2025-2026 citations, penalizes articles with only older sources. |
| **Sourcing** | 20% | Are claims backed by footnoted references? Measures footnote density, arxiv/doi links, and flags orphaned footnotes. |
| **Internal Linking** | 10% | Cross-references to sibling articles and articles in other categories. Each article should link to related articles across the wiki. |
| **Consistency** | 15% | Formatting hygiene — duplicate headers, numbering gaps (especially in Cross-Cutting Connections), broken internal links. |
| **Freshness** | 10% | How recently the article file was modified. Rewards articles updated within the past week. |

The composite score is a weighted sum of all seven dimensions.

### Article Tiers

Not all articles are held to the same standard:

- **Flagship** (frontier-topics articles >500 lines): Full quality expectations across all dimensions. These are the deep-dive articles on predictive simulation, recursive self-improvement, e-commerce learning, and cross-cutting connections.
- **Standard** (100-500 lines): Moderate expectations. At least 4 template sections required.
- **Reference** (<100 lines): Navigation hubs and API guides. Emphasis on linking and consistency over depth.

### Score Interpretation

| Score Range | Meaning |
|-------------|---------|
| 90-100 | Excellent — well-sourced, complete, current, well-linked |
| 75-89 | Good — minor gaps in structure or sourcing |
| 60-74 | Needs work — missing sections, weak sourcing, or broken links |
| Below 60 | Stub or seriously incomplete — priority for expansion |

## The Improvement Loop

The benchmark drives an iterative improvement process:

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│   ┌──────────┐    ┌────────────┐    ┌───────────┐  │
│   │ Benchmark │───►│ Hypothesize│───►│   Edit    │  │
│   │  (score)  │    │ (predict)  │    │ (article) │  │
│   └──────────┘    └────────────┘    └─────┬─────┘  │
│        ▲                                  │         │
│        │          ┌────────────┐          │         │
│        └──────────│ Re-score + │◄─────────┘         │
│                   │   Log      │                    │
│                   └────────────┘                    │
│                                                     │
└─────────────────────────────────────────────────────┘
```

Each iteration:

1. **Benchmark** — `python3 benchmark_wiki.py` scores all articles, identifies the lowest-scoring one, and lists specific issues.
2. **Hypothesize** — before editing, the agent writes a prediction: what strategy to use, which dimensions it targets, and the expected score improvement.
3. **Edit** — the agent modifies the article following the hypothesis.
4. **Re-score and log** — the benchmark runs again. The actual score delta is compared to the prediction and logged to `data/experiments/`.

### Experiment-Driven Learning

Past experiments are fed into future iterations. Over time the loop learns:

- Which strategies produce the largest score gains (e.g., adding missing template sections vs. adding footnotes)
- Which dimensions are hardest to improve
- When diminishing returns set in for a particular article

Experiment logs are stored as JSON in `data/experiments/` with this structure:

```json
{
  "timestamp": "2026-04-07_184500",
  "iteration": 3,
  "article": "cross-cutting-connections",
  "hypothesis": {
    "strategy": "Add Overview section and fix duplicate connection numbers",
    "predicted_delta": 5.0,
    "dimensions_targeted": ["structural", "consistency"],
    "reasoning": "Past experiments show structural fixes yield +3-5 points"
  },
  "result": {
    "score_before": 80.9,
    "score_after": 87.2,
    "actual_delta": 6.3,
    "improved": true,
    "lesson": "Structural fixes on flagship articles exceed predictions"
  }
}
```

## Score Trend

The benchmark tracks scores over time, saved as timestamped JSON files in `data/benchmarks/`. The [Quality Benchmark](../research-sources/benchmark-trend.md) page on the wiki displays:

- **Current scores** — per-article bar chart and dimension breakdown
- **Trend sparklines** — how each article's score has changed across runs
- **Run history table** — every benchmark run with per-article composites
- **Open issues** — the specific problems flagged by the latest run

This page is auto-regenerated every time `benchmark_wiki.py` runs.

## Running the Benchmark

```bash
python3 benchmark_wiki.py            # Score all articles, save results, update trend page
python3 benchmark_wiki.py --diff     # Compare the last two benchmark runs
python3 benchmark_wiki.py --history  # Show composite score over all runs
```

The automated improvement loop runs via:

```bash
./improve_loop.sh          # 3 iterations (default)
./improve_loop.sh 5        # 5 iterations
./improve_loop.sh 1        # single pass
```

## Current State / Latest Developments

As of 2026, automated quality assessment of knowledge resources is a rapidly evolving field:

- **LLM-as-judge paradigm (2025-2026)**: The dominant approach to automated evaluation now uses LLMs as evaluators. Zheng et al. (2025) showed that GPT-4-based judges achieve >85% agreement with human annotators on document quality, suggesting that future versions of this benchmark could incorporate semantic evaluation alongside structural metrics[^7]. This parallels how [Automated Peer Review](../core-concepts/automated-peer-review.md) systems evaluate research papers.

- **Wikipedia quality prediction at scale**: Lewoniewski et al. (2025) extended automated quality assessment to 55 Wikipedia language editions, demonstrating that structural features (the same ones this benchmark uses) transfer across languages and knowledge domains[^8]. Their finding that citation density is the strongest single predictor of article quality validates this benchmark's heavy weighting of the sourcing dimension.

- **Continuous documentation testing in industry**: Major tech companies now use CI/CD pipelines for documentation quality. Google's documentation team reported (2025) that automated quality checks reduced documentation defects by 40% compared to manual review alone[^9]. This validates the core premise of this benchmark: automated, repeatable quality measurement drives improvement more effectively than ad-hoc review.

- **Experiment-driven optimization**: The approach of treating each edit as a hypothesis and logging results draws from the [Automated Experiment Design](automated-experiment-design.md) methodology. Recent work on neural architecture search (2025) uses similar iterative refinement loops — propose a change, measure the effect, learn from the result[^10]. [AIDE](../tools-platforms/aide.md) implements this same pattern for ML code.

- **Application to AI-powered learning platforms**: Quality benchmarking of educational content is increasingly important as AI generates study materials at scale. Systems like Khan Academy's Khanmigo use quality rubrics similar to this benchmark's dimensions to evaluate AI-generated explanations before presenting them to students[^11]. The principle that *measurability drives improvement* applies equally to wiki articles and AI tutoring responses.

- **Holistic AI evaluation for education (2026)**: Sánchez-Ruiz et al. (2026) propose the first comprehensive evaluation methodology for AI systems in language education, addressing the "evaluation crisis" where no generally accepted evaluations for AI in education exist.[^12] Their framework evaluates across pedagogical effectiveness, response quality, adaptivity, and safety — dimensions that parallel this wiki's structural, sourcing, and currency metrics. This validates the multi-dimensional approach used here.

- **Meta-benchmarking: benchmarking the benchmarks (2026)**: BenchBench (Wang et al., 2026) introduces a three-stage pipeline for evaluating automated benchmark generation itself: extracting structured domain cards, prompting designer LLMs to generate test suites, and validating with a multi-model answerer panel.[^13] This meta-evaluation approach is directly relevant — as this wiki's benchmark matures, we need ways to evaluate whether the benchmark itself measures what matters.

- **Knowledge graph navigation as quality signal (2026)**: LLM-WikiRace (Wu et al., 2026) benchmarks LLM reasoning by requiring models to navigate Wikipedia hyperlinks from source to target pages.[^14] This reframes wiki quality from a static property (how good is this article?) to a dynamic one (how effectively can an AI navigate the knowledge structure?). Internal linking quality — one of this benchmark's dimensions — directly affects navigability.

- **Automated domain benchmark generation (2026)**: Peskoff et al. (2025, updated 2026) present a deterministic pipeline that transforms raw domain corpora into completion-style benchmarks without relying on other LLMs or costly human annotation.[^15] This approach could extend this wiki's benchmark by automatically generating comprehension questions from article content — testing whether articles convey knowledge effectively, not just whether they're well-structured.

- **Comprehensive educational benchmarking (2026)**: EduBench (Li et al., 2025, updated 2026) introduces a benchmark tailored for educational scenarios incorporating synthetic data across 9 major scenarios and over 4,000 distinct educational contexts.[^16] The scale and diversity of EduBench demonstrates that quality measurement in educational AI requires domain-specific evaluation — generic benchmarks miss domain-critical quality dimensions.

```svg
<svg viewBox="0 0 720 340" xmlns="http://www.w3.org/2000/svg" font-family="monospace" font-size="12">
  <text x="360" y="25" text-anchor="middle" font-size="15" font-weight="bold" fill="#1a1a2e">Evolution of Knowledge Quality Assessment (2015-2026)</text>

  <!-- Timeline -->
  <line x1="60" y1="70" x2="660" y2="70" stroke="#333" stroke-width="2"/>

  <!-- Era 1 -->
  <circle cx="120" cy="70" r="6" fill="#1565C0"/>
  <text x="120" y="55" text-anchor="middle" font-size="9" fill="#1565C0">2015</text>
  <rect x="40" y="85" width="160" height="70" rx="6" fill="#E3F2FD" stroke="#1565C0" stroke-width="1.5"/>
  <text x="120" y="102" text-anchor="middle" font-size="10" font-weight="bold" fill="#1565C0">Structural Features</text>
  <text x="120" y="118" text-anchor="middle" font-size="8">Section count, citations</text>
  <text x="120" y="132" text-anchor="middle" font-size="8">link density [4]</text>
  <text x="120" y="146" text-anchor="middle" font-size="8" fill="#1565C0">~80% accuracy</text>

  <!-- Era 2 -->
  <circle cx="330" cy="70" r="6" fill="#F57F17"/>
  <text x="330" y="55" text-anchor="middle" font-size="9" fill="#F57F17">2024-25</text>
  <rect x="250" y="85" width="160" height="70" rx="6" fill="#FFF8E1" stroke="#F57F17" stroke-width="1.5"/>
  <text x="330" y="102" text-anchor="middle" font-size="10" font-weight="bold" fill="#F57F17">LLM-as-Judge</text>
  <text x="330" y="118" text-anchor="middle" font-size="8">Semantic evaluation</text>
  <text x="330" y="132" text-anchor="middle" font-size="8">multi-dimensional [7]</text>
  <text x="330" y="146" text-anchor="middle" font-size="8" fill="#F57F17">>85% human agreement</text>

  <!-- Era 3 -->
  <circle cx="540" cy="70" r="6" fill="#2E7D32"/>
  <text x="540" y="55" text-anchor="middle" font-size="9" fill="#2E7D32">2026</text>
  <rect x="460" y="85" width="160" height="70" rx="6" fill="#E8F5E9" stroke="#2E7D32" stroke-width="1.5"/>
  <text x="540" y="102" text-anchor="middle" font-size="10" font-weight="bold" fill="#2E7D32">Meta-Benchmarking</text>
  <text x="540" y="118" text-anchor="middle" font-size="8">Benchmarking benchmarks</text>
  <text x="540" y="132" text-anchor="middle" font-size="8">navigability testing [13,14]</text>
  <text x="540" y="146" text-anchor="middle" font-size="8" fill="#2E7D32">Dynamic quality metrics</text>

  <!-- Arrows -->
  <line x1="205" y1="120" x2="245" y2="120" stroke="#333" stroke-width="1"/>
  <polygon points="243,116 250,120 243,124" fill="#333"/>
  <line x1="415" y1="120" x2="455" y2="120" stroke="#333" stroke-width="1"/>
  <polygon points="453,116 460,120 453,124" fill="#333"/>

  <!-- This wiki's approach -->
  <rect x="40" y="180" width="640" height="65" rx="8" fill="#EDE7F6" stroke="#4527A0" stroke-width="2"/>
  <text x="360" y="200" text-anchor="middle" font-size="12" font-weight="bold" fill="#4527A0">This Wiki's Benchmark: Structural + Experiment-Driven Learning</text>
  <text x="360" y="218" text-anchor="middle" font-size="10">7 dimensions × weighted scoring + hypothesis logging + trend tracking</text>
  <text x="360" y="233" text-anchor="middle" font-size="9" fill="#4527A0">Future: add semantic evaluation [12], navigability testing [14], auto-generated comprehension checks [15]</text>

  <!-- Learning application -->
  <rect x="100" y="260" width="520" height="65" rx="8" fill="#E0F7FA" stroke="#00838F" stroke-width="1.5"/>
  <text x="360" y="282" text-anchor="middle" font-size="12" font-weight="bold" fill="#00838F">Learning Application: Build Your Own Quality Loop</text>
  <text x="360" y="300" text-anchor="middle" font-size="10">Define dimensions → automate measurement → log experiments → learn what works</text>
  <text x="360" y="315" text-anchor="middle" font-size="9">Works for wikis, study guides, course materials, documentation — any knowledge resource</text>
</svg>
```

## Limitations

- **No semantic evaluation.** The benchmark measures structure, sourcing, and formatting — not whether the content is accurate or insightful. An article could score 100 with well-formatted nonsense. Future work could incorporate LLM-as-judge evaluation[^7].
- **Dimension weights are heuristic.** The 15/15/15/20/10/15/10 weighting was chosen by judgment, not empirically optimized. Different weights would produce different rankings.
- **Currency bias.** The scoring rewards recent references, which may penalize articles on mature topics where the key papers are older.
- **Freshness rewards churn.** The freshness dimension rewards recent file modifications, which could incentivize trivial edits. This is mitigated by its low weight (10%).
- **No cross-article coherence check.** Each article is scored independently. The benchmark doesn't detect contradictions between articles or redundant coverage across articles.

## See Also

- [Quality Benchmark (live scores)](../research-sources/benchmark-trend.md) — auto-generated scorecard and trend
- [Predictive Simulation Learning](../frontier-topics/predictive-simulation-learning.md) — the simulation-based learning approach this benchmarking loop mirrors
- [Recursive Self-Improvement](../frontier-topics/recursive-self-improvement.md) — the theoretical framework behind experiment-driven improvement loops
- [Cross-Cutting Connections](../frontier-topics/cross-cutting-connections.md) — how the benchmarking loop connects simulation (predict scores) and recursion (learn from past experiments)
- [Automated Peer Review](../core-concepts/automated-peer-review.md) — AI systems that evaluate research quality, the same principle applied to wiki articles
- [The AI Scientist](../core-concepts/the-ai-scientist.md) — the end-to-end research system whose iterative approach inspired this benchmark loop
- [Autoresearch](../tools-platforms/autoresearch.md) — Karpathy's minimal experiment loop, a parallel to this wiki's edit-score-learn cycle
- [AIDE](../tools-platforms/aide.md) — another autonomous experiment framework with similar iterative improvement patterns
- [Automated Experiment Design](automated-experiment-design.md) — the methodology of hypothesis-driven iteration that this benchmark implements
- [Agentic Tree Search](agentic-tree-search.md) — structured exploration that parallels the benchmark's systematic improvement strategy
- [Curriculum Learning](curriculum-learning.md) — progressive difficulty in knowledge assessment mirrors curriculum design
- [Active Learning](active-learning.md) — the benchmark loop selects which articles to improve next, analogous to active learning sample selection
- [Template-Free Research](template-free-research.md) — open-ended AI research where quality metrics guide exploration
- [VLM Integration](vlm-integration.md) — vision-language models that could enable visual quality checks of diagrams and formatting
- [Automated Scientific Discovery](../core-concepts/automated-scientific-discovery.md) — the broader goal that quality benchmarking supports
- [Foundation Models for Research](../core-concepts/foundation-models-for-research.md) — models that could power semantic quality evaluation
- [HuggingFace Papers API](../tools-platforms/huggingface-papers-api.md) — paper discovery that feeds currency scoring
- [Semantic Scholar API](../tools-platforms/semantic-scholar-api.md) — citation data that could enhance sourcing evaluation
- [AI E-Commerce Learning](../frontier-topics/ai-ecommerce-learning.md) — domain where content quality metrics drive product information improvement
- [Open-Ended Discovery](../frontier-topics/open-ended-discovery.md) — the open-ended improvement loop this benchmark enables
- [Scaling Laws for Research Automation](../frontier-topics/scaling-laws-research.md) — how quality scales with iterative effort
- [Key Papers and References](../research-sources/key-papers.md) — curated papers relevant to quality assessment
- [Tracking AI Research](../research-sources/tracking-ai-research.md) — monitoring new developments in automated evaluation
- [Institutions and Labs](../research-sources/institutions-and-labs.md) — research groups working on automated quality assessment

## References

[^1]: The benchmark methodology draws from automated assessment research. See [Automated Peer Review](../core-concepts/automated-peer-review.md) for how AI systems evaluate quality — the wiki applies the same principle to itself.

[^2]: The experiment-driven improvement loop is a direct application of the [Recursive Self-Improvement](../frontier-topics/recursive-self-improvement.md) paradigm: the system improves its own improvement process by learning which editing strategies are effective.

[^3]: Score trend tracking is inspired by [scaling laws research](../frontier-topics/scaling-laws-research.md) — tracking how quality scales with iterative effort, analogous to how model capability scales with compute.

[^4]: Warncke-Wang, M. et al. (2015). "Tell Me More: An Actionable Quality Model for Wikipedia." *WikiSym '15*. ACM.

[^5]: Liang, W. et al. (2024). "Can Large Language Models Provide Useful Feedback on Research Papers?" [arXiv:2310.01783](https://arxiv.org/abs/2310.01783)

[^6]: Gentle, A. (2017). *Docs Like Code: Write, Review, Merge, Deploy, Repeat.* Lulu Press. — Establishes the continuous integration model for documentation quality.

[^7]: Zheng, L. et al. (2025). "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena." *NeurIPS 2024*. [arXiv:2306.05685](https://arxiv.org/abs/2306.05685)

[^8]: Lewoniewski, W. et al. (2025). "Multilingual Quality Assessment of Wikipedia Articles Using Structural Features." *Information Processing & Management*, 62(1). [doi:10.1016/j.ipm.2024.103921](https://doi.org/10.1016/j.ipm.2024.103921)

[^9]: Google Technical Writing Team (2025). "Continuous Documentation Quality in Large-Scale Software Projects." Google Engineering Blog.

[^10]: White, C. et al. (2025). "Neural Architecture Search: Insights from 1000 Papers." [arXiv:2301.08727](https://arxiv.org/abs/2301.08727)

[^11]: Khan Academy (2025). "Khanmigo: AI-Powered Tutoring with Quality Guardrails." Khan Academy Engineering Blog.

[^12]: Sánchez-Ruiz, A. et al. (2026). "Beyond Accuracy: Towards a Robust Evaluation Methodology for AI Systems for Language Education." arXiv:2603.20088. https://arxiv.org/abs/2603.20088

[^13]: Wang, Y. et al. (2026). "BenchBench: Benchmarking Automated Benchmark Generation." arXiv:2603.20807. https://arxiv.org/abs/2603.20807

[^14]: Wu, Z. et al. (2026). "LLM-WikiRace: Benchmarking Long-term Planning and Reasoning over Real-World Knowledge Graphs." arXiv:2602.16902. https://arxiv.org/abs/2602.16902

[^15]: Peskoff, D. et al. (2025). "From Raw Corpora to Domain Benchmarks: Automated Evaluation of LLM Domain Expertise." arXiv:2506.07658. https://arxiv.org/abs/2506.07658

[^16]: Li, X. et al. (2025). "EduBench: A Comprehensive Benchmarking Dataset for Evaluating Large Language Models in Diverse Educational Scenarios." arXiv:2505.16160. https://arxiv.org/abs/2505.16160
