#!/bin/sh
git diff --name-only --find-renames=100% --find-copies=100% --diff-filter=R upstream/JP -z -- |xargs --null -I % git mv % Files/
