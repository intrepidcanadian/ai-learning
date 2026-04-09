#!/bin/bash
# Wikipedia for AI Learning -- Cron Update Script
# Runs update_wiki.py with proper environment and logging
#
# This script is called by macOS cron (see `crontab -l` to view schedule).
# Cron runs only when the Mac is awake -- missed runs are skipped,
# but update_wiki.py fetches the last 3 days of papers each run so it catches up.
#
# Manage the cron schedule:
#   crontab -l                    # View current schedule
#   crontab -e                    # Edit schedule
#   crontab -r                    # Remove all cron jobs
#
# Example schedules:
#   0 * * * *    --> Every hour (current)
#   0 8 * * *    --> Daily at 8am
#   0 8,20 * * * --> Twice daily (8am and 8pm)
#
# Logs: data/cron.log (this wrapper) and data/update.log (detailed fetch log)
# Paper database: data/papers.json (dedup + history across runs)

WIKI_DIR="/Users/tony/Documents/wikipediaforlearning"
PYTHON="/Applications/Xcode.app/Contents/Developer/usr/bin/python3"
LOG_FILE="$WIKI_DIR/data/cron.log"

mkdir -p "$WIKI_DIR/data"

echo "────────────────────────────────────────" >> "$LOG_FILE"
echo "Cron run: $(date)" >> "$LOG_FILE"

cd "$WIKI_DIR" && $PYTHON update_wiki.py >> "$LOG_FILE" 2>&1

echo "Exit code: $?" >> "$LOG_FILE"
echo "" >> "$LOG_FILE"
