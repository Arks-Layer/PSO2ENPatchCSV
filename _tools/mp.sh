#!/bin/sh
#PYTHONIOENCODING=utf-8 xargs --max-procs 8 --no-run-if-empty $0
PYTHONIOENCODING=utf-8 LC_ALL="POSIX" parallel --no-notice --no-run-if-empty --keep-order --xargs -m $@
