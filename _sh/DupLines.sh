#!/bin/sh
_py/DupLines_Filter.py . _misc/jp_dup.json|jq -S .
