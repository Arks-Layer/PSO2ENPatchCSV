#!/bin/sh
cp _aspell/PSO2.dict.BASE /tmp/PSO2.dict
sh -c "find . -name '*_name.csv' -or -name 'ui_charamake_parts.csv' -print0|xargs -0 python3 _py/aspell.py"|strings -n 2|sed -e 's/[ \t][ \t]*/\n/g' -e 's/\!//g' -e "s/'//g"|./_sh/sortuniq.sh|grep -v -E -f _aspell/reject.dict|strings -n 1 > /tmp/PSO2.dict.DYN
cat _aspell/PSO2.dict.BASE /tmp/PSO2.dict.DYN _aspell/PSO2.*.dict|strings -n 1 > /tmp/PSO2.dict
find . -name "*.csv" -not -name "smut_filter.csv" -not -name "*_BACKUP_*.csv" -not -name "*_BASE_*.csv" -not -name "*_REMOTE_*.csv" -print0|xargs -0 python3 _py/aspell.py|strings -n 1|aspell pipe --personal=/tmp/PSO2.dict --encoding utf-8 --lang=en|strings -n 2|fgrep -v -e "*"
#./aspell.sh |tee /tmp/PSO2_aspell.txt|sort|uniq --count|sort -n|2>/tmp/PSO2_aout.txt
