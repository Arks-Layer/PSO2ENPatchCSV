#!/bin/sh
set -euo pipefail
find . -type d -not -path "./.git/*"|tr '[:upper:]' '[:lower:]'|sort|uniq -d
