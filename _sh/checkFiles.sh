#!/bin/sh
find . -path "./Files/*" -print0|_tools/mp.sh -0 git diff --exit-code origin/JP --
