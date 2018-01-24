#!/bin/sh
_sh/outputPO.sh > tmp.po
_sh/inputPO.sh tmp.po
git add -u
find . -name "*.csv" -not -path "*/Files/*" -print0 | _tools/mp.sh -0 -j1 --no-keep-order -- git mv {} Files
_tools/TODO.sh
_tools/getsort.sh HEAD | _tools/setsort.sh > /dev/null
git status --untracked-files=no
