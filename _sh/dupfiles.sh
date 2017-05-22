#!/bin/sh
dups=$(find . -maxdepth 1 -type d -not -name "Files" -not -path "*/.git" -not -path "*/_*" -not -path "." -print0|./_tools/mp.sh -I{} -0 find {} -type f -print0|./_tools/mp.sh -0 basename -a | xargs -I{} find Files -name "{}"|xargs basename -a| ./_tools/mp.sh -n 1 -I{} echo "{}\n")
if [ -n "$dups" ]; then
	printf "duplicate files founds in File folder\n "
	echo $dups
	exit 1
fi
