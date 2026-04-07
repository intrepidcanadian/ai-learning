# Quality Benchmark

Automated quality scores for the wiki's articles across all categories. Articles are scored with tier-aware expectations: **flagship** articles face the highest quality bar, **standard** articles have moderate expectations, and **reference** articles are evaluated primarily on linking and consistency.

Scores are computed by [`benchmark_wiki.py`](../benchmark_wiki.py) across seven dimensions: structural completeness, depth, currency, sourcing, internal linking, consistency, and freshness. See [Wiki Quality Benchmarking](../methodologies/wiki-quality-benchmarking.md) for full methodology.

## Current Score

**Overall: 85.8/100** | 45 articles | 148,032 words

Tier scores: **Standard:** 84.7 | **Flagship:** 96.8

Coverage: 26 substantial | 0 stubs (0.0%)

Freshness: 100.0% updated this week | median age: 0.1 days

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

*Last benchmarked: 2026-04-08T05:50*

### Core Concepts

| Article | Tier | Struct | Depth | Currency | Sourcing | Linking | Consist | Fresh | **Score** |
|---------|------|--------|-------|----------|----------|---------|---------|-------|-----------|
| hallucination-detection | standard | 100 | 80 | 80 | 97 | 82 | 100 | 99 | **89.9** |
| the-ai-scientist | standard | 100 | 56 | 85 | 100 | 77 | 100 | 97 | **86.4** |
| automated-scientific-discovery | standard | 100 | 75 | 58 | 94 | 77 | 100 | 96 | **84.2** |
| retrieval-augmented-generation | standard | 100 | 72 | 61 | 71 | 88 | 100 | 99 | **83.1** |
| foundation-models-for-research | standard | 100 | 53 | 63 | 100 | 77 | 100 | 97 | **82.6** |
| automated-peer-review | standard | 100 | 53 | 55 | 100 | 77 | 100 | 97 | **81.4** |
| knowledge-distillation | standard | 100 | 66 | 72 | 69 | 77 | 100 | 99 | **81.4** |
| transfer-learning | standard | 100 | 71 | 66 | 68 | 77 | 100 | 99 | **81.1** |

### Tools & Platforms

| Article | Tier | Struct | Depth | Currency | Sourcing | Linking | Consist | Fresh | **Score** |
|---------|------|--------|-------|----------|----------|---------|---------|-------|-----------|
| aider | standard | 100 | 60 | 88 | 86 | 84 | 100 | 97 | **86.8** |
| huggingface-papers-api | standard | 100 | 69 | 76 | 100 | 76 | 100 | 96 | **86.8** |
| semantic-scholar-api | standard | 100 | 69 | 71 | 100 | 76 | 100 | 97 | **86.0** |
| autoresearch | standard | 100 | 56 | 61 | 100 | 92 | 100 | 96 | **85.8** |
| aide | standard | 100 | 61 | 74 | 95 | 76 | 100 | 97 | **84.5** |
| code-generation | standard | 100 | 73 | 77 | 51 | 84 | 100 | 99 | **81.9** |

### Methodologies

| Article | Tier | Struct | Depth | Currency | Sourcing | Linking | Consist | Fresh | **Score** |
|---------|------|--------|-------|----------|----------|---------|---------|-------|-----------|
| interpretability | standard | 100 | 77 | 88 | 100 | 63 | 100 | 99 | **87.3** |
| domain-specificity | standard | 100 | 73 | 88 | 88 | 72 | 100 | 99 | **86.7** |
| vlm-integration | standard | 100 | 74 | 79 | 100 | 69 | 100 | 97 | **86.6** |
| prompt-engineering | standard | 100 | 78 | 80 | 89 | 71 | 100 | 99 | **86.2** |
| evaluation-methodology | standard | 100 | 73 | 60 | 100 | 81 | 100 | 99 | **86.1** |
| world-models | standard | 100 | 74 | 75 | 100 | 69 | 100 | 98 | **86.1** |
| applications-for-real-world-learning | standard | 100 | 76 | 92 | 79 | 70 | 100 | 99 | **86.0** |
| synthetic-data-generation | standard | 100 | 75 | 74 | 93 | 74 | 100 | 99 | **86.0** |
| inference-optimization | standard | 100 | 68 | 78 | 95 | 69 | 100 | 99 | **84.9** |
| test-time-compute | standard | 100 | 80 | 73 | 86 | 69 | 100 | 98 | **84.6** |
| agentic-tree-search | standard | 100 | 67 | 70 | 100 | 67 | 100 | 96 | **83.7** |
| template-free-research | standard | 100 | 65 | 68 | 94 | 67 | 100 | 96 | **82.2** |
| automated-experiment-design | standard | 100 | 62 | 61 | 100 | 69 | 100 | 97 | **82.1** |
| curriculum-learning | standard | 100 | 81 | 61 | 74 | 71 | 100 | 98 | **81.5** |
| computational-cost | standard | 100 | 58 | 70 | 90 | 67 | 100 | 99 | **81.0** |
| active-learning | standard | 100 | 70 | 82 | 62 | 67 | 100 | 99 | **80.5** |
| wiki-quality-benchmarking | standard | 100 | 69 | 57 | 79 | 69 | 100 | 96 | **79.3** |
| test-time-compute-scaling | standard | 100 | 72 | 83 | 56 | 63 | 100 | 99 | **79.2** |

