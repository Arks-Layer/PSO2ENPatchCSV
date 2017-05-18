#!/bin/sh
#xargs --max-procs 8 --no-run-if-empty $0
parallel --no-run-if-empty --keep-order --progress --xargs -m $@
