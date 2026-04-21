#!/bin/bash
set -euo pipefail
find . -path "./Files/*.csv" ! -path "./Files/load_banner_large_04.csv" -print0|_tools/mp.sh --no-keep-order -0 git diff --name-status --diff-filter=M --exit-code upstream/JP --;( exit ${PIPESTATUS[1]} )
