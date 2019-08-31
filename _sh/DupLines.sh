#!/bin/sh
set -eu
PYTHONIOENCODING=utf-8 _py/DupLines_Filter.py . _misc/jp_dup.json > /tmp/filter.json
PYTHONIOENCODING=utf-8 _py/DupLines_Vaules.py . /tmp/filter.json|jq -S .
