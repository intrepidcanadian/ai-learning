#!/bin/bash
# Wikipedia for AI Learning -- Self-Improving Loop
#
# Each iteration:
#   1. Benchmark current state
#   2. Claude Code writes a hypothesis (what to change, predicted score delta)
#   3. Claude Code makes the edit
#   4. Re-benchmark to measure actual delta
#   5. Log the experiment (hypothesis vs reality)
#
# Over time, the experiment log teaches the loop which strategies work.
#
# Usage:
#   ./improve_loop.sh          # 3 iterations
#   ./improve_loop.sh 5        # 5 iterations
#   ./improve_loop.sh 1        # single pass

WIKI_DIR="$(cd "$(dirname "$0")" && pwd)"
ITERATIONS="${1:-3}"
EXPERIMENTS_DIR="$WIKI_DIR/data/experiments"

cd "$WIKI_DIR"
mkdir -p "$EXPERIMENTS_DIR"

for i in $(seq 1 "$ITERATIONS"); do
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "  ITERATION $i / $ITERATIONS"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""

    TIMESTAMP=$(date +%Y-%m-%d_%H%M%S)
    EXPERIMENT_FILE="$EXPERIMENTS_DIR/${TIMESTAMP}.json"

    # Step 1: Benchmark (before)
    echo "Running pre-edit benchmark..."
    SCORES_BEFORE=$(python3 benchmark_wiki.py 2>&1)
    echo "$SCORES_BEFORE"

    # Extract lowest scoring article
    LOWEST=$(echo "$SCORES_BEFORE" | grep "Lowest scoring:" | sed 's/.*Lowest scoring: //')
    if [ -z "$LOWEST" ]; then
        echo "Could not determine lowest scoring article. Stopping."
        exit 1
    fi

    # Collect past experiment summaries for context
    PAST_EXPERIMENTS=""
    for exp in $(ls -t "$EXPERIMENTS_DIR"/*.json 2>/dev/null | head -10); do
        PAST_EXPERIMENTS="$PAST_EXPERIMENTS
$(python3 -c "
import json, sys
with open('$exp') as f:
    e = json.load(f)
h = e.get('hypothesis', {})
r = e.get('result', {})
print(f\"- [{e.get('article','')}] Strategy: {h.get('strategy','')} | Predicted: +{h.get('predicted_delta',0)} | Actual: {r.get('actual_delta','?')} | Worked: {r.get('improved','?')}\")
" 2>/dev/null)"
    done

    echo ""
    echo "→ Target: $LOWEST"
    echo ""

    # Step 2: Claude Code hypothesizes + edits
    claude -p "You are improving a wiki through an experiment-driven loop.

## Your task
1. Read the benchmark output and past experiments below.
2. Write a hypothesis to data/experiments/${TIMESTAMP}.json BEFORE editing. The hypothesis must include:
   - article: which article you're editing
   - strategy: what you plan to do (1 sentence)
   - predicted_delta: how many composite points you expect to gain (number)
   - dimensions_targeted: which score dimensions this should improve (list)
   - reasoning: why you think this will work, informed by past experiments
3. Edit the article ($LOWEST) to execute your strategy. Follow CLAUDE.md rules.
4. After editing, run python3 benchmark_wiki.py to get the new score.
5. Update data/experiments/${TIMESTAMP}.json with the result:
   - score_before: composite before your edit
   - score_after: composite after your edit
   - actual_delta: score_after - score_before
   - improved: true/false
   - lesson: what you learned (1 sentence)

Write the hypothesis JSON like this:
{
  \"timestamp\": \"${TIMESTAMP}\",
  \"iteration\": $i,
  \"article\": \"$LOWEST\",
  \"hypothesis\": {
    \"strategy\": \"...\",
    \"predicted_delta\": 0,
    \"dimensions_targeted\": [],
    \"reasoning\": \"...\"
  },
  \"result\": {
    \"score_before\": 0,
    \"score_after\": 0,
    \"actual_delta\": 0,
    \"improved\": false,
    \"lesson\": \"...\"
  }
}

## Past experiments (learn from these)
${PAST_EXPERIMENTS:-No past experiments yet. This is the first run.}

## Current benchmark
$SCORES_BEFORE"

    # Step 3: Re-benchmark (updates trend page) and rebuild HTML
    echo "Re-benchmarking and rebuilding wiki..."
    python3 benchmark_wiki.py
    python3 build.py

    # Step 4: Log result summary
    if [ -f "$EXPERIMENT_FILE" ]; then
        echo ""
        echo "Experiment logged:"
        python3 -c "
import json
with open('$EXPERIMENT_FILE') as f:
    e = json.load(f)
h = e.get('hypothesis', {})
r = e.get('result', {})
print(f\"  Strategy: {h.get('strategy', 'unknown')}\")
print(f\"  Predicted: +{h.get('predicted_delta', '?')}  Actual: {r.get('actual_delta', '?')}\")
print(f\"  Improved: {r.get('improved', '?')}\")
print(f\"  Lesson: {r.get('lesson', 'none logged')}\")
" 2>/dev/null
    else
        echo "  (No experiment file written)"
    fi

    echo ""
    echo "Iteration $i complete."
done

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  FINAL RESULTS"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
python3 benchmark_wiki.py --history
python3 benchmark_wiki.py --diff

echo ""
echo "Experiment log:"
for exp in $(ls -t "$EXPERIMENTS_DIR"/*.json 2>/dev/null | head -10); do
    python3 -c "
import json
with open('$exp') as f:
    e = json.load(f)
h = e.get('hypothesis', {})
r = e.get('result', {})
print(f\"  [{e.get('timestamp','')}] {e.get('article','')}: {h.get('strategy','')} → delta={r.get('actual_delta','?')} ({'✓' if r.get('improved') else '✗'})\")
" 2>/dev/null
done
