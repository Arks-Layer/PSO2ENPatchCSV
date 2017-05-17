#!/bin/bash
rm -rf /tmp/BOM.stderr
find . -name "*.csv" -not -path "*/Files/*" -not -path "*/.git/*" -print0|_tools/mp.sh -0 ./_py/BOM.py > /tmp/BOM.stdout
if [ -s /tmp/BOM.stdout ]; then
	cat /tmp/BOM.stdout
	exit 1
fi
