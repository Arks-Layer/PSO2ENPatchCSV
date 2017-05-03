#!/bin/sh
sort|uniq -c|sed 's/^[[:space:]]*//g'|sort -h -r|cut -f 2 -d " "|sed 's/[[:space:]]//g'
