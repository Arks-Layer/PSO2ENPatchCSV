#!/bin/bash
LANG=fr
cp _aspell/PSO2.dict.BASE /tmp/PSO2.dict
sh -c "find . -name '*_name.csv' -or -name 'ui_charamake_parts.csv' -print0|PYTHONIOENCODING=utf-8 _tools/mp.sh -0 _py/aspell.py"|sed -e 's/[ \t][ \t]*/\n/g' -e 's/\!//g' -e "s/'//g"|./_tools/sortuniq.sh|grep -v -E -f _aspell/reject.dict|strings -n 1 > /tmp/PSO2.dict.DYN
cat _aspell/PSO2.dict.BASE /tmp/PSO2.dict.DYN _aspell/PSO2.*.dict|strings -n 1 > /tmp/PSO2.dict
find . -name "*.csv" -not -name "smut_filter.csv" -not -name "*_BACKUP_*.csv" -not -name "*_BASE_*.csv" -not -name "*_REMOTE_*.csv" -not -path "*/.git/*" -print0|PYTHONIOENCODING=utf-8 _tools/mp.sh -0 _py/aspell.py|strings -n 2|aspell pipe --personal=/tmp/PSO2.dict --mode=none --encoding utf-8 --lang=$LANG|strings -n 2|fgrep -v -e "*"
