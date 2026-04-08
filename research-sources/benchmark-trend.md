# Quality Benchmark

Automated quality scores for the wiki's articles across all categories. Articles are scored with tier-aware expectations: **flagship** articles face the highest quality bar, **standard** articles have moderate expectations, and **reference** articles are evaluated primarily on linking and consistency.

Scores are computed by [`benchmark_wiki.py`](../benchmark_wiki.py) across seven dimensions: structural completeness, depth, currency, sourcing, internal linking, consistency, and freshness. See [Wiki Quality Benchmarking](../methodologies/wiki-quality-benchmarking.md) for full methodology.

## Current Score

**Overall: 87.8/100** | 45 articles | 160,444 words

Tier scores: **Standard:** 87.0 | **Flagship:** 96.6

Coverage: 34 substantial | 0 stubs (0.0%)

Freshness: 100.0% updated this week | median age: 0.7 days

### Coverage Metrics

| Metric | Score | Detail |
|--------|-------|--------|
| **Topic Coverage** | 100.0/100 | 45/45 cross-link references resolved, 0 gaps |
| **Wishlist Coverage** | 60.6% | 20/33 planned topics written, 13 remaining |
| **Combined Coverage** | 80% | Average of topic + wishlist — mode: **Quality** |

**Remaining wishlist topics:**

- core-concepts
- tools-platforms
- research-sources
- same-category-methodologies
- frontier-topics
- evaluation-difficulty
- catastrophic-forgetting
- application-to-real-world-learning
- distribution-shift
- 2025-2026-trends
- learning-connection
- 2026-landscape
- verification-bottleneck

*Last benchmarked: 2026-04-08T22:12*

### Core Concepts

| Article | Tier | Struct | Depth | Currency | Sourcing | Linking | Consist | Fresh | **Score** |
|---------|------|--------|-------|----------|----------|---------|---------|-------|-----------|
| retrieval-augmented-generation | standard | 100 | 72 | 89 | 96 | 88 | 100 | 99 | **91.1** |
| hallucination-detection | standard | 100 | 80 | 80 | 97 | 82 | 100 | 93 | **89.6** |
| foundation-models-for-research | standard | 100 | 76 | 76 | 100 | 82 | 100 | 99 | **89.2** |
| transfer-learning | standard | 100 | 72 | 87 | 85 | 77 | 100 | 94 | **86.7** |
| the-ai-scientist | standard | 100 | 56 | 85 | 100 | 77 | 100 | 90 | **86.0** |
| knowledge-distillation | standard | 100 | 66 | 81 | 84 | 77 | 100 | 95 | **84.8** |
| automated-peer-review | standard | 100 | 67 | 63 | 100 | 77 | 100 | 95 | **84.7** |
| automated-scientific-discovery | standard | 100 | 75 | 58 | 94 | 77 | 100 | 89 | **83.9** |

### Tools & Platforms

| Article | Tier | Struct | Depth | Currency | Sourcing | Linking | Consist | Fresh | **Score** |
|---------|------|--------|-------|----------|----------|---------|---------|-------|-----------|
| code-generation | standard | 100 | 88 | 92 | 86 | 84 | 100 | 99 | **91.7** |
| huggingface-papers-api | standard | 100 | 69 | 76 | 100 | 76 | 100 | 90 | **86.5** |
| aider | standard | 100 | 60 | 88 | 86 | 84 | 100 | 90 | **86.4** |
| semantic-scholar-api | standard | 100 | 69 | 71 | 100 | 76 | 100 | 90 | **85.7** |
| autoresearch | standard | 100 | 56 | 61 | 100 | 92 | 100 | 90 | **85.5** |
| aide | standard | 100 | 61 | 74 | 95 | 76 | 100 | 90 | **84.2** |

### Methodologies

