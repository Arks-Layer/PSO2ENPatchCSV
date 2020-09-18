#!/bin/bash
set -euo pipefail
find . -name "*.csv" -not -path "*/Files/*" -not -path "*/.git/*" -not -size 0c -print0|_tools/mp.sh -0 ./_py/EOL.py > /tmp/EOL.stdout
if [ -s /tmp/EOL.stdout ]; then
	cat /tmp/EOL.stdout
	exit 1
fi
