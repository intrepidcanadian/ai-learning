# Quality Benchmark

Automated quality scores for the wiki's articles across all categories. Articles are scored with tier-aware expectations: **flagship** articles face the highest quality bar, **standard** articles have moderate expectations, and **reference** articles are evaluated primarily on linking and consistency.

Scores are computed by [`benchmark_wiki.py`](../benchmark_wiki.py) across seven dimensions: structural completeness, depth, currency, sourcing, internal linking, consistency, and freshness. See [Wiki Quality Benchmarking](../methodologies/wiki-quality-benchmarking.md) for full methodology.

## Current Score

**Overall: 85.5/100** | 37 articles | 128,172 words

Tier scores: **Standard:** 84.1 | **Flagship:** 97.0

Coverage: 18 substantial | 0 stubs (0.0%)

Freshness: 100.0% updated this week | median age: 0.2 days

**Topic Coverage: 100.0/100** (36/36 references resolved, 0 gaps)

*Last benchmarked: 2026-04-08T04:10*

### Core Concepts

| Article | Tier | Struct | Depth | Currency | Sourcing | Linking | Consist | Fresh | **Score** |
|---------|------|--------|-------|----------|----------|---------|---------|-------|-----------|
| the-ai-scientist | standard | 100 | 56 | 85 | 100 | 80 | 100 | 97 | **87.0** |
| automated-scientific-discovery | standard | 100 | 75 | 58 | 94 | 80 | 100 | 96 | **84.9** |
| foundation-models-for-research | standard | 100 | 53 | 63 | 100 | 80 | 100 | 97 | **83.2** |
| automated-peer-review | standard | 100 | 53 | 55 | 100 | 80 | 100 | 97 | **82.0** |
| transfer-learning | standard | 100 | 71 | 66 | 68 | 80 | 100 | 99 | **81.7** |
| hallucination-detection | standard | 100 | 62 | 51 | 80 | 80 | 100 | 99 | **79.9** |
| retrieval-augmented-generation | standard | 100 | 71 | 43 | 49 | 78 | 100 | 99 | **75.0** |

### Tools & Platforms

| Article | Tier | Struct | Depth | Currency | Sourcing | Linking | Consist | Fresh | **Score** |
|---------|------|--------|-------|----------|----------|---------|---------|-------|-----------|
| aider | standard | 100 | 60 | 88 | 86 | 84 | 100 | 97 | **86.8** |
| huggingface-papers-api | standard | 100 | 69 | 76 | 100 | 76 | 100 | 97 | **86.8** |
| semantic-scholar-api | standard | 100 | 69 | 71 | 100 | 76 | 100 | 97 | **86.0** |
| autoresearch | standard | 100 | 56 | 61 | 100 | 92 | 100 | 97 | **85.8** |
| aide | standard | 100 | 61 | 74 | 95 | 76 | 100 | 97 | **84.5** |
| code-generation | standard | 100 | 73 | 77 | 51 | 82 | 100 | 99 | **81.5** |

### Methodologies

| Article | Tier | Struct | Depth | Currency | Sourcing | Linking | Consist | Fresh | **Score** |
|---------|------|--------|-------|----------|----------|---------|---------|-------|-----------|
| vlm-integration | standard | 100 | 74 | 79 | 100 | 74 | 100 | 97 | **87.6** |
| world-models | standard | 100 | 74 | 75 | 100 | 74 | 100 | 99 | **87.1** |
| test-time-compute | standard | 100 | 80 | 73 | 86 | 74 | 100 | 99 | **85.6** |
| agentic-tree-search | standard | 100 | 67 | 70 | 100 | 70 | 100 | 97 | **84.4** |
| automated-experiment-design | standard | 100 | 62 | 61 | 100 | 74 | 100 | 97 | **83.1** |
| curriculum-learning | standard | 100 | 81 | 61 | 74 | 78 | 100 | 99 | **83.0** |
| template-free-research | standard | 100 | 65 | 68 | 94 | 70 | 100 | 97 | **82.9** |
| active-learning | standard | 100 | 70 | 82 | 62 | 70 | 100 | 99 | **81.0** |
| wiki-quality-benchmarking | standard | 100 | 69 | 57 | 79 | 74 | 100 | 97 | **80.4** |
| interpretability | standard | 100 | 69 | 68 | 72 | 66 | 100 | 99 | **79.5** |
| evaluation-methodology | standard | 100 | 71 | 34 | 73 | 75 | 100 | 99 | **76.7** |
| synthetic-data-generation | standard | 100 | 75 | 49 | 64 | 64 | 100 | 99 | **76.0** |

