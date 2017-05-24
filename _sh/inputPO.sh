#!/bin/bash
find . -name "*.csv" -not -path "./.git/*" -print0|./_tools/mp.sh -0 -- ./_py/inputPO.py $1
find . -name "*.csv" -not -path "./.git/*" -print0|./_tools/mp.sh -0 -- dos2unix -k -q --
