#!/bin/sh
tail -n +2|fgrep -e "&"|cut -f 2 -d " "|./_tools/sortuniq.sh