### Frontier Topics

| Article | Tier | Struct | Depth | Currency | Sourcing | Linking | Consist | Fresh | **Score** |
|---------|------|--------|-------|----------|----------|---------|---------|-------|-----------|
| recursive-self-improvement | flagship | 100 | 100 | 99 | 96 | 90 | 100 | 96 | **97.9** |
| ai-ecommerce-learning | flagship | 100 | 100 | 100 | 92 | 85 | 100 | 99 | **96.9** |
| predictive-simulation-learning | flagship | 100 | 97 | 98 | 96 | 85 | 100 | 96 | **96.6** |
| cross-cutting-connections | flagship | 100 | 100 | 100 | 88 | 90 | 100 | 99 | **96.5** |
| multi-agent-systems | standard | 100 | 82 | 85 | 90 | 84 | 100 | 99 | **90.3** |
| blockchain-ai-optimization | standard | 100 | 70 | 74 | 94 | 86 | 100 | 97 | **87.8** |
| open-ended-discovery | standard | 100 | 48 | 80 | 100 | 85 | 100 | 97 | **86.0** |
| scaling-laws-research | standard | 100 | 58 | 73 | 98 | 80 | 100 | 97 | **85.2** |
| ai-safety-in-research | standard | 100 | 52 | 82 | 100 | 75 | 100 | 97 | **84.9** |

### Research Sources

| Article | Tier | Struct | Depth | Currency | Sourcing | Linking | Consist | Fresh | **Score** |
|---------|------|--------|-------|----------|----------|---------|---------|-------|-----------|
| institutions-and-labs | standard | 100 | 67 | 76 | 98 | 100 | 100 | 97 | **91.0** |
| tracking-ai-research | standard | 100 | 78 | 69 | 94 | 100 | 100 | 97 | **91.0** |
| key-papers | standard | 100 | 67 | 84 | 64 | 100 | 100 | 96 | **87.0** |

## Score Trend

