#!/bin/sh
find . -path "./Files/*" -print0|xargs -0 git diff --exit-code origin/JP --
