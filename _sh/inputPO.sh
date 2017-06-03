#!/bin/bash
if [ "$#" -gt "0" ]; then
	find . -name "*.csv" -not -path "./.git/*" -not -path "./Files/*" -print0|./_tools/mp.sh -0 -- ./_py/inputPO.py $1
	find . -name "*.csv" -not -path "./.git/*" -not -path "./Files/*" -print0|./_tools/mp.sh -0 -- dos2unix -k -q --
fi
if [ "$#" -gt "1" ]; then
	find Files -name "*.csv" -not -path "./.git/*" -print0|./_tools/mp.sh -0 -- ./_py/inputPO.py $1
	find Files -name "*.csv" -not -path "./.git/*" -print0|./_tools/mp.sh -0 -- dos2unix -k -q --
	_tools/TODO.sh
fi
