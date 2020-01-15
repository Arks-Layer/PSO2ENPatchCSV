#!/bin/bash
set -euo pipefail
git ls-tree -r --name-only upstream/JP -z -- Files > /tmp/Moved.lst
find . -mindepth 1 -maxdepth 1 -type d -not -path "./Files*" -not -path "./_*" -not -path "./.*"  -print0 >> /tmp/Moved.lst
xargs --arg-file=/tmp/Moved.lst --null git diff --name-status --find-renames=100% --diff-filter=R --exit-code upstream/JP --
