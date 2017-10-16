#!/bin/sh
#Things to do when a new JP build is up
_py/DupLines_Make.py . |  jq -S 'def recursively(f): . as $in | if type == "object" then reduce keys[] as $key ( {}; . + { ($key): ($in[$key] |recursively(f)) } ) elif type == "array" then map( recursively(f) ) | f  else . end; recursively(sort)' > _misc/jp_dup.json