**Overall composite:** 88.3 -> 85.5  `▅▅▅▆▆▆▆▆▆▆▆▆▇▇▇██   ▁▁▂▂▂▂▃▃▃▃▃▃▄▄▄▄▄▄▄▅▅▅▅▅▅▅▅▅▅▅▅▆▆▆▆▆▆▆▆▆▆▆▆▆▅▅▅▅▅▅`

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
<polygon points="55.0,93.6 64.3,93.6 73.7,93.6 83.0,81.1 92.4,68.1 101.7,68.1 111.1,68.1 120.4,67.5 129.8,68.1 139.1,68.1 148.5,68.1 157.8,67.5 167.2,60.4 176.5,55.0 185.9,49.6 195.2,43.0 204.6,43.0 213.9,230.6 223.3,232.8 232.6,232.8 242.0,202.9 251.3,202.9 260.7,180.1 270.0,180.1 279.3,167.0 288.7,167.0 298.0,156.7 307.4,156.7 316.7,154.5 326.1,154.5 335.4,142.6 344.8,139.8 354.1,135.5 363.5,135.5 372.8,125.2 382.2,125.7 391.5,125.7 400.9,114.8 410.2,114.8 419.6,103.9 428.9,103.9 438.3,103.9 447.6,103.9 457.0,103.9 466.3,103.9 475.7,103.9 485.0,103.9 494.3,98.0 503.7,98.0 513.0,93.6 522.4,93.6 531.7,87.6 541.1,87.6 550.4,87.6 559.8,87.6 569.1,87.6 578.5,87.6 587.8,87.6 597.2,87.6 606.5,87.6 615.9,87.6 625.2,87.6 634.6,87.6 643.9,87.6 653.3,93.1 662.6,93.1 672.0,108.3 681.3,108.3 690.7,108.3 700.0,108.8 700.0,260.0 55.0,260.0" fill="#4A90D9" opacity="0.1"/>
<polyline points="55.0,93.6 64.3,93.6 73.7,93.6 83.0,81.1 92.4,68.1 101.7,68.1 111.1,68.1 120.4,67.5 129.8,68.1 139.1,68.1 148.5,68.1 157.8,67.5 167.2,60.4 176.5,55.0 185.9,49.6 195.2,43.0 204.6,43.0 213.9,230.6 223.3,232.8 232.6,232.8 242.0,202.9 251.3,202.9 260.7,180.1 270.0,180.1 279.3,167.0 288.7,167.0 298.0,156.7 307.4,156.7 316.7,154.5 326.1,154.5 335.4,142.6 344.8,139.8 354.1,135.5 363.5,135.5 372.8,125.2 382.2,125.7 391.5,125.7 400.9,114.8 410.2,114.8 419.6,103.9 428.9,103.9 438.3,103.9 447.6,103.9 457.0,103.9 466.3,103.9 475.7,103.9 485.0,103.9 494.3,98.0 503.7,98.0 513.0,93.6 522.4,93.6 531.7,87.6 541.1,87.6 550.4,87.6 559.8,87.6 569.1,87.6 578.5,87.6 587.8,87.6 597.2,87.6 606.5,87.6 615.9,87.6 625.2,87.6 634.6,87.6 643.9,87.6 653.3,93.1 662.6,93.1 672.0,108.3 681.3,108.3 690.7,108.3 700.0,108.8" fill="none" stroke="#4A90D9" stroke-width="2.5" stroke-linejoin="round"/>
<circle class="chart-dot" cx="55.0" cy="93.6" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 18:27  —  Score: 88.3" data-note=""/>
<circle class="chart-dot" cx="83.0" cy="81.1" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 18:49  —  Score: 90.6" data-note=""/>
<circle class="chart-dot" cx="111.1" cy="68.1" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 18:57  —  Score: 93.0" data-note=""/>
<circle class="chart-dot" cx="139.1" cy="68.1" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 19:02  —  Score: 93.0" data-note=""/>
<circle class="chart-dot" cx="167.2" cy="60.4" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 19:11  —  Score: 94.4" data-note=""/>
<circle class="chart-dot" cx="195.2" cy="43.0" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 19:16  —  Score: 97.6" data-note=""/>
<circle class="chart-dot" cx="223.3" cy="232.8" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 19:51  —  Score: 62.7" data-note=""/>
<circle class="chart-dot" cx="242.0" cy="202.9" r="5" fill="#e67e22" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 20:09  —  Score: 68.2" data-note="Expand 5 lowest-scoring stubs (institutions-and-labs, vlm-integration, automated..."/>
<circle class="chart-dot" cx="251.3" cy="202.9" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 20:10  —  Score: 68.2" data-note=""/>
<circle class="chart-dot" cx="260.7" cy="180.1" r="5" fill="#e67e22" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 20:20  —  Score: 72.4" data-note="Expand the 4 lowest-scoring articles (tracking-ai-research, foundation-models-fo..."/>
<circle class="chart-dot" cx="279.3" cy="167.0" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 20:28  —  Score: 74.8" data-note=""/>
<circle class="chart-dot" cx="307.4" cy="156.7" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 20:30  —  Score: 76.7" data-note=""/>
<circle class="chart-dot" cx="316.7" cy="154.5" r="5" fill="#e67e22" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 20:34  —  Score: 77.1" data-note="Add background sections to lowest-scoring articles, add footnoted references to ..."/>
<circle class="chart-dot" cx="335.4" cy="142.6" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 20:42  —  Score: 79.3" data-note=""/>
<circle class="chart-dot" cx="354.1" cy="135.5" r="5" fill="#e67e22" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 20:45  —  Score: 80.6" data-note="Fix lowest-scoring article (ai-safety-in-research 58.6), add missing sections an..."/>
<circle class="chart-dot" cx="363.5" cy="135.5" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 20:52  —  Score: 80.6" data-note=""/>
<circle class="chart-dot" cx="382.2" cy="125.7" r="5" fill="#e67e22" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 21:01  —  Score: 82.4" data-note="Fix lowest-scoring articles (wiki-quality-benchmarking, template-free-research, ..."/>
<circle class="chart-dot" cx="391.5" cy="125.7" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 21:03  —  Score: 82.4" data-note=""/>
<circle class="chart-dot" cx="400.9" cy="114.8" r="5" fill="#e67e22" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 21:11  —  Score: 84.4" data-note="Expand the 4 lowest-scoring articles (aide, aider, semantic-scholar-api, agentic..."/>
<circle class="chart-dot" cx="419.6" cy="103.9" r="5" fill="#e67e22" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 22:15  —  Score: 86.4" data-note="Expand the 5 lowest-scoring articles with 2025-2026 papers (sourced from web sea..."/>
<circle class="chart-dot" cx="447.6" cy="103.9" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 22:27  —  Score: 86.4" data-note=""/>
<circle class="chart-dot" cx="475.7" cy="103.9" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 22:34  —  Score: 86.4" data-note=""/>
<circle class="chart-dot" cx="503.7" cy="98.0" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 22:58  —  Score: 87.5" data-note=""/>
<circle class="chart-dot" cx="531.7" cy="87.6" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 23:17  —  Score: 89.4" data-note=""/>
<circle class="chart-dot" cx="559.8" cy="87.6" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-08 00:30  —  Score: 89.4" data-note=""/>
<circle class="chart-dot" cx="587.8" cy="87.6" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-08 02:38  —  Score: 89.4" data-note=""/>
<circle class="chart-dot" cx="615.9" cy="87.6" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-08 03:03  —  Score: 89.4" data-note=""/>
<circle class="chart-dot" cx="643.9" cy="87.6" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-08 03:08  —  Score: 89.4" data-note=""/>
<circle class="chart-dot" cx="672.0" cy="108.3" r="5" fill="#e67e22" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-08 03:54  —  Score: 85.6" data-note="Write 5 new wishlist articles (hallucination-detection, interpretability, active..."/>
<circle class="chart-dot" cx="700.0" cy="108.8" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-08 04:10  —  Score: 85.5" data-note=""/>
<text x="55.0" y="85.6" text-anchor="start" font-size="11" font-weight="bold" fill="#2c3e50">88.3</text>
<text x="213.9" y="222.6" text-anchor="middle" font-size="11" font-weight="bold" fill="#2c3e50">63.1</text>
<text x="700.0" y="100.8" text-anchor="end" font-size="11" font-weight="bold" fill="#2c3e50">85.5</text>
<text x="55.0" y="278" text-anchor="middle" font-size="10" fill="#888">18:27</text>
<text x="176.5" y="278" text-anchor="middle" font-size="10" fill="#888">19:12</text>
<text x="298.0" y="278" text-anchor="middle" font-size="10" fill="#888">20:30</text>
<text x="419.6" y="278" text-anchor="middle" font-size="10" fill="#888">22:15</text>
<text x="541.1" y="278" text-anchor="middle" font-size="10" fill="#888">2026-04-08</text>
<text x="662.6" y="278" text-anchor="middle" font-size="10" fill="#888">2026-04-08</text>
<text x="700.0" y="278" text-anchor="end" font-size="10" fill="#888">2026-04-08</text>
<line x1="213.9" y1="30" x2="213.9" y2="260" stroke="#e67e22" stroke-width="1.5" stroke-dasharray="5,3"/>
<text x="217.9" y="44" font-size="10" fill="#e67e22">v2</text>
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

| Timestamp | Ver | Quality | Coverage | Articles | Notes |
|-----------|-----|---------|----------|----------|-------|
| 2026-04-07 18:27 | v1 | **88.3** | — | 4 |  |
| 2026-04-07 18:41 | v1 | **88.3** | — | 4 |  |
| 2026-04-07 18:43 | v1 | **88.3** | — | 4 |  |
| 2026-04-07 18:49 | v1 | **90.6** | — | 4 |  |
| 2026-04-07 18:51 | v1 | **93.0** | — | 4 |  |
| 2026-04-07 18:55 | v1 | **93.0** | — | 4 |  |
| 2026-04-07 18:57 | v1 | **93.0** | — | 4 |  |
| 2026-04-07 19:01 | v1 | **93.1** | — | 4 |  |
| 2026-04-07 19:02 | v1 | **93.0** | — | 4 |  |
| 2026-04-07 19:02 | v1 | **93.0** | — | 4 |  |
| 2026-04-07 19:03 | v1 | **93.0** | — | 4 |  |
| 2026-04-07 19:09 | v1 | **93.1** | — | 4 |  |
| 2026-04-07 19:11 | v1 | **94.4** | — | 4 |  |
| 2026-04-07 19:12 | v1 | **95.4** | — | 4 |  |
| 2026-04-07 19:14 | v1 | **96.4** | — | 4 |  |
| 2026-04-07 19:16 | v1 | **97.6** | — | 4 |  |
| 2026-04-07 19:19 | v1 | **97.6** | — | 4 |  |
| 2026-04-07 19:47 | v2 | **63.1** | — | 24 |  |
| 2026-04-07 19:51 | v2 | **62.7** | — | 25 |  |
| 2026-04-07 19:59 | v2 | **62.7** | — | 25 |  |
| 2026-04-07 20:09 | v2 | **68.2** | — | 25 | Expand 5 lowest-scoring stubs (institutions-and-labs, vlm-integration, automated... |
| 2026-04-07 20:10 | v2 | **68.2** | — | 25 |  |
| 2026-04-07 20:20 | v2 | **72.4** | — | 25 | Expand the 4 lowest-scoring articles (tracking-ai-research, foundation-models-fo... |
| 2026-04-07 20:22 | v2 | **72.4** | — | 25 |  |
| 2026-04-07 20:28 | v2 | **74.8** | — | 25 |  |
| 2026-04-07 20:28 | v2 | **74.8** | — | 25 |  |
| 2026-04-07 20:30 | v2 | **76.7** | — | 25 |  |
| 2026-04-07 20:30 | v2 | **76.7** | — | 25 |  |
| 2026-04-07 20:34 | v2 | **77.1** | — | 25 | Add background sections to lowest-scoring articles, add footnoted references to ... |
| 2026-04-07 20:38 | v2 | **77.1** | — | 25 |  |
| 2026-04-07 20:42 | v2 | **79.3** | — | 25 |  |
| 2026-04-07 20:43 | v2 | **79.8** | — | 25 |  |
| 2026-04-07 20:45 | v2 | **80.6** | — | 25 | Fix lowest-scoring article (ai-safety-in-research 58.6), add missing sections an... |
| 2026-04-07 20:52 | v2 | **80.6** | — | 25 |  |
| 2026-04-07 20:59 | v2 | **82.5** | — | 25 |  |
| 2026-04-07 21:01 | v2 | **82.4** | — | 25 | Fix lowest-scoring articles (wiki-quality-benchmarking, template-free-research, ... |
| 2026-04-07 21:03 | v2 | **82.4** | — | 25 |  |
| 2026-04-07 21:11 | v2 | **84.4** | — | 25 | Expand the 4 lowest-scoring articles (aide, aider, semantic-scholar-api, agentic... |
| 2026-04-07 22:03 | v2 | **84.4** | — | 25 |  |
| 2026-04-07 22:15 | v2 | **86.4** | — | 25 | Expand the 5 lowest-scoring articles with 2025-2026 papers (sourced from web sea... |
| 2026-04-07 22:23 | v2 | **86.4** | — | 25 |  |
| 2026-04-07 22:26 | v2 | **86.4** | — | 25 |  |
| 2026-04-07 22:27 | v2 | **86.4** | — | 25 |  |
| 2026-04-07 22:28 | v2 | **86.4** | — | 25 |  |
| 2026-04-07 22:28 | v2 | **86.4** | — | 25 |  |
| 2026-04-07 22:34 | v2 | **86.4** | — | 25 |  |
| 2026-04-07 22:38 | v2 | **86.4** | — | 25 |  |
| 2026-04-07 22:45 | v2 | **87.5** | — | 25 |  |
| 2026-04-07 22:58 | v2 | **87.5** | — | 25 |  |
| 2026-04-07 23:07 | v2 | **88.3** | — | 25 |  |
| 2026-04-07 23:09 | v2 | **88.3** | — | 25 |  |
| 2026-04-07 23:17 | v2 | **89.4** | — | 25 |  |
| 2026-04-08 00:29 | v2 | **89.4** | 96.3 | 25 |  |
| 2026-04-08 00:29 | v2 | **89.4** | 100.0 | 25 |  |
| 2026-04-08 00:30 | v2 | **89.4** | 100.0 | 25 |  |
| 2026-04-08 01:13 | v2 | **89.4** | 100.0 | 25 |  |
| 2026-04-08 02:29 | v2 | **89.4** | 100.0 | 25 |  |
| 2026-04-08 02:38 | v2 | **89.4** | 100.0 | 25 |  |
| 2026-04-08 02:47 | v2 | **89.4** | 100.0 | 25 |  |
| 2026-04-08 03:03 | v2 | **89.4** | 100.0 | 25 |  |
| 2026-04-08 03:03 | v2 | **89.4** | 100.0 | 25 |  |
| 2026-04-08 03:04 | v2 | **89.4** | 100.0 | 25 |  |
| 2026-04-08 03:04 | v2 | **89.4** | 100.0 | 25 |  |
| 2026-04-08 03:08 | v2 | **89.4** | 100.0 | 25 |  |
| 2026-04-08 03:16 | v2 | **88.4** | 100.0 | 29 |  |
| 2026-04-08 03:46 | v2 | **88.4** | 100.0 | 29 |  |
| 2026-04-08 03:54 | v2 | **85.6** | 100.0 | 34 | Write 5 new wishlist articles (hallucination-detection, interpretability, active... |
| 2026-04-08 04:01 | v2 | **85.6** | 100.0 | 34 |  |
| 2026-04-08 04:02 | v2 | **85.6** | 100.0 | 34 |  |
| 2026-04-08 04:10 | v2 | **85.5** | 100.0 | 37 |  |

## Open Issues

*No issues found -- all articles pass all checks.*

---

*This page is auto-generated by `benchmark_wiki.py`. Do not edit manually.*