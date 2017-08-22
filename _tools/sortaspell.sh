#!/bin/sh
fgrep -e "&"|cut -f 2 -d " "|./_tools/sortuniq.sh
