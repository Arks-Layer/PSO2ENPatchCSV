#!/bin/sh
if [ "$#" -ne 1 ]; then
	basedir="."
else
	basedir="$1"
fi
while IFS=' ' read -r file dir
do
	newdir=`echo $dir|sed "s/\"//g"`
	if [ ! -d "$basedir/$newdir" ]; then
		echo "Making directory $newdir"
		mkdir -p "$basedir/$newdir"
	fi
	oldfile=`find  . -not -path "./Files/*" -not -path "*/.git/*" -name "$file"`
	#echo "$basedir/$newdir/$file"
	if [ ! -z "$oldfile" ] && [ ! -e "$basedir/$newdir/$file" ]
	then
		#echo "$basedir/$newdir/$basefile"
		echo "Moving $file to $basedir/$newdir"
		git mv -f "$oldfile" "$basedir/$newdir/"
	fi
done
