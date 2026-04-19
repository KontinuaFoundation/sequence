#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR/../Chapters"

: > book_00.txt
for i in $(seq -w 1 36); do
  cat "book_$i.txt" >> book_00.txt
done
