#!/bin/sh
for var in "$@"
do
	echo -n "-f $var "
done
