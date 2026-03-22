#!/bin/bash
set -euo pipefail

python3 - <<'PY'
import subprocess
import sys
from collections import Counter
from pathlib import Path

files = subprocess.check_output(["git", "ls-files"], text=True).splitlines()
names = [Path(path).name for path in files if path.endswith(".csv")]
counts = Counter(names)
dups = sorted(name for name, count in counts.items() if count > 1)

if dups:
    print("Found duplicate files")
    for name in dups:
        print(name)
    sys.exit(1)
PY
