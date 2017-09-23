#/bin/sh
cat /tmp/dict.txt
find . -type f -name "*.csv" -not -path "*/Files/*.csv" -print0|_tools/mp.sh -0 fgrep -w -f /tmp/dict.txt
find . -maxdepth 1 -name "aspell.nofail"|egrep '.*' > /dev/null || exit `wc -l /tmp/dict.txt|cut -f1 --d " "`
