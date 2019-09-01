#!/bin/bash
set -euo pipefail
find . -path "./Files/*" -print0|_tools/mp.sh --no-keep-order -0 git diff --name-status --exit-code upstream/JP --|sed -e "s/M\t//g";( exit ${PIPESTATUS[1]} )
