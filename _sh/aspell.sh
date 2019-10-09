#!/bin/bash
set -uo pipefail
LANGDICT=en
cp _aspell/PSO2.dict.BASE /tmp/PSO2.dict
PYTHONIOENCODING=utf-8 find . -name '*_name.csv' -or -name 'ui_charamake_parts.csv' -print0|xargs -0 _py/aspell.py|sort|uniq|grep -v -E -f _aspell/reject.dict|sed -f _aspell/reject.sed|_py/stripCJK.py|strings -n 2 -e S > /tmp/PSO2.dict.DYN
cat /tmp/PSO2.dict.DYN _aspell/PSO2.*.dict|strings -n 2 -e S|sort|uniq|_py/stripCJK.py|sed -f _aspell/reject.sed|strings -n 2 -e S >> /tmp/PSO2.dict
if [ -e aspell.disabled ]; then
	echo Spell Checking disabled
	exit 0
fi
PYTHONIOENCODING=utf-8 find . -name "*.csv" -not -name "smut_filter.csv" -not -name "*_BACKUP_*.csv" -not -name "*_BASE_*.csv" -not -name "*_REMOTE_*.csv" -not -path "./.git/*" -not -path "./Files/*" -not -name "oa_tanabata.csv" -print0|xargs -0 _py/aspell.py|_py/filtercmd.py|tee /dev/null|strings -n 2 -e S|tee /tmp/strings.txt|_tools/mp.sh --round-robin --pipe aspell pipe --personal=/tmp/PSO2.dict --mode=none --encoding utf-8 --lang=$LANGDICT|strings -n 2 -e S|fgrep -v -e "*" -e "spell "
rc=$?
if [ -e aspell.warning ]; then
	if [ $rc -ne 0 ]; then
		exit 0
	exit 1
	fi
fi
exit 0
