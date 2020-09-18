#!/bin/bash
set -euo pipefail
rm -rf /tmp/BOM.stderr
find . -name "*.csv" -not -path "*/Files/*" -not -path "*/.git/*" -print0|_tools/mp.sh --no-keep-order -0 ./_py/BOM.py
