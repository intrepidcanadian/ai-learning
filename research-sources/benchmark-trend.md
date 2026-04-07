# Quality Benchmark

Automated quality scores for the wiki's articles across all categories. Articles are scored with tier-aware expectations: **flagship** articles face the highest quality bar, **standard** articles have moderate expectations, and **reference** articles are evaluated primarily on linking and consistency.

Scores are computed by [`benchmark_wiki.py`](../benchmark_wiki.py) across seven dimensions: structural completeness, depth, currency, sourcing, internal linking, consistency, and freshness. See [Wiki Quality Benchmarking](../methodologies/wiki-quality-benchmarking.md) for full methodology.

## Current Score

**Overall: 89.4/100** | 25 articles | 101,850 words

Tier scores: **Standard:** 88.0 | **Flagship:** 97.0

Coverage: 10 substantial | 0 stubs (0.0%)

Freshness: 100.0% updated this week | median age: 0.0 days

*Last benchmarked: 2026-04-07T23:17*

### Core Concepts

| Article | Tier | Struct | Depth | Currency | Sourcing | Linking | Consist | Fresh | **Score** |
|---------|------|--------|-------|----------|----------|---------|---------|-------|-----------|
| the-ai-scientist | standard | 100 | 56 | 85 | 100 | 100 | 100 | 99 | **91.1** |
| automated-scientific-discovery | standard | 100 | 75 | 58 | 94 | 100 | 100 | 98 | **89.0** |
| foundation-models-for-research | standard | 100 | 53 | 63 | 100 | 100 | 100 | 99 | **87.4** |
| automated-peer-review | standard | 100 | 53 | 55 | 100 | 100 | 100 | 99 | **86.2** |

### Tools & Platforms

| Article | Tier | Struct | Depth | Currency | Sourcing | Linking | Consist | Fresh | **Score** |
|---------|------|--------|-------|----------|----------|---------|---------|-------|-----------|
| aider | standard | 100 | 60 | 88 | 86 | 90 | 100 | 99 | **88.0** |
| huggingface-papers-api | standard | 100 | 69 | 76 | 100 | 80 | 100 | 99 | **87.7** |
| autoresearch | standard | 100 | 56 | 61 | 100 | 100 | 100 | 99 | **87.5** |
| semantic-scholar-api | standard | 100 | 69 | 71 | 100 | 80 | 100 | 99 | **87.0** |
| aide | standard | 100 | 61 | 74 | 95 | 80 | 100 | 99 | **85.5** |

### Methodologies

| Article | Tier | Struct | Depth | Currency | Sourcing | Linking | Consist | Fresh | **Score** |
|---------|------|--------|-------|----------|----------|---------|---------|-------|-----------|
| vlm-integration | standard | 100 | 74 | 79 | 100 | 100 | 100 | 99 | **92.9** |
| agentic-tree-search | standard | 100 | 67 | 70 | 100 | 90 | 100 | 99 | **88.5** |
| automated-experiment-design | standard | 100 | 62 | 61 | 100 | 100 | 100 | 99 | **88.4** |
| template-free-research | standard | 100 | 65 | 68 | 94 | 90 | 100 | 99 | **87.0** |
| wiki-quality-benchmarking | standard | 100 | 69 | 57 | 79 | 100 | 100 | 99 | **85.7** |

### Frontier Topics

| Article | Tier | Struct | Depth | Currency | Sourcing | Linking | Consist | Fresh | **Score** |
|---------|------|--------|-------|----------|----------|---------|---------|-------|-----------|
| recursive-self-improvement | flagship | 100 | 100 | 99 | 96 | 94 | 100 | 98 | **98.4** |
| ai-ecommerce-learning | flagship | 100 | 97 | 100 | 95 | 88 | 100 | 98 | **97.1** |
| predictive-simulation-learning | flagship | 100 | 97 | 98 | 96 | 88 | 100 | 98 | **97.0** |
| cross-cutting-connections | flagship | 100 | 97 | 100 | 87 | 88 | 100 | 98 | **95.5** |
| blockchain-ai-optimization | standard | 100 | 70 | 74 | 94 | 90 | 100 | 99 | **88.7** |
| open-ended-discovery | standard | 100 | 48 | 80 | 100 | 88 | 100 | 99 | **86.8** |
| scaling-laws-research | standard | 100 | 58 | 73 | 98 | 82 | 100 | 99 | **85.7** |
| ai-safety-in-research | standard | 100 | 52 | 82 | 100 | 77 | 100 | 99 | **85.5** |

### Research Sources

