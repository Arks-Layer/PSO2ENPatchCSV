#!/bin/sh
find . -name "*.csv" -not -path "./.git/*" -not -path "./Files/*" -print0|_tools/mp.sh -0 _py/dupCSV.py
