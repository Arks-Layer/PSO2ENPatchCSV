#!/bin/sh
set -eu
find . -type d -not -path "./.git/*"|tr '[:upper:]' '[:lower:]'|sort|uniq -d
