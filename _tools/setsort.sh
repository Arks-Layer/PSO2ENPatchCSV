#!/bin/bash
while IFS=' ' read -r file dir
do
	echo mkdir -p $dir
	echo git mv -n $file $dir
done
