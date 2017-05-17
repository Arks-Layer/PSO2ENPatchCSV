#!/bin/bash
rm -rf /tmp/UTF8.stderr
find . -name "*.csv" -not -path "*/Files/*" -not -path "*/.git/*" -print0|_tools/mp.sh -0 ./_py/UTF8.py > /tmp/UTF8.stdout
if [ -s /tmp/UTF8.stdout ]; then
	cat /tmp/UTF8.stdout
	exit 1
fi