### Frontier Topics

| Article | Tier | Struct | Depth | Currency | Sourcing | Linking | Consist | Fresh | **Score** |
|---------|------|--------|-------|----------|----------|---------|---------|-------|-----------|
| recursive-self-improvement | flagship | 100 | 100 | 99 | 96 | 86 | 100 | 99 | **97.6** |
| ai-ecommerce-learning | flagship | 100 | 100 | 100 | 92 | 82 | 100 | 99 | **96.6** |
| cross-cutting-connections | flagship | 100 | 100 | 100 | 88 | 91 | 100 | 99 | **96.6** |
| predictive-simulation-learning | flagship | 100 | 97 | 98 | 96 | 82 | 100 | 99 | **96.5** |
| multi-agent-systems | standard | 100 | 82 | 85 | 90 | 86 | 100 | 98 | **90.7** |
| blockchain-ai-optimization | standard | 100 | 70 | 74 | 94 | 82 | 100 | 96 | **86.9** |
| open-ended-discovery | standard | 100 | 48 | 80 | 100 | 82 | 100 | 97 | **85.5** |
| scaling-laws-research | standard | 100 | 58 | 73 | 98 | 77 | 100 | 97 | **84.6** |
| ai-safety-in-research | standard | 100 | 52 | 82 | 100 | 73 | 100 | 97 | **84.5** |
| e-commerce-applications | standard | 100 | 74 | 68 | 52 | 74 | 100 | 99 | **78.8** |

### Research Sources

| Article | Tier | Struct | Depth | Currency | Sourcing | Linking | Consist | Fresh | **Score** |
|---------|------|--------|-------|----------|----------|---------|---------|-------|-----------|
| institutions-and-labs | standard | 100 | 67 | 76 | 98 | 100 | 100 | 97 | **91.0** |
| tracking-ai-research | standard | 100 | 78 | 69 | 94 | 100 | 100 | 97 | **91.0** |
| key-papers | standard | 100 | 67 | 84 | 64 | 100 | 100 | 96 | **87.0** |

## Score Trend

