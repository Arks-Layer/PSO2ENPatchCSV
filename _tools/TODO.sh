#/bin/sh
mkdir -p Files.TODO
find . -path "./Files/*" -print0|_tools/mp.sh -0 git diff --name-status --exit-code upstream/JP --|sed -e "s/M\t//g" -e "s/A\t//g"|_tools/mp.sh -j1 -- git mv {} Files.TODO
