#!/bin/sh
find . -type f -name "*.csv" -print0|_tools/mp.sh -0 basename -a -z|sort -z|uniq -d -z|xargs -0 -n1 echo>/tmp/dups.stdout
if [ -s /tmp/dups.stdout ]; then
	echo Found duplicate files
	cat /tmp/dups.stdout
	exit 1
fi
