#!/bin/bash
set -euo pipefail
find . -name "*.csv" -not -path "*/Files/*" -not -path "*/.git/*" -print0|_tools/mp.sh -0 _py/quote.py
