#!/bin/bash
rm /tmp/BOM.stderr
find . -name "*.csv" -not -path "*/Files/*" -not -path "*/.git/*" -print0|xargs -0 ./_py/BOM.py 2> /tmp/BOM.stderr
if [ -s /tmp/BOM.stderr ]; then
	cat /tmp/BOM.stderr
	exit 1
fi