| Article | Tier | Struct | Depth | Currency | Sourcing | Linking | Consist | Fresh | **Score** |
|---------|------|--------|-------|----------|----------|---------|---------|-------|-----------|
| institutions-and-labs | standard | 100 | 67 | 76 | 98 | 100 | 100 | 99 | **91.1** |
| tracking-ai-research | standard | 100 | 78 | 69 | 94 | 100 | 100 | 99 | **91.1** |
| key-papers | standard | 100 | 67 | 84 | 64 | 100 | 100 | 98 | **87.2** |

## Score Trend

**Overall composite:** 88.3 -> 89.4  `▅▅▅▆▆▆▆▆▆▆▆▆▇▇▇██   ▁▁▂▂▂▂▃▃▃▃▃▃▄▄▄▄▄▄▄▅▅▅▅▅▅▅▅▅▅▅▅▆`

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
<polygon points="55.0,93.6 67.6,93.6 80.3,93.6 92.9,81.1 105.6,68.1 118.2,68.1 130.9,68.1 143.5,67.5 156.2,68.1 168.8,68.1 181.5,68.1 194.1,67.5 206.8,60.4 219.4,55.0 232.1,49.6 244.7,43.0 257.4,43.0 270.0,230.6 282.6,232.8 295.3,232.8 307.9,202.9 320.6,202.9 333.2,180.1 345.9,180.1 358.5,167.0 371.2,167.0 383.8,156.7 396.5,156.7 409.1,154.5 421.8,154.5 434.4,142.6 447.1,139.8 459.7,135.5 472.4,135.5 485.0,125.2 497.6,125.7 510.3,125.7 522.9,114.8 535.6,114.8 548.2,103.9 560.9,103.9 573.5,103.9 586.2,103.9 598.8,103.9 611.5,103.9 624.1,103.9 636.8,103.9 649.4,98.0 662.1,98.0 674.7,93.6 687.4,93.6 700.0,87.6 700.0,260.0 55.0,260.0" fill="#4A90D9" opacity="0.1"/>
<polyline points="55.0,93.6 67.6,93.6 80.3,93.6 92.9,81.1 105.6,68.1 118.2,68.1 130.9,68.1 143.5,67.5 156.2,68.1 168.8,68.1 181.5,68.1 194.1,67.5 206.8,60.4 219.4,55.0 232.1,49.6 244.7,43.0 257.4,43.0 270.0,230.6 282.6,232.8 295.3,232.8 307.9,202.9 320.6,202.9 333.2,180.1 345.9,180.1 358.5,167.0 371.2,167.0 383.8,156.7 396.5,156.7 409.1,154.5 421.8,154.5 434.4,142.6 447.1,139.8 459.7,135.5 472.4,135.5 485.0,125.2 497.6,125.7 510.3,125.7 522.9,114.8 535.6,114.8 548.2,103.9 560.9,103.9 573.5,103.9 586.2,103.9 598.8,103.9 611.5,103.9 624.1,103.9 636.8,103.9 649.4,98.0 662.1,98.0 674.7,93.6 687.4,93.6 700.0,87.6" fill="none" stroke="#4A90D9" stroke-width="2.5" stroke-linejoin="round"/>
<circle class="chart-dot" cx="55.0" cy="93.6" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 18:27  —  Score: 88.3" data-note=""/>
<circle class="chart-dot" cx="80.3" cy="93.6" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 18:43  —  Score: 88.3" data-note=""/>
<circle class="chart-dot" cx="105.6" cy="68.1" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 18:51  —  Score: 93.0" data-note=""/>
<circle class="chart-dot" cx="130.9" cy="68.1" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 18:57  —  Score: 93.0" data-note=""/>
<circle class="chart-dot" cx="156.2" cy="68.1" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 19:02  —  Score: 93.0" data-note=""/>
<circle class="chart-dot" cx="181.5" cy="68.1" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 19:03  —  Score: 93.0" data-note=""/>
<circle class="chart-dot" cx="206.8" cy="60.4" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 19:11  —  Score: 94.4" data-note=""/>
<circle class="chart-dot" cx="232.1" cy="49.6" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 19:14  —  Score: 96.4" data-note=""/>
<circle class="chart-dot" cx="257.4" cy="43.0" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 19:19  —  Score: 97.6" data-note=""/>
<circle class="chart-dot" cx="282.6" cy="232.8" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 19:51  —  Score: 62.7" data-note=""/>
<circle class="chart-dot" cx="307.9" cy="202.9" r="5" fill="#e67e22" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 20:09  —  Score: 68.2" data-note="Expand 5 lowest-scoring stubs (institutions-and-labs, vlm-integration, automated..."/>
<circle class="chart-dot" cx="333.2" cy="180.1" r="5" fill="#e67e22" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 20:20  —  Score: 72.4" data-note="Expand the 4 lowest-scoring articles (tracking-ai-research, foundation-models-fo..."/>
<circle class="chart-dot" cx="358.5" cy="167.0" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 20:28  —  Score: 74.8" data-note=""/>
<circle class="chart-dot" cx="383.8" cy="156.7" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 20:30  —  Score: 76.7" data-note=""/>
<circle class="chart-dot" cx="409.1" cy="154.5" r="5" fill="#e67e22" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 20:34  —  Score: 77.1" data-note="Add background sections to lowest-scoring articles, add footnoted references to ..."/>
<circle class="chart-dot" cx="434.4" cy="142.6" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 20:42  —  Score: 79.3" data-note=""/>
<circle class="chart-dot" cx="459.7" cy="135.5" r="5" fill="#e67e22" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 20:45  —  Score: 80.6" data-note="Fix lowest-scoring article (ai-safety-in-research 58.6), add missing sections an..."/>
<circle class="chart-dot" cx="485.0" cy="125.2" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 20:59  —  Score: 82.5" data-note=""/>
<circle class="chart-dot" cx="497.6" cy="125.7" r="5" fill="#e67e22" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 21:01  —  Score: 82.4" data-note="Fix lowest-scoring articles (wiki-quality-benchmarking, template-free-research, ..."/>
<circle class="chart-dot" cx="510.3" cy="125.7" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 21:03  —  Score: 82.4" data-note=""/>
<circle class="chart-dot" cx="522.9" cy="114.8" r="5" fill="#e67e22" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 21:11  —  Score: 84.4" data-note="Expand the 4 lowest-scoring articles (aide, aider, semantic-scholar-api, agentic..."/>
<circle class="chart-dot" cx="535.6" cy="114.8" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 22:03  —  Score: 84.4" data-note=""/>
<circle class="chart-dot" cx="548.2" cy="103.9" r="5" fill="#e67e22" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 22:15  —  Score: 86.4" data-note="Expand the 5 lowest-scoring articles with 2025-2026 papers (sourced from web sea..."/>
<circle class="chart-dot" cx="560.9" cy="103.9" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 22:23  —  Score: 86.4" data-note=""/>
<circle class="chart-dot" cx="586.2" cy="103.9" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 22:27  —  Score: 86.4" data-note=""/>
<circle class="chart-dot" cx="611.5" cy="103.9" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 22:28  —  Score: 86.4" data-note=""/>
<circle class="chart-dot" cx="636.8" cy="103.9" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 22:38  —  Score: 86.4" data-note=""/>
<circle class="chart-dot" cx="662.1" cy="98.0" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 22:58  —  Score: 87.5" data-note=""/>
<circle class="chart-dot" cx="687.4" cy="93.6" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 23:09  —  Score: 88.3" data-note=""/>
<circle class="chart-dot" cx="700.0" cy="87.6" r="3.5" fill="#4A90D9" stroke="#fff" stroke-width="1.5" style="cursor:pointer" data-tip="2026-04-07 23:17  —  Score: 89.4" data-note=""/>
<text x="55.0" y="85.6" text-anchor="start" font-size="11" font-weight="bold" fill="#2c3e50">88.3</text>
<text x="270.0" y="222.6" text-anchor="middle" font-size="11" font-weight="bold" fill="#2c3e50">63.1</text>
<text x="700.0" y="79.6" text-anchor="end" font-size="11" font-weight="bold" fill="#2c3e50">89.4</text>
<text x="55.0" y="278" text-anchor="middle" font-size="10" fill="#888">18:27</text>
<text x="181.5" y="278" text-anchor="middle" font-size="10" fill="#888">19:03</text>
<text x="307.9" y="278" text-anchor="middle" font-size="10" fill="#888">20:09</text>
<text x="434.4" y="278" text-anchor="middle" font-size="10" fill="#888">20:42</text>
<text x="560.9" y="278" text-anchor="middle" font-size="10" fill="#888">22:23</text>
<text x="687.4" y="278" text-anchor="middle" font-size="10" fill="#888">23:09</text>
<text x="700.0" y="278" text-anchor="end" font-size="10" fill="#888">23:17</text>
<line x1="270.0" y1="30" x2="270.0" y2="260" stroke="#e67e22" stroke-width="1.5" stroke-dasharray="5,3"/>
<text x="274.0" y="44" font-size="10" fill="#e67e22">v2</text>
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

| Timestamp | Ver | Overall | Articles | Notes |
|-----------|-----|---------|----------|-------|
| 2026-04-07 18:27 | v1 | **88.3** | 4 |  |
| 2026-04-07 18:41 | v1 | **88.3** | 4 |  |
| 2026-04-07 18:43 | v1 | **88.3** | 4 |  |
| 2026-04-07 18:49 | v1 | **90.6** | 4 |  |
| 2026-04-07 18:51 | v1 | **93.0** | 4 |  |
| 2026-04-07 18:55 | v1 | **93.0** | 4 |  |
| 2026-04-07 18:57 | v1 | **93.0** | 4 |  |
| 2026-04-07 19:01 | v1 | **93.1** | 4 |  |
| 2026-04-07 19:02 | v1 | **93.0** | 4 |  |
| 2026-04-07 19:02 | v1 | **93.0** | 4 |  |
| 2026-04-07 19:03 | v1 | **93.0** | 4 |  |
| 2026-04-07 19:09 | v1 | **93.1** | 4 |  |
| 2026-04-07 19:11 | v1 | **94.4** | 4 |  |
| 2026-04-07 19:12 | v1 | **95.4** | 4 |  |
| 2026-04-07 19:14 | v1 | **96.4** | 4 |  |
| 2026-04-07 19:16 | v1 | **97.6** | 4 |  |
| 2026-04-07 19:19 | v1 | **97.6** | 4 |  |
| 2026-04-07 19:47 | v2 | **63.1** | 24 |  |
| 2026-04-07 19:51 | v2 | **62.7** | 25 |  |
| 2026-04-07 19:59 | v2 | **62.7** | 25 |  |
| 2026-04-07 20:09 | v2 | **68.2** | 25 | Expand 5 lowest-scoring stubs (institutions-and-labs, vlm-integration, automated... |
| 2026-04-07 20:10 | v2 | **68.2** | 25 |  |
| 2026-04-07 20:20 | v2 | **72.4** | 25 | Expand the 4 lowest-scoring articles (tracking-ai-research, foundation-models-fo... |
| 2026-04-07 20:22 | v2 | **72.4** | 25 |  |
| 2026-04-07 20:28 | v2 | **74.8** | 25 |  |
| 2026-04-07 20:28 | v2 | **74.8** | 25 |  |
| 2026-04-07 20:30 | v2 | **76.7** | 25 |  |
| 2026-04-07 20:30 | v2 | **76.7** | 25 |  |
| 2026-04-07 20:34 | v2 | **77.1** | 25 | Add background sections to lowest-scoring articles, add footnoted references to ... |
| 2026-04-07 20:38 | v2 | **77.1** | 25 |  |
| 2026-04-07 20:42 | v2 | **79.3** | 25 |  |
| 2026-04-07 20:43 | v2 | **79.8** | 25 |  |
| 2026-04-07 20:45 | v2 | **80.6** | 25 | Fix lowest-scoring article (ai-safety-in-research 58.6), add missing sections an... |
| 2026-04-07 20:52 | v2 | **80.6** | 25 |  |
| 2026-04-07 20:59 | v2 | **82.5** | 25 |  |
| 2026-04-07 21:01 | v2 | **82.4** | 25 | Fix lowest-scoring articles (wiki-quality-benchmarking, template-free-research, ... |
| 2026-04-07 21:03 | v2 | **82.4** | 25 |  |
| 2026-04-07 21:11 | v2 | **84.4** | 25 | Expand the 4 lowest-scoring articles (aide, aider, semantic-scholar-api, agentic... |
| 2026-04-07 22:03 | v2 | **84.4** | 25 |  |
| 2026-04-07 22:15 | v2 | **86.4** | 25 | Expand the 5 lowest-scoring articles with 2025-2026 papers (sourced from web sea... |
| 2026-04-07 22:23 | v2 | **86.4** | 25 |  |
| 2026-04-07 22:26 | v2 | **86.4** | 25 |  |
| 2026-04-07 22:27 | v2 | **86.4** | 25 |  |
| 2026-04-07 22:28 | v2 | **86.4** | 25 |  |
| 2026-04-07 22:28 | v2 | **86.4** | 25 |  |
| 2026-04-07 22:34 | v2 | **86.4** | 25 |  |
| 2026-04-07 22:38 | v2 | **86.4** | 25 |  |
| 2026-04-07 22:45 | v2 | **87.5** | 25 |  |
| 2026-04-07 22:58 | v2 | **87.5** | 25 |  |
| 2026-04-07 23:07 | v2 | **88.3** | 25 |  |
| 2026-04-07 23:09 | v2 | **88.3** | 25 |  |
| 2026-04-07 23:17 | v2 | **89.4** | 25 |  |

## Open Issues

*No issues found -- all articles pass all checks.*

---

*This page is auto-generated by `benchmark_wiki.py`. Do not edit manually.*