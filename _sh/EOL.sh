#!/bin/bash
find . -name "*.csv" -not -path "*/Files/*" -not -path "*/.git/*" -print0|_tools/mp.sh -0 ./_py/EOL.py > /tmp/EOL.stdout
if [ -s /tmp/EOL.stdout ]; then
	cat /tmp/EOL.stdout
	exit 1
fi
