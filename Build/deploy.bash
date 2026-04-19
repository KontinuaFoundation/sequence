#!/usr/bin/env bash
# Expected layout:
#   GitHub/
#     sequence/Build/<this script>
#     kontinuafoundation.github.io/
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR/../../"

# Mirror generated site assets (overwrites, skips unchanged, adds new).
rsync -av sequence/Build/Resources-en_US/ kontinuafoundation.github.io/kontinua-site/public

cd kontinuafoundation.github.io
if [ -n "$(git status --porcelain)" ]; then
  git add -A
  git commit -m "Deploy site: $(date -u +"%Y-%m-%d %H:%M:%SZ")"
  git push origin main
else
  echo "No changes to deploy."
fi
