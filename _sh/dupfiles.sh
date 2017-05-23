#!/bin/sh
find . -type f -not -path "*/.git" -not -path "*/_*" -name "*.csv" -print0|_tools/mp.sh -0 basename -a|uniq -d -i|>/tmp/dups.stdout
if [ -s /tmp/dups.stdout ]; then
	echo Found duplicate files
	cat /tmp/dups.stdout
	exit 1
fi
