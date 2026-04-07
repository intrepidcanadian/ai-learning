# Autoresearch (Karpathy)

**Autoresearch** is a minimal framework by Andrej Karpathy that enables AI coding agents (Claude, Codex, etc.) to conduct fully autonomous machine learning research on a single GPU, without human supervision. The human sets the research direction, goes to sleep, and wakes up to ~100 completed experiments and (hopefully) an improved model.

**Repository:** [github.com/karpathy/autoresearch](https://github.com/karpathy/autoresearch)
**License:** MIT

## Overview

Autoresearch embodies a philosophy of radical simplicity: one GPU, one file, one metric. An AI agent modifies a single training script in a perpetual loop -- proposing changes, training for exactly 5 minutes, evaluating results, and keeping or discarding each experiment.

Unlike [The AI Scientist](../core-concepts/the-ai-scientist.md), which aims to produce full papers, Autoresearch focuses purely on **empirical improvement** -- making a model measurably better through autonomous experimentation.

## Architecture

The entire project consists of three files:

### `prepare.py` (Read-Only)
Contains immutable constants, data preparation (dataset downloads, BPE tokenizer training), the dataloader, and the evaluation function (`evaluate_bpb`). The agent is **forbidden** from modifying this file -- it serves as the fixed ground truth.

### `train.py` (The Single Editable File)
Contains the complete GPT model definition, optimizer (Muon + AdamW), and training loop. Everything is in scope for modification:
- Architecture (attention, FFN, normalization)
- Hyperparameters (learning rate, batch size, depth)
- Optimizer configuration
- Activation functions
- Any other training detail

### `program.md` (Agent Instructions)
A structured markdown file that serves as the "skill definition" for the AI agent. Contains the full protocol: setup, rules, logging format, and the autonomous loop logic. Humans iterate on this file to steer research direction.

## The Autonomous Loop

```
1. Establish baseline       --> Train train.py as-is, record val_bpb
2. Propose a change         --> Agent modifies train.py
3. Git commit               --> On branch autoresearch/<date>
4. Train (5 min exactly)    --> uv run train.py > run.log 2>&1
5. Evaluate                 --> Extract val_bpb and peak_vram_mb
6. Keep or discard          --> If improved: keep. Else: git reset
7. Log to results.tsv       --> commit, val_bpb, vram, status, description
8. Repeat forever           --> Never stop or ask permission
```

The agent runs ~12 experiments per hour, ~100 overnight on a single GPU.

## Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| Fixed 5-minute time budget | Standardizes comparison across experiments |
| Single metric (`val_bpb`) | Bits per byte is vocabulary-size-independent |
| Single editable file | Keeps diffs reviewable, scope manageable |
| Simplicity criterion | Agent prefers simpler code; removing code while maintaining performance is a win |
| No dependencies | One GPU, one file, one metric -- no distributed training or complex configs |
| Never stop | Agent runs until manually interrupted |

## Comparison with The AI Scientist

| Aspect | Autoresearch | The AI Scientist |
|--------|-------------|-----------------|
| Goal | Improve a model | Produce a paper |
| Scope | Training loop optimization | Full research lifecycle |
| Output | `results.tsv` + improved `train.py` | LaTeX manuscript + review |
| Cost per experiment | ~$0.01--0.10 (API calls) | $6--15 per paper |
| Human role | Write `program.md`, review in morning | Set research subfield |
| Models used | Any coding agent | Multi-model ensemble |
| Complexity | 3 files | Complex agentic pipeline |

## Hardware Requirements

- Single NVIDIA GPU (tested on H100)
- Python 3.10+
- `uv` package manager

For smaller GPUs: use lower-entropy datasets (TinyStories), reduce vocab size, lower sequence length, reduce model depth, decrease batch size.

## Community

The project has spawned community forks for:
- **macOS** (MPS/MLX backends)
- **Windows** (RTX GPUs)
- **AMD GPUs** (ROCm)

## Significance

Autoresearch represents a different philosophy from The AI Scientist: rather than automating the full research communication pipeline, it automates the **core empirical loop** that drives ML progress. It shifts the human role from "person who runs experiments" to "person who designs the research program and reviews results."

## Background / Theoretical Foundations

Autoresearch builds on the idea that **empirical ML research is fundamentally a search problem**: given a fixed evaluation metric, find the model configuration that optimizes it. This frames the agent's role as an optimization process over code space [^1].

Key intellectual foundations:

- **Neural architecture search (NAS)**: Zoph & Le (2017) demonstrated that AI agents can search over neural network architectures to find designs that outperform human-designed models [^2]. Autoresearch generalizes this: instead of searching architectures only, the agent searches over the entire training configuration.
- **AI-generating algorithms (AI-GAs)**: Clune (2019) proposed systems that automatically generate the components of AI — architectures, learning rules, and training environments — in an open-ended loop [^3]. Autoresearch is a minimal, practical instantiation of this vision.
- **Coding agents for research**: The rise of capable coding agents (Claude, Codex, Gemini) made it practical to have AI systems modify and execute research code autonomously [^4]. Autoresearch's contribution is showing that a *minimal* agent loop — one file, one metric, one GPU — is sufficient for meaningful research progress.

**Learning application**: Autoresearch demonstrates a powerful study technique for ML practitioners. By setting up a simple experiment loop (hypothesis → code change → evaluate → keep or discard), learners can develop intuition for which changes matter. The "overnight 100 experiments" pattern is directly applicable to coursework and personal projects — set up automated hyperparameter sweeps and review results in the morning.

## Current State / Latest Developments (2025–2026)

- **Agentic research frameworks proliferating:** Autoresearch's minimal loop has influenced a wave of more sophisticated agentic research systems. The "Agentic AI for Scientific Discovery" survey (Chen et al., 2025) identifies Autoresearch as a key exemplar of the "empirical loop" pattern alongside more complex systems like AIDE and The AI Scientist[^5]
- **World model integration:** Dyna-Mind (Yu et al., 2025) extends the empirical loop concept by teaching agents to build internal simulations of experiment outcomes before running them, reducing the number of physical experiments needed by up to 40%[^6]. This predict-then-verify approach could make Autoresearch-style loops more compute-efficient
- **Self-play for agent improvement:** Recent work on self-improving AI through self-play (Singh et al., 2025) formalizes the keep-or-discard pattern as a Generator-Verifier-Updater operator, providing theoretical grounding for why Autoresearch's simple loop converges to better solutions[^7]
- **Community adoption (2025–2026):** The project has grown beyond its original H100 target, with active forks supporting Apple Silicon (MLX), AMD ROCm, and consumer GPUs. Several university ML courses now use Autoresearch as a teaching tool for autonomous experimentation
- **Safety considerations:** The AI Agent Index (2026) documents safety features across deployed agent systems, highlighting that Autoresearch's sandboxed single-file design is one of the safer autonomous research patterns — modifications are confined to `train.py` and easily auditable via git diff[^8]

## See Also

- [The AI Scientist](../core-concepts/the-ai-scientist.md)
- [AIDE](../tools-platforms/aide.md)
- [Automated Experiment Design](../methodologies/automated-experiment-design.md)
- [Open-Ended Discovery](../frontier-topics/open-ended-discovery.md)
- [Scaling Laws for Research Automation](../frontier-topics/scaling-laws-research.md) — how Autoresearch experiments compound according to scaling relationships
- [Recursive Self-Improvement](../frontier-topics/recursive-self-improvement.md) — the keep-or-discard loop as a minimal form of recursive improvement
- [Tracking AI Research](../research-sources/tracking-ai-research.md) — community forks and developments around Autoresearch

## References

[^1]: Karpathy, A. (2025). "Autoresearch." [github.com/karpathy/autoresearch](https://github.com/karpathy/autoresearch)

[^2]: Zoph, B. & Le, Q. (2017). "Neural Architecture Search with Reinforcement Learning." [arXiv:1611.01578](https://arxiv.org/abs/1611.01578)

[^3]: Clune, J. (2019). "AI-Generating Algorithms, an Alternate Paradigm for Producing General Artificial Intelligence." [arXiv:1905.10985](https://arxiv.org/abs/1905.10985)

[^4]: Jimenez, C. et al. (2024). "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?" [arXiv:2310.06770](https://arxiv.org/abs/2310.06770)

[^5]: Chen, Z. et al. (2025). "Agentic AI for Scientific Discovery: A Survey of Progress, Challenges, and Future Directions." [arXiv:2503.08979](https://arxiv.org/abs/2503.08979)

[^6]: Yu, X., Peng, B. & Galley, M. (2025). "Dyna-Mind: Learning to Simulate from Experience for Better AI Agents." [arXiv:2510.09577](https://arxiv.org/abs/2510.09577)

[^7]: Singh, A. et al. (2025). "Self-Improving AI Agents through Self-Play." [arXiv:2512.02731](https://arxiv.org/abs/2512.02731)

[^8]: Lam, M. et al. (2026). "The 2025 AI Agent Index: Documenting Technical and Safety Features of Deployed Agentic AI Systems." [arXiv:2602.17753](https://arxiv.org/abs/2602.17753)
