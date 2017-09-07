#!/bin/sh
_py/getDupLines.py . > /tmp/DupLines.json
_py/checkDupLines.py . /tmp/DupLines.json
