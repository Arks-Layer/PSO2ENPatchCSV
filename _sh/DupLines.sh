#!/bin/sh
# this assume outputPO.sh had ran
_py/getDupLines.py /tmp/PSO2ENPatchCSV.outputPO/JP/ > /tmp/DupLines.json
_py/checkDupLines.py . /tmp/DupLines.json
