#!/bin/sh
if [ "$#" -ne 1 ]; then
	basedir=""
else
	basedir="$1"
fi
while IFS=' ' read -r file dir
do
	newdir=`echo $dir|sed "s/\"//g"`
	if [ ! -d "$basedir$newdir" ]; then
		#echo "Making directory $newdir"
		mkdir -p "$basdir$newdir"
	fi
	newfile=`find  . -not -path "./Files/*" -not -path "*/.git/*" -name "$file"`
	if [ ! -z "$newfile" ]; then
		#echo "Moving $newfile to $newdir"
		git mv -f $newfile "$basedir$newdir" 2>/dev/null
	fi
done
