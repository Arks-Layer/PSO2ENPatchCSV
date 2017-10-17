#!/bin/sh
 _py/DupLines_Filter.py .  _misc/jp_dup.json > /tmp/filter.json
 _py/DupLines_Vaules.py .  /tmp/filter.json  > /tmp/values.json
 _py/DupLines_Replace.py . /tmp/values.json  /tmp/filter.json
 _tools/TODO.sh
_py/DupLines_Filter.py .  _misc/jp_dup.json | jq -S 'def recursively(f): . as $in | if type == "object" then reduce keys[] as $key ( {}; . + { ($key): ($in[$key] |recursively(f)) } ) elif type == "array" then map( recursively(f) ) | f  else . end; recursively(sort)'
