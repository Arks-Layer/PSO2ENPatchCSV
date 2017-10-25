#!/bin/sh
find . -name "*.csv" -not -path "*/Files/*" -not -path "*/Files.TODO/*" -print0|xargs -0 -n 10000 -I '{}' git mv '{}' Files
_tools/TODO.sh
_tools/getsort.sh HEAD|_tools/setsort.sh
