#!/bin/sh
cat PSO2.dict.BASE>/tmp/PSO2.dict
find . -name "*_name.csv" -name "ui_charamake_parts.csv" -print0|xargs -0 python3 aspell.py|strings -n 2|sed -e 's/[ \t][ \t]*/\
/g' -e 's/\!//g' -e "s/'//g"|uniq|grep -v -e "weather0" -e "poka1" -e "poka2" -e "Ship0" -e "Ship1" -e "Self0" -e "PSO2es" -e "PSO2" -e "0%">>/tmp/PSO2.dict
cat PSO2.*.dict >> /tmp/PSO2.dict
find . -name "*.csv" -not -name "smut_filter.csv" -not -name "*_BACKUP_*.csv" -not -name "*_BASE_*.csv" -not -name "*_REMOTE_*.csv" -print0|xargs -0 python3 aspell.py|strings -n 1|aspell pipe --personal=/tmp/PSO2.dict --encoding utf-8 2>/dev/null|strings -n 2|fgrep -v -e "*"
#./aspell.sh |tee /tmp/PSO2_aspell.txt|sort|uniq --count|sort -n|2>/tmp/PSO2_aout.txt