| Article | Tier | Struct | Depth | Currency | Sourcing | Linking | Consist | Fresh | **Score** |
|---------|------|--------|-------|----------|----------|---------|---------|-------|-----------|
| agentic-tree-search | standard | 100 | 79 | 89 | 100 | 71 | 100 | 99 | **89.4** |
| active-learning | standard | 100 | 90 | 88 | 85 | 74 | 100 | 94 | **89.0** |
| curriculum-learning | standard | 100 | 81 | 83 | 100 | 71 | 100 | 95 | **88.5** |
| automated-experiment-design | standard | 100 | 88 | 76 | 100 | 69 | 100 | 99 | **88.4** |
| wiki-quality-benchmarking | standard | 100 | 72 | 87 | 100 | 74 | 100 | 93 | **88.3** |
| template-free-research | standard | 100 | 89 | 83 | 91 | 69 | 100 | 99 | **88.2** |
| computational-cost | standard | 100 | 76 | 81 | 97 | 74 | 100 | 94 | **87.6** |
| interpretability | standard | 100 | 77 | 88 | 100 | 63 | 100 | 93 | **87.0** |
| applications-for-real-world-learning | standard | 100 | 76 | 92 | 79 | 74 | 100 | 93 | **86.5** |
| domain-specificity | standard | 100 | 73 | 88 | 88 | 72 | 100 | 93 | **86.4** |
| vlm-integration | standard | 100 | 74 | 79 | 100 | 69 | 100 | 90 | **86.2** |
| prompt-engineering | standard | 100 | 78 | 80 | 89 | 71 | 100 | 93 | **85.9** |
| evaluation-methodology | standard | 100 | 73 | 60 | 100 | 81 | 100 | 92 | **85.8** |
| world-models | standard | 100 | 74 | 75 | 100 | 69 | 100 | 92 | **85.8** |
| synthetic-data-generation | standard | 100 | 75 | 74 | 93 | 74 | 100 | 92 | **85.7** |
| test-time-compute-scaling | standard | 100 | 75 | 90 | 79 | 70 | 100 | 93 | **85.2** |
| inference-optimization | standard | 100 | 68 | 78 | 95 | 69 | 100 | 92 | **84.5** |
| test-time-compute | standard | 100 | 80 | 73 | 86 | 69 | 100 | 92 | **84.2** |

### Frontier Topics

| Article | Tier | Struct | Depth | Currency | Sourcing | Linking | Consist | Fresh | **Score** |
|---------|------|--------|-------|----------|----------|---------|---------|-------|-----------|
| recursive-self-improvement | flagship | 100 | 100 | 99 | 96 | 86 | 100 | 92 | **97.2** |
| predictive-simulation-learning | flagship | 100 | 97 | 97 | 97 | 86 | 100 | 96 | **96.8** |
| cross-cutting-connections | flagship | 100 | 100 | 100 | 88 | 91 | 100 | 93 | **96.3** |
| ai-ecommerce-learning | flagship | 100 | 100 | 100 | 92 | 82 | 100 | 92 | **96.2** |
| multi-agent-systems | standard | 100 | 85 | 86 | 91 | 86 | 100 | 96 | **91.3** |
| e-commerce-applications | standard | 100 | 76 | 88 | 79 | 82 | 100 | 93 | **87.5** |
| blockchain-ai-optimization | standard | 100 | 70 | 74 | 94 | 82 | 100 | 90 | **86.6** |
| open-ended-discovery | standard | 100 | 48 | 80 | 100 | 82 | 100 | 90 | **85.1** |
| ai-safety-in-research | standard | 100 | 52 | 82 | 100 | 73 | 100 | 90 | **84.2** |
| scaling-laws-research | standard | 100 | 58 | 73 | 98 | 77 | 100 | 90 | **84.2** |

### Research Sources

| Article | Tier | Struct | Depth | Currency | Sourcing | Linking | Consist | Fresh | **Score** |
|---------|------|--------|-------|----------|----------|---------|---------|-------|-----------|
| tracking-ai-research | standard | 100 | 78 | 69 | 94 | 100 | 100 | 90 | **90.7** |
| institutions-and-labs | standard | 100 | 67 | 76 | 98 | 100 | 100 | 90 | **90.6** |
| key-papers | standard | 100 | 67 | 84 | 64 | 100 | 100 | 89 | **86.7** |

## Score Trend

