#!/bin/sh
# this assume outputPO.sh had ran
#_py/getDupLines.py /tmp/PSO2ENPatchCSV.outputPO/JP/ > /tmp/DupLines.json
#cat /tmp/DupLines.json |  jq -S 'def recursively(f): . as $in | if type == "object" then reduce keys[] as $key ( {}; . + { ($key): ($in[$key] |recursively(f)) } ) elif type == "array" then map( recursively(f) ) | f  else . end; recursively(sort)' > _misc/jp_dup.json
_py/checkDupLines.py . _misc/jp_dup.json
