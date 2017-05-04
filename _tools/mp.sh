#!/bin/sh
xargs -P 0 -n 128 -s 2048 $@
