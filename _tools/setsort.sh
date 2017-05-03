#!/bin/sh
while IFS=' ' read -r file dir
do
	newdir=`echo $dir|sed "s/\"//g"`
	if [ ! -d "$newdir" ]; then
		echo "Making directory " $newdir
		mkdir -p "$newdir"
	fi
	newfile=`find  . -not -path "./Files/*" -not -path "*/.git/*" -name "$file"`
	if [ ! -z "$newfile" ]; then
		echo "Moving $newfile to $newdir"
		#git mv -f $newfile "$newdir" 2>/dev/null
	fi
done
