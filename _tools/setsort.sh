#!/bin/sh
while IFS=' ' read -r file dir
do
	mkdir -p $dir
	newfile=`find  . -name "*.csv" -not -path "../Files/*" -not -path "*/.git/*" -name "$file"`
	git mv $newfile $dir
done
