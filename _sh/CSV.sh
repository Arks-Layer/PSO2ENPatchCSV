#!/bin/bash
set -euo pipefail
find . -name "*.csv" -not -path "*/Files/*" -not -path "*/.git/*" -print0|_tools/mp.sh --no-keep-order -0 _py/CSV.py
