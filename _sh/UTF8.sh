#!/bin/bash
rm -rf /tmp/UTF8.stderr
find . -name "*.csv" -not -path "*/Files/*" -not -path "*/.git/*" -print0|_tools/mp.sh -0 ./_py/UTF8.py 2> /tmp/UTF8.stderr
if [ -s /tmp/UTF8.stderr ]; then
	cat /tmp/UTF8.stderr
	exit 1
fi
