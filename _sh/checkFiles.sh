#!/bin/bash
find . -path "./Files/*" -print0|_tools/mp.sh -0 git diff --name-status --exit-code upstream/JP --|sed -e "s/M\t//g";( exit ${PIPESTATUS[1]} )
