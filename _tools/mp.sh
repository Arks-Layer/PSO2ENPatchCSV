#!/bin/sh
xargs -P 0 -n 200 -s 4096 $@
