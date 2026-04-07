# AIDE: AI-Driven Exploration

**AIDE** (AI-Driven Exploration) is a system for automated machine learning experimentation that explores the space of possible solutions through code generation. It represents a code-centric approach to ML research automation, where the search space is defined by all possible Python programs that solve a given task.

**Paper:** Jiang, Z. et al. (2025). "AIDE: AI-driven exploration in the space of code." [arXiv:2502.13138](https://arxiv.org/abs/2502.13138)

## Overview

Unlike traditional AutoML systems that search over predefined hyperparameter spaces, AIDE treats the entire code space as its search domain. An LLM generates, modifies, and evaluates complete Python scripts, using the results of each run to inform the next iteration.

## Background / Theoretical Foundations

AIDE builds on the insight that **programs are a more expressive search space than hyperparameters** [^1]. Traditional AutoML (Feurer et al., 2015) searches over predefined configurations — architecture choices, learning rates, regularization strengths [^3]. AIDE generalizes this: any change expressible in Python is a valid search step.

This connects to program synthesis research, where the goal is generating programs that satisfy a specification [^4]. In AIDE's case, the "specification" is a performance metric, and the "synthesizer" is an LLM that understands both code and ML. The key advance is using execution feedback (actual training results) to guide synthesis, rather than relying solely on the LLM's prior knowledge.

**Learning application**: AIDE demonstrates a powerful study strategy for ML practitioners. Rather than manually tweaking hyperparameters, frame your experiments as a search problem: define a clear metric, generate candidate solutions, evaluate them, and let the results guide your next move. AIDE automates this, but the same structured approach improves manual experimentation.

## How It Works

1. **Problem specification** -- User provides a task description and evaluation metric
2. **Initial solution generation** -- LLM generates a complete Python script as a starting point
3. **Iterative refinement** -- The system repeatedly:
   - Analyzes current results and error messages
   - Proposes modifications to the code
   - Executes the modified script
   - Evaluates performance against the metric
4. **Solution selection** -- The best-performing script is returned

## Comparison with Related Systems

| System | Search Space | Output | Human Input |
|--------|-------------|--------|-------------|
| AIDE | All Python programs | Best script | Task description |
| [Autoresearch](../tools-platforms/autoresearch.md) | Modifications to `train.py` | Improved model | `program.md` |
| [The AI Scientist](../core-concepts/the-ai-scientist.md) | Research ideas + code | Full paper | Research subfield |
| Traditional AutoML | Hyperparameter grid | Best config | Pipeline definition |

## Key Design Principles

- **Code is the search space** -- Rather than searching over configurations, AIDE searches over programs
- **LLM as the search algorithm** -- The language model's understanding of code and ML serves as the heuristic
- **Execution feedback** -- Actual run results (metrics, errors, outputs) guide the search
- **Minimal human specification** -- Users describe *what* they want, not *how* to achieve it

## Connection to MLAgentBench

AIDE was evaluated on **MLAgentBench** (Huang et al., 2024), a benchmark for evaluating language agents on ML experimentation tasks[^2]. MLAgentBench provides standardized ML tasks with defined metrics, enabling comparison of different automated research approaches.

### MLE-Bench Results

On the more recent MLE-bench (Chan et al., 2025), AIDE demonstrated strong performance across Kaggle-style ML tasks[^5]:

| Agent | Tasks Solved (%) | Median Rank |
|-------|-----------------|-------------|
| AIDE | 16.9% | Top 37% |
| OpenHands | 11.0% | Top 44% |
| MLAB baseline | 8.7% | Top 52% |

These results establish AIDE as one of the strongest automated ML engineering agents available, approaching the skill level of mid-tier Kaggle competitors.

## Significance

AIDE demonstrates that LLMs can serve as effective search algorithms in program space -- a much richer search domain than traditional hyperparameter grids. This approach complements:
- [Agentic Tree Search](../methodologies/agentic-tree-search.md) -- Used by The AI Scientist for structured exploration
- [Autoresearch](../tools-platforms/autoresearch.md) -- Similar autonomous loop but with a fixed single-file constraint

## Current State / Latest Developments

As of 2026, AIDE has evolved significantly since its initial release:

- **Kaggle competition performance**: AIDE achieved top-10% performance on multiple Kaggle competitions autonomously, demonstrating that LLM-guided code search can compete with experienced human data scientists[^1]. On the MLE-bench (Machine Learning Engineering Benchmark), AIDE solved 16.9% of tasks compared to 8.7% for baseline agents[^5].

- **Multi-model integration**: Recent versions support multiple LLM backends (GPT-4o, Claude Sonnet 4, DeepSeek-R1), allowing users to choose the best model for their compute budget and task complexity[^1].

- **Tree-structured exploration**: AIDE now implements a tree-structured search similar to [Agentic Tree Search](../methodologies/agentic-tree-search.md), maintaining multiple solution branches and selecting the most promising ones for further refinement[^5].

- **Application to learning**: AIDE's approach has implications for AI-powered education. By treating solution-finding as a search problem with execution feedback, it demonstrates how AI tutors could explore multiple explanation strategies for a student, evaluating each approach's effectiveness before settling on the best one. This mirrors how effective human tutors adapt their teaching style based on student responses.

## Limitations / Challenges

- **High variance**: Because the search space is all programs, results can vary significantly across runs — a lucky initial generation may find a great solution, while an unlucky one may explore unproductive regions.
- **Compute cost**: Each iteration requires executing a full training script. For expensive training tasks, this limits the number of search steps feasible in a given time budget.
- **Interpretability**: When AIDE finds a good solution, understanding *why* it works can be difficult if the generated code is complex or unconventional.
- **Task specification sensitivity**: Performance depends heavily on how clearly the task and metric are described — vague specifications lead to poor solutions[^1].

## See Also

- [Autoresearch](../tools-platforms/autoresearch.md) — similar autonomous loop with single-file constraint
- [The AI Scientist](../core-concepts/the-ai-scientist.md) — full research automation pipeline
- [Automated Experiment Design](../methodologies/automated-experiment-design.md) — the methodology AIDE instantiates
- [Agentic Tree Search](../methodologies/agentic-tree-search.md) — structured exploration strategy used by The AI Scientist
- [Recursive Self-Improvement](../frontier-topics/recursive-self-improvement.md) — AIDE's iterative refinement as a form of self-improvement
- [Scaling Laws for Research Automation](../frontier-topics/scaling-laws-research.md) — how AIDE performance scales with iterations
- [Tracking AI Research](../research-sources/tracking-ai-research.md) — monitoring AIDE-style tools in the research landscape

## References

[^1]: Jiang, Z. et al. (2025). "AIDE: AI-driven exploration in the space of code." [arXiv:2502.13138](https://arxiv.org/abs/2502.13138)

[^2]: Huang, Q. et al. (2024). "MLAgentBench: evaluating language agents on machine learning experimentation." *ICML*, 235, 20271--20309.

[^3]: Feurer, M. et al. (2015). "Efficient and Robust Automated Machine Learning." *NeurIPS*, 28. [arXiv:1507.05444](https://arxiv.org/abs/1507.05444)

[^4]: Gulwani, S. et al. (2017). "Program Synthesis." *Foundations and Trends in Programming Languages*, 4(1-2), 1-119.

[^5]: Chan, J. et al. (2025). "MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering." [arXiv:2410.07095](https://arxiv.org/abs/2410.07095)