**Overall composite:** 88.3 -> 85.8  `▅▅▅▆▆▆▆▆▆▆▆▆▇▇▇██   ▁▁▂▂▂▂▃▃▃▃▃▃▄▄▄▄▄▄▄▅▅▅▅▅▅▅▅▅▅▅▅▆▆▆▆▆▆▆▆▆▆▆▆▆▅▅▅▅▅▅▅▅▅▅▅▅▅▅`

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
<polygon points="55.0,93.6 63.4,93.6 71.8,93.6 80.1,81.1 88.5,68.1 96.9,68.1 105.3,68.1 113.6,67.5 122.0,68.1 130.4,68.1 138.8,68.1 147.1,67.5 155.5,60.4 163.9,55.0 172.3,49.6 180.6,43.0 189.0,43.0 197.4,230.6 205.8,232.8 214.2,232.8 222.5,202.9 230.9,202.9 239.3,180.1 247.7,180.1 256.0,167.0 264.4,167.0 272.8,156.7 281.2,156.7 289.5,154.5 297.9,154.5 306.3,142.6 314.7,139.8 323.1,135.5 331.4,135.5 339.8,125.2 348.2,125.7 356.6,125.7 364.9,114.8 373.3,114.8 381.7,103.9 390.1,103.9 398.4,103.9 406.8,103.9 415.2,103.9 423.6,103.9 431.9,103.9 440.3,103.9 448.7,98.0 457.1,98.0 465.5,93.6 473.8,93.6 482.2,87.6 490.6,87.6 499.0,87.6 507.3,87.6 515.7,87.6 524.1,87.6 532.5,87.6 540.8,87.6 549.2,87.6 557.6,87.6 566.0,87.6 574.4,87.6 582.7,87.6 591.1,93.1 599.5,93.1 607.9,108.3 616.2,108.3 624.6,108.3 633.0,108.8 641.4,108.8 649.7,107.8 658.1,107.2 666.5,107.2 674.9,106.7 683.2,106.7 691.6,106.7 700.0,107.2 700.0,260.0 55.0,260.0" fill="#4A90D9" opacity="0.1"/>
<polyline points="55.0,93.6 63.4,93.6 71.8,93.6 80.1,81.1 88.5,68.1 96.9,68.1 105.3,68.1 113.6,67.5 122.0,68.1 130.4,68.1 138.8,68.1 147.1,67.5 155.5,60.4 163.9,55.0 172.3,49.6 180.6,43.0 189.0,43.0 197.4,230.6 205.8,232.8 214.2,232.8 222.5,202.9 230.9,202.9 239.3,180.1 247.7,180.1 256.0,167.0 264.4,167.0 272.8,156.7 281.2,156.7 289.5,154.5 297.9,154.5 306.3,142.6 314.7,139.8 323.1,135.5 331.4,135.5 339.8,125.2 348.2,125.7 356.6,125.7 364.9,114.8 373.3,114.8 381.7,103.9 390.1,103.9 398.4,103.9 406.8,103.9 415.2,103.9 423.6,103.9 431.9,103.9 440.3,103.9 448.7,98.0 457.1,98.0 465.5,93.6 473.8,93.6 482.2,87.6 490.6,87.6 499.0,87.6 507.3,87.6 515.7,87.6 524.1,87.6 532.5,87.6 540.8,87.6 549.2,87.6 557.6,87.6 566.0,87.6 574.4,87.6 582.7,87.6 591.1,93.1 599.5,93.1 607.9,108.3 616.2,108.3 624.6,108.3 633.0,108.8 641.4,108.8 649.7,107.8 658.1,107.2 666.5,107.2 674.9,106.7 683.2,106.7 691.6,106.7 700.0,107.2" fill="none" stroke="#4A90D9" stroke-width="2.5" stroke-linejoin="round"/>
<circle class="chart-dot" cx="55.0" cy="93.6" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 18:27  —  Score: 88.3" data-note=""/>
<circle class="chart-dot" cx="80.1" cy="81.1" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 18:49  —  Score: 90.6" data-note=""/>
<circle class="chart-dot" cx="105.3" cy="68.1" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 18:57  —  Score: 93.0" data-note=""/>
<circle class="chart-dot" cx="130.4" cy="68.1" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 19:02  —  Score: 93.0" data-note=""/>
<circle class="chart-dot" cx="155.5" cy="60.4" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 19:11  —  Score: 94.4" data-note=""/>
<circle class="chart-dot" cx="180.6" cy="43.0" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 19:16  —  Score: 97.6" data-note=""/>
<circle class="chart-dot" cx="205.8" cy="232.8" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 19:51  —  Score: 62.7" data-note=""/>
<circle class="chart-dot" cx="222.5" cy="202.9" r="5" fill="#e67e22" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 20:09  —  Score: 68.2" data-note="Expand 5 lowest-scoring stubs (institutions-and-labs, vlm-integration, automated..."/>
<circle class="chart-dot" cx="230.9" cy="202.9" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 20:10  —  Score: 68.2" data-note=""/>
<circle class="chart-dot" cx="239.3" cy="180.1" r="5" fill="#e67e22" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 20:20  —  Score: 72.4" data-note="Expand the 4 lowest-scoring articles (tracking-ai-research, foundation-models-fo..."/>
<circle class="chart-dot" cx="256.0" cy="167.0" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 20:28  —  Score: 74.8" data-note=""/>
<circle class="chart-dot" cx="281.2" cy="156.7" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 20:30  —  Score: 76.7" data-note=""/>
<circle class="chart-dot" cx="289.5" cy="154.5" r="5" fill="#e67e22" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 20:34  —  Score: 77.1" data-note="Add background sections to lowest-scoring articles, add footnoted references to ..."/>
<circle class="chart-dot" cx="306.3" cy="142.6" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 20:42  —  Score: 79.3" data-note=""/>
<circle class="chart-dot" cx="323.1" cy="135.5" r="5" fill="#e67e22" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 20:45  —  Score: 80.6" data-note="Fix lowest-scoring article (ai-safety-in-research 58.6), add missing sections an..."/>
<circle class="chart-dot" cx="331.4" cy="135.5" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 20:52  —  Score: 80.6" data-note=""/>
<circle class="chart-dot" cx="348.2" cy="125.7" r="5" fill="#e67e22" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 21:01  —  Score: 82.4" data-note="Fix lowest-scoring articles (wiki-quality-benchmarking, template-free-research, ..."/>
<circle class="chart-dot" cx="356.6" cy="125.7" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 21:03  —  Score: 82.4" data-note=""/>
<circle class="chart-dot" cx="364.9" cy="114.8" r="5" fill="#e67e22" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 21:11  —  Score: 84.4" data-note="Expand the 4 lowest-scoring articles (aide, aider, semantic-scholar-api, agentic..."/>
<circle class="chart-dot" cx="381.7" cy="103.9" r="5" fill="#e67e22" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 22:15  —  Score: 86.4" data-note="Expand the 5 lowest-scoring articles with 2025-2026 papers (sourced from web sea..."/>
<circle class="chart-dot" cx="406.8" cy="103.9" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 22:27  —  Score: 86.4" data-note=""/>
<circle class="chart-dot" cx="431.9" cy="103.9" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 22:34  —  Score: 86.4" data-note=""/>
<circle class="chart-dot" cx="457.1" cy="98.0" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 22:58  —  Score: 87.5" data-note=""/>
<circle class="chart-dot" cx="482.2" cy="87.6" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 23:17  —  Score: 89.4" data-note=""/>
<circle class="chart-dot" cx="507.3" cy="87.6" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-08 00:30  —  Score: 89.4" data-note=""/>
<circle class="chart-dot" cx="532.5" cy="87.6" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-08 02:38  —  Score: 89.4" data-note=""/>
<circle class="chart-dot" cx="557.6" cy="87.6" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-08 03:03  —  Score: 89.4" data-note=""/>
<circle class="chart-dot" cx="582.7" cy="87.6" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-08 03:08  —  Score: 89.4" data-note=""/>
<circle class="chart-dot" cx="607.9" cy="108.3" r="5" fill="#e67e22" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-08 03:54  —  Score: 85.6" data-note="Write 5 new wishlist articles (hallucination-detection, interpretability, active..."/>
<circle class="chart-dot" cx="633.0" cy="108.8" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-08 04:10  —  Score: 85.5" data-note=""/>
<circle class="chart-dot" cx="658.1" cy="107.2" r="5" fill="#e67e22" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-08 04:25  —  Score: 85.8" data-note="Write 3 new wishlist articles (inference-optimization, knowledge-distillation, p..."/>
<circle class="chart-dot" cx="674.9" cy="106.7" r="5" fill="#e67e22" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-08 04:54  —  Score: 85.9" data-note="Write 3 new wishlist articles (applications-for-real-world-learning, computation..."/>
<circle class="chart-dot" cx="683.2" cy="106.7" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-08 05:35  —  Score: 85.9" data-note=""/>
<circle class="chart-dot" cx="700.0" cy="107.2" r="5" fill="#e67e22" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-08 05:50  —  Score: 85.8" data-note="Write 3 new wishlist articles (inference-optimization, knowledge-distillation, p..."/>
<text x="55.0" y="85.6" text-anchor="start" font-size="11" font-weight="bold" fill="#2c3e50">88.3</text>
<text x="197.4" y="222.6" text-anchor="middle" font-size="11" font-weight="bold" fill="#2c3e50">63.1</text>
<text x="700.0" y="99.2" text-anchor="end" font-size="11" font-weight="bold" fill="#2c3e50">85.8</text>
<text x="55.0" y="278" text-anchor="middle" font-size="10" fill="#888">18:27</text>
<text x="180.6" y="278" text-anchor="middle" font-size="10" fill="#888">19:16</text>
<text x="306.3" y="278" text-anchor="middle" font-size="10" fill="#888">20:42</text>
<text x="431.9" y="278" text-anchor="middle" font-size="10" fill="#888">22:34</text>
<text x="557.6" y="278" text-anchor="middle" font-size="10" fill="#888">2026-04-08</text>
<text x="683.2" y="278" text-anchor="middle" font-size="10" fill="#888">2026-04-08</text>
<text x="700.0" y="278" text-anchor="end" font-size="10" fill="#888">2026-04-08</text>
<line x1="197.4" y1="30" x2="197.4" y2="260" stroke="#e67e22" stroke-width="1.5" stroke-dasharray="5,3"/>
<text x="201.4" y="44" font-size="10" fill="#e67e22">v2</text>
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
| 2026-04-08 04:25 | v2 | **85.8** | 100.0 | 48.4% | 74% | 40 | Write 3 new wishlist articles (inference-optimization, knowledge-distillation, p... |
| 2026-04-08 04:42 | v2 | **85.8** | 100.0 | 48.4% | 74% | 40 |  |
| 2026-04-08 04:54 | v2 | **85.9** | 100.0 | 58.1% | 79% | 43 | Write 3 new wishlist articles (applications-for-real-world-learning, computation... |
| 2026-04-08 05:35 | v2 | **85.9** | 100.0 | 58.1% | 79% | 43 |  |
| 2026-04-08 05:38 | v2 | **85.9** | 100.0 | 58.1% | 79% | 43 |  |
| 2026-04-08 05:50 | v2 | **85.8** | 100.0 | 60.6% | 80% | 45 | Write 3 new wishlist articles (inference-optimization, knowledge-distillation, p... |

## Open Issues

*No issues found -- all articles pass all checks.*

---

*This page is auto-generated by `benchmark_wiki.py`. Do not edit manually.*