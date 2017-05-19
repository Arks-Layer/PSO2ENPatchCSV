#!/bin/sh
#xargs --max-procs 8 --no-run-if-empty $0
LC_ALL="POSIX" parallel --will-cite --no-run-if-empty --keep-order --progress --xargs -m $@
