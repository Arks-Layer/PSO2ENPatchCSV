#!/bin/sh
#xargs --max-procs 8 --no-run-if-empty $0
LC_ALL="POSIX" parallel --no-notice --no-run-if-empty --keep-order --xargs -m $@
