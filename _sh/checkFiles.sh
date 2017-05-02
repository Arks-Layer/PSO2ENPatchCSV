#!/bin/sh
find . -path "./Files/*" -print0|xargs -P 0 -n 1024 -0 git diff --exit-code origin/JP --