**Overall composite:** 88.3 -> 87.8  `▅▅▅▆▆▆▆▆▆▆▆▆▇▇▇██   ▁▁▂▂▂▂▃▃▃▃▃▃▄▄▄▄▄▄▄▅▅▅▅▅▅▅▅▅▅▅▅▆▆▆▆▆▆▆▆▆▆▆▆▆▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅`

### Score Over Time

<div style="position:relative;display:inline-block;width:100%;max-width:720px">
<div id="chart-tooltip" style="display:none;position:absolute;background:#1a1a2e;color:#fff;padding:8px 12px;border-radius:6px;font-size:12px;pointer-events:none;z-index:10;max-width:320px;line-height:1.4;white-space:pre-wrap;box-shadow:0 2px 8px rgba(0,0,0,0.2)"></div>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 320" font-family="system-ui, -apple-system, sans-serif">
<rect width="720" height="320" fill="#fafafa" rx="8"/>
<text x="360" y="20" text-anchor="middle" font-size="14" font-weight="bold" fill="#1a1a2e">Wiki Quality Score Over Time</text>
<line x1="55" y1="236.6" x2="700" y2="236.6" stroke="#e0e0e0" stroke-width="1"/>
<text x="47" y="240.6" text-anchor="end" font-size="11" fill="#666">62</text>
<line x1="55" y1="209.4" x2="700" y2="209.4" stroke="#e0e0e0" stroke-width="1"/>
<text x="47" y="213.4" text-anchor="end" font-size="11" fill="#666">67</text>
<line x1="55" y1="182.2" x2="700" y2="182.2" stroke="#e0e0e0" stroke-width="1"/>
<text x="47" y="186.2" text-anchor="end" font-size="11" fill="#666">72</text>
<line x1="55" y1="155.1" x2="700" y2="155.1" stroke="#e0e0e0" stroke-width="1"/>
<text x="47" y="159.1" text-anchor="end" font-size="11" fill="#666">77</text>
<line x1="55" y1="127.9" x2="700" y2="127.9" stroke="#e0e0e0" stroke-width="1"/>
<text x="47" y="131.9" text-anchor="end" font-size="11" fill="#666">82</text>
<line x1="55" y1="100.7" x2="700" y2="100.7" stroke="#e0e0e0" stroke-width="1"/>
<text x="47" y="104.7" text-anchor="end" font-size="11" fill="#666">87</text>
<line x1="55" y1="73.5" x2="700" y2="73.5" stroke="#e0e0e0" stroke-width="1"/>
<text x="47" y="77.5" text-anchor="end" font-size="11" fill="#666">92</text>
<line x1="55" y1="46.3" x2="700" y2="46.3" stroke="#e0e0e0" stroke-width="1"/>
<text x="47" y="50.3" text-anchor="end" font-size="11" fill="#666">97</text>
<polygon points="55.0,93.6 62.3,93.6 69.7,93.6 77.0,81.1 84.3,68.1 91.6,68.1 99.0,68.1 106.3,67.5 113.6,68.1 121.0,68.1 128.3,68.1 135.6,67.5 143.0,60.4 150.3,55.0 157.6,49.6 164.9,43.0 172.3,43.0 179.6,230.6 186.9,232.8 194.3,232.8 201.6,202.9 208.9,202.9 216.2,180.1 223.6,180.1 230.9,167.0 238.2,167.0 245.6,156.7 252.9,156.7 260.2,154.5 267.6,154.5 274.9,142.6 282.2,139.8 289.5,135.5 296.9,135.5 304.2,125.2 311.5,125.7 318.9,125.7 326.2,114.8 333.5,114.8 340.9,103.9 348.2,103.9 355.5,103.9 362.8,103.9 370.2,103.9 377.5,103.9 384.8,103.9 392.2,103.9 399.5,98.0 406.8,98.0 414.1,93.6 421.5,93.6 428.8,87.6 436.1,87.6 443.5,87.6 450.8,87.6 458.1,87.6 465.5,87.6 472.8,87.6 480.1,87.6 487.4,87.6 494.8,87.6 502.1,87.6 509.4,87.6 516.8,87.6 524.1,93.1 531.4,93.1 538.8,108.3 546.1,108.3 553.4,108.3 560.7,108.8 568.1,108.8 575.4,107.8 582.7,107.2 590.1,107.2 597.4,106.7 604.7,106.7 612.0,106.7 619.4,107.2 626.7,107.2 634.0,104.5 641.4,104.5 648.7,101.8 656.0,102.3 663.4,100.7 670.7,100.7 678.0,101.8 685.3,98.5 692.7,98.5 700.0,96.3 700.0,260.0 55.0,260.0" fill="#4A90D9" opacity="0.1"/>
<polyline points="55.0,93.6 62.3,93.6 69.7,93.6 77.0,81.1 84.3,68.1 91.6,68.1 99.0,68.1 106.3,67.5 113.6,68.1 121.0,68.1 128.3,68.1 135.6,67.5 143.0,60.4 150.3,55.0 157.6,49.6 164.9,43.0 172.3,43.0 179.6,230.6 186.9,232.8 194.3,232.8 201.6,202.9 208.9,202.9 216.2,180.1 223.6,180.1 230.9,167.0 238.2,167.0 245.6,156.7 252.9,156.7 260.2,154.5 267.6,154.5 274.9,142.6 282.2,139.8 289.5,135.5 296.9,135.5 304.2,125.2 311.5,125.7 318.9,125.7 326.2,114.8 333.5,114.8 340.9,103.9 348.2,103.9 355.5,103.9 362.8,103.9 370.2,103.9 377.5,103.9 384.8,103.9 392.2,103.9 399.5,98.0 406.8,98.0 414.1,93.6 421.5,93.6 428.8,87.6 436.1,87.6 443.5,87.6 450.8,87.6 458.1,87.6 465.5,87.6 472.8,87.6 480.1,87.6 487.4,87.6 494.8,87.6 502.1,87.6 509.4,87.6 516.8,87.6 524.1,93.1 531.4,93.1 538.8,108.3 546.1,108.3 553.4,108.3 560.7,108.8 568.1,108.8 575.4,107.8 582.7,107.2 590.1,107.2 597.4,106.7 604.7,106.7 612.0,106.7 619.4,107.2 626.7,107.2 634.0,104.5 641.4,104.5 648.7,101.8 656.0,102.3 663.4,100.7 670.7,100.7 678.0,101.8 685.3,98.5 692.7,98.5 700.0,96.3" fill="none" stroke="#4A90D9" stroke-width="2.5" stroke-linejoin="round"/>
<circle class="chart-dot" cx="55.0" cy="93.6" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 18:27  —  Score: 88.3" data-note=""/>
<circle class="chart-dot" cx="84.3" cy="68.1" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 18:51  —  Score: 93.0" data-note=""/>
<circle class="chart-dot" cx="113.6" cy="68.1" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 19:02  —  Score: 93.0" data-note=""/>
<circle class="chart-dot" cx="143.0" cy="60.4" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 19:11  —  Score: 94.4" data-note=""/>
<circle class="chart-dot" cx="172.3" cy="43.0" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 19:19  —  Score: 97.6" data-note=""/>
<circle class="chart-dot" cx="201.6" cy="202.9" r="5" fill="#e67e22" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 20:09  —  Score: 68.2" data-note="Expand 5 lowest-scoring stubs (institutions-and-labs, vlm-integration, automated..."/>
<circle class="chart-dot" cx="216.2" cy="180.1" r="5" fill="#e67e22" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 20:20  —  Score: 72.4" data-note="Expand the 4 lowest-scoring articles (tracking-ai-research, foundation-models-fo..."/>
<circle class="chart-dot" cx="230.9" cy="167.0" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 20:28  —  Score: 74.8" data-note=""/>
<circle class="chart-dot" cx="260.2" cy="154.5" r="5" fill="#e67e22" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 20:34  —  Score: 77.1" data-note="Add background sections to lowest-scoring articles, add footnoted references to ..."/>
<circle class="chart-dot" cx="289.5" cy="135.5" r="5" fill="#e67e22" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 20:45  —  Score: 80.6" data-note="Fix lowest-scoring article (ai-safety-in-research 58.6), add missing sections an..."/>
<circle class="chart-dot" cx="311.5" cy="125.7" r="5" fill="#e67e22" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 21:01  —  Score: 82.4" data-note="Fix lowest-scoring articles (wiki-quality-benchmarking, template-free-research, ..."/>
<circle class="chart-dot" cx="318.9" cy="125.7" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 21:03  —  Score: 82.4" data-note=""/>
<circle class="chart-dot" cx="326.2" cy="114.8" r="5" fill="#e67e22" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 21:11  —  Score: 84.4" data-note="Expand the 4 lowest-scoring articles (aide, aider, semantic-scholar-api, agentic..."/>
<circle class="chart-dot" cx="340.9" cy="103.9" r="5" fill="#e67e22" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 22:15  —  Score: 86.4" data-note="Expand the 5 lowest-scoring articles with 2025-2026 papers (sourced from web sea..."/>
<circle class="chart-dot" cx="348.2" cy="103.9" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 22:23  —  Score: 86.4" data-note=""/>
<circle class="chart-dot" cx="377.5" cy="103.9" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 22:28  —  Score: 86.4" data-note=""/>
<circle class="chart-dot" cx="406.8" cy="98.0" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 22:58  —  Score: 87.5" data-note=""/>
<circle class="chart-dot" cx="436.1" cy="87.6" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-08 00:29  —  Score: 89.4" data-note=""/>
<circle class="chart-dot" cx="465.5" cy="87.6" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-08 02:29  —  Score: 89.4" data-note=""/>
<circle class="chart-dot" cx="494.8" cy="87.6" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-08 03:03  —  Score: 89.4" data-note=""/>
<circle class="chart-dot" cx="524.1" cy="93.1" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-08 03:16  —  Score: 88.4" data-note=""/>
<circle class="chart-dot" cx="538.8" cy="108.3" r="5" fill="#e67e22" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-08 03:54  —  Score: 85.6" data-note="Write 5 new wishlist articles (hallucination-detection, interpretability, active..."/>
<circle class="chart-dot" cx="553.4" cy="108.3" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-08 04:02  —  Score: 85.6" data-note=""/>
<circle class="chart-dot" cx="582.7" cy="107.2" r="5" fill="#e67e22" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-08 04:25  —  Score: 85.8" data-note="Write 2 new wishlist articles (e-commerce-applications, test-time-compute-scalin..."/>
<circle class="chart-dot" cx="597.4" cy="106.7" r="5" fill="#e67e22" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-08 04:54  —  Score: 85.9" data-note="Write 3 new wishlist articles (applications-for-real-world-learning, computation..."/>
<circle class="chart-dot" cx="612.0" cy="106.7" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-08 05:38  —  Score: 85.9" data-note=""/>
<circle class="chart-dot" cx="619.4" cy="107.2" r="5" fill="#e67e22" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-08 05:50  —  Score: 85.8" data-note="Write 2 new wishlist articles (e-commerce-applications, test-time-compute-scalin..."/>
<circle class="chart-dot" cx="641.4" cy="104.5" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-08 07:42  —  Score: 86.3" data-note=""/>
<circle class="chart-dot" cx="670.7" cy="100.7" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-08 13:54  —  Score: 87.0" data-note=""/>
<circle class="chart-dot" cx="700.0" cy="96.3" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-08 22:12  —  Score: 87.8" data-note=""/>
<text x="55.0" y="85.6" text-anchor="start" font-size="11" font-weight="bold" fill="#2c3e50">88.3</text>
<text x="179.6" y="222.6" text-anchor="middle" font-size="11" font-weight="bold" fill="#2c3e50">63.1</text>
<text x="700.0" y="88.3" text-anchor="end" font-size="11" font-weight="bold" fill="#2c3e50">87.8</text>
<text x="55.0" y="278" text-anchor="middle" font-size="10" fill="#888">18:27</text>
<text x="179.6" y="278" text-anchor="middle" font-size="10" fill="#888">19:47</text>
<text x="304.2" y="278" text-anchor="middle" font-size="10" fill="#888">20:59</text>
<text x="428.8" y="278" text-anchor="middle" font-size="10" fill="#888">23:17</text>
<text x="553.4" y="278" text-anchor="middle" font-size="10" fill="#888">2026-04-08</text>
<text x="678.0" y="278" text-anchor="middle" font-size="10" fill="#888">2026-04-08</text>
<text x="700.0" y="278" text-anchor="end" font-size="10" fill="#888">2026-04-08</text>
<line x1="179.6" y1="30" x2="179.6" y2="260" stroke="#e67e22" stroke-width="1.5" stroke-dasharray="5,3"/>
<text x="183.6" y="44" font-size="10" fill="#e67e22">v2</text>
</svg>
<script>
(function() {
  var tip = document.getElementById('chart-tooltip');
  if (!tip) return;
  var dots = document.querySelectorAll('.chart-dot');
  dots.forEach(function(dot) {
    dot.addEventListener('mouseenter', function(e) {
      var text = dot.getAttribute('data-tip');
      var note = dot.getAttribute('data-note');
      if (note) text += '\n' + note;
      tip.textContent = text;
      tip.style.display = 'block';
    });
    dot.addEventListener('mousemove', function(e) {
      var wrapper = tip.parentElement;
      var rect = wrapper.getBoundingClientRect();
      var x = e.clientX - rect.left + 12;
      var y = e.clientY - rect.top - 10;
      if (x + tip.offsetWidth > rect.width) x = x - tip.offsetWidth - 24;
      if (y < 0) y = y + 30;
      tip.style.left = x + 'px';
      tip.style.top = y + 'px';
    });
    dot.addEventListener('mouseleave', function() {
      tip.style.display = 'none';
    });
  });
})();
</script>
</div>

### Run History

| Timestamp | Ver | Quality | Topic Cov | Wishlist Cov | Combined | Articles | Notes |
|-----------|-----|---------|-----------|-------------|----------|----------|-------|
| 2026-04-07 18:27 | v1 | **88.3** | — | — | — | 4 |  |
| 2026-04-07 18:41 | v1 | **88.3** | — | — | — | 4 |  |
| 2026-04-07 18:43 | v1 | **88.3** | — | — | — | 4 |  |
| 2026-04-07 18:49 | v1 | **90.6** | — | — | — | 4 |  |
| 2026-04-07 18:51 | v1 | **93.0** | — | — | — | 4 |  |
| 2026-04-07 18:55 | v1 | **93.0** | — | — | — | 4 |  |
| 2026-04-07 18:57 | v1 | **93.0** | — | — | — | 4 |  |
| 2026-04-07 19:01 | v1 | **93.1** | — | — | — | 4 |  |
| 2026-04-07 19:02 | v1 | **93.0** | — | — | — | 4 |  |
| 2026-04-07 19:02 | v1 | **93.0** | — | — | — | 4 |  |
| 2026-04-07 19:03 | v1 | **93.0** | — | — | — | 4 |  |
| 2026-04-07 19:09 | v1 | **93.1** | — | — | — | 4 |  |
| 2026-04-07 19:11 | v1 | **94.4** | — | — | — | 4 |  |
| 2026-04-07 19:12 | v1 | **95.4** | — | — | — | 4 |  |
| 2026-04-07 19:14 | v1 | **96.4** | — | — | — | 4 |  |
| 2026-04-07 19:16 | v1 | **97.6** | — | — | — | 4 |  |
| 2026-04-07 19:19 | v1 | **97.6** | — | — | — | 4 |  |
| 2026-04-07 19:47 | v2 | **63.1** | — | — | — | 24 |  |
| 2026-04-07 19:51 | v2 | **62.7** | — | — | — | 25 |  |
| 2026-04-07 19:59 | v2 | **62.7** | — | — | — | 25 |  |
| 2026-04-07 20:09 | v2 | **68.2** | — | — | — | 25 | Expand 5 lowest-scoring stubs (institutions-and-labs, vlm-integration, automated... |
| 2026-04-07 20:10 | v2 | **68.2** | — | — | — | 25 |  |
| 2026-04-07 20:20 | v2 | **72.4** | — | — | — | 25 | Expand the 4 lowest-scoring articles (tracking-ai-research, foundation-models-fo... |
| 2026-04-07 20:22 | v2 | **72.4** | — | — | — | 25 |  |
| 2026-04-07 20:28 | v2 | **74.8** | — | — | — | 25 |  |
| 2026-04-07 20:28 | v2 | **74.8** | — | — | — | 25 |  |
| 2026-04-07 20:30 | v2 | **76.7** | — | — | — | 25 |  |
| 2026-04-07 20:30 | v2 | **76.7** | — | — | — | 25 |  |
| 2026-04-07 20:34 | v2 | **77.1** | — | — | — | 25 | Add background sections to lowest-scoring articles, add footnoted references to ... |
| 2026-04-07 20:38 | v2 | **77.1** | — | — | — | 25 |  |
| 2026-04-07 20:42 | v2 | **79.3** | — | — | — | 25 |  |
| 2026-04-07 20:43 | v2 | **79.8** | — | — | — | 25 |  |
| 2026-04-07 20:45 | v2 | **80.6** | — | — | — | 25 | Fix lowest-scoring article (ai-safety-in-research 58.6), add missing sections an... |
| 2026-04-07 20:52 | v2 | **80.6** | — | — | — | 25 |  |
| 2026-04-07 20:59 | v2 | **82.5** | — | — | — | 25 |  |
| 2026-04-07 21:01 | v2 | **82.4** | — | — | — | 25 | Fix lowest-scoring articles (wiki-quality-benchmarking, template-free-research, ... |
| 2026-04-07 21:03 | v2 | **82.4** | — | — | — | 25 |  |
| 2026-04-07 21:11 | v2 | **84.4** | — | — | — | 25 | Expand the 4 lowest-scoring articles (aide, aider, semantic-scholar-api, agentic... |
| 2026-04-07 22:03 | v2 | **84.4** | — | — | — | 25 |  |
| 2026-04-07 22:15 | v2 | **86.4** | — | — | — | 25 | Expand the 5 lowest-scoring articles with 2025-2026 papers (sourced from web sea... |
| 2026-04-07 22:23 | v2 | **86.4** | — | — | — | 25 |  |
| 2026-04-07 22:26 | v2 | **86.4** | — | — | — | 25 |  |
| 2026-04-07 22:27 | v2 | **86.4** | — | — | — | 25 |  |
| 2026-04-07 22:28 | v2 | **86.4** | — | — | — | 25 |  |
| 2026-04-07 22:28 | v2 | **86.4** | — | — | — | 25 |  |
| 2026-04-07 22:34 | v2 | **86.4** | — | — | — | 25 |  |
| 2026-04-07 22:38 | v2 | **86.4** | — | — | — | 25 |  |
| 2026-04-07 22:45 | v2 | **87.5** | — | — | — | 25 |  |
| 2026-04-07 22:58 | v2 | **87.5** | — | — | — | 25 |  |
| 2026-04-07 23:07 | v2 | **88.3** | — | — | — | 25 |  |
| 2026-04-07 23:09 | v2 | **88.3** | — | — | — | 25 |  |
| 2026-04-07 23:17 | v2 | **89.4** | — | — | — | 25 |  |
| 2026-04-08 00:29 | v2 | **89.4** | 96.3 | — | — | 25 |  |
| 2026-04-08 00:29 | v2 | **89.4** | 100.0 | — | — | 25 |  |
| 2026-04-08 00:30 | v2 | **89.4** | 100.0 | — | — | 25 |  |
| 2026-04-08 01:13 | v2 | **89.4** | 100.0 | — | — | 25 |  |
| 2026-04-08 02:29 | v2 | **89.4** | 100.0 | — | — | 25 |  |
| 2026-04-08 02:38 | v2 | **89.4** | 100.0 | 0.0% | 50% | 25 |  |
| 2026-04-08 02:47 | v2 | **89.4** | 100.0 | 0.0% | 50% | 25 |  |
| 2026-04-08 03:03 | v2 | **89.4** | 100.0 | 0.0% | 50% | 25 |  |
| 2026-04-08 03:03 | v2 | **89.4** | 100.0 | 0.0% | 50% | 25 |  |
| 2026-04-08 03:04 | v2 | **89.4** | 100.0 | 0.0% | 50% | 25 |  |
| 2026-04-08 03:04 | v2 | **89.4** | 100.0 | 0.0% | 50% | 25 |  |
| 2026-04-08 03:08 | v2 | **89.4** | 100.0 | 0.0% | 50% | 25 |  |
| 2026-04-08 03:16 | v2 | **88.4** | 100.0 | 20.0% | 60% | 29 |  |
| 2026-04-08 03:46 | v2 | **88.4** | 100.0 | 17.4% | 59% | 29 |  |
| 2026-04-08 03:54 | v2 | **85.6** | 100.0 | 32.1% | 66% | 34 | Write 5 new wishlist articles (hallucination-detection, interpretability, active... |
| 2026-04-08 04:01 | v2 | **85.6** | 100.0 | 31.0% | 66% | 34 |  |
| 2026-04-08 04:02 | v2 | **85.6** | 100.0 | 31.0% | 66% | 34 |  |
| 2026-04-08 04:10 | v2 | **85.5** | 100.0 | 38.7% | 69% | 37 |  |
| 2026-04-08 04:13 | v2 | **85.5** | 100.0 | 38.7% | 69% | 37 |  |
| 2026-04-08 04:25 | v2 | **85.7** | 100.0 | 48.4% | 74% | 40 |  |
| 2026-04-08 04:25 | v2 | **85.8** | 100.0 | 48.4% | 74% | 40 | Write 2 new wishlist articles (e-commerce-applications, test-time-compute-scalin... |
| 2026-04-08 04:42 | v2 | **85.8** | 100.0 | 48.4% | 74% | 40 |  |
| 2026-04-08 04:54 | v2 | **85.9** | 100.0 | 58.1% | 79% | 43 | Write 3 new wishlist articles (applications-for-real-world-learning, computation... |
| 2026-04-08 05:35 | v2 | **85.9** | 100.0 | 58.1% | 79% | 43 |  |
| 2026-04-08 05:38 | v2 | **85.9** | 100.0 | 58.1% | 79% | 43 |  |
| 2026-04-08 05:50 | v2 | **85.8** | 100.0 | 60.6% | 80% | 45 | Write 2 new wishlist articles (e-commerce-applications, test-time-compute-scalin... |
| 2026-04-08 06:03 | v2 | **85.8** | 100.0 | 60.6% | 80% | 45 |  |
| 2026-04-08 06:09 | v2 | **86.3** | 100.0 | 60.6% | 80% | 45 |  |
| 2026-04-08 07:42 | v2 | **86.3** | 100.0 | 60.6% | 80% | 45 |  |
| 2026-04-08 07:48 | v2 | **86.8** | 100.0 | 60.6% | 80% | 45 |  |
| 2026-04-08 12:17 | v2 | **86.7** | 100.0 | 60.6% | 80% | 45 |  |
| 2026-04-08 12:22 | v2 | **87.0** | 100.0 | 60.6% | 80% | 45 |  |
| 2026-04-08 13:54 | v2 | **87.0** | 100.0 | 60.6% | 80% | 45 |  |
| 2026-04-08 21:54 | v2 | **86.8** | 100.0 | 60.6% | 80% | 45 |  |
| 2026-04-08 21:58 | v2 | **87.4** | 100.0 | 60.6% | 80% | 45 |  |
| 2026-04-08 22:05 | v2 | **87.4** | 100.0 | 60.6% | 80% | 45 |  |
| 2026-04-08 22:12 | v2 | **87.8** | 100.0 | 60.6% | 80% | 45 |  |

## Open Issues

*No issues found -- all articles pass all checks.*

---

*This page is auto-generated by `benchmark_wiki.py`. Do not edit manually.*