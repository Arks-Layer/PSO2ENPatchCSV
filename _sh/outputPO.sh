#!/bin/bash
PWDC="$(pwd -P)"
rm -rf /tmp/PSO2ENPatchCSV.outputPO
mkdir -p /tmp/PSO2ENPatchCSV.outputPO
JP="upstream/JP"
EN="upstream/EN"
rsync --recursive --executability --whole-file . /tmp/PSO2ENPatchCSV.outputPO/WC/ --exclude ".git" --del && cd /tmp/PSO2ENPatchCSV.outputPO/WC/Files && find .. -name "*.csv" -not -path "../Files/*" -print0|$PWDC/_tools/mp.sh -0 ln -s {} . \; &
git archive --format=tar --prefix=PSO2ENPatchCSV.outputPO/EN/ $EN | tar xf - -C /tmp && cd /tmp/PSO2ENPatchCSV.outputPO/EN/Files && find .. -name "*.csv" -not -path "../Files/*" -print0|$PWDC/_tools/mp.sh -0 ln -s {} . \; &
git archive --format=tar --prefix=PSO2ENPatchCSV.outputPO/JP/ $JP | tar xf - -C /tmp &
buildJP="$(git describe --always --tags $JP)"
buildEN="$(git describe --always --tags $EN)"
buildWC="$(git describe --always --tags)"
POTCommitID=`echo $buildWC | cut -f 1-2 -d -`
POTDate="$(git --no-pager show -s --format='%ad' --date=format:'%Y-%m-%d %H:%M:%S%z' $POTCommitID)"
PODate="$(git --no-pager show -s --format='%ad' --date=format:'%Y-%m-%d %H:%M:%S%z')"
LastTranslator="$(git --no-pager show -s --format='%an <%ae>')"
TagBranch="$(git describe --always --tags|cut -f 1 -d -|tr [A-Z] [a-z])"
echo \#, fuzzy
echo msgid \"\"
echo msgstr \"\"
echo \"Project-Id-Version: PSO2 CSV $buildJP	$buildEN	$buildWC\\n\"
echo \"Report-Msgid-Bugs-To: https://github.com/Arks-Layer/PSO2ENPatchCSV/issues\\n\"
echo \"POT-Creation-Date: $POTDate\\n\"
echo \"PO-Revision-Date: $PODate\\n\"
echo \"Last-Translator: $LastTranslator\\n\"
echo \"Language-Team: None\\n\"
echo \"Language: $TagBranch\\n\"
echo \"MIME-Version: 1.0\\n\"
echo \"Content-Type: text/plain\; charset=UTF-8\\n\"
echo \"Content-Transfer-Encoding: 8bit\\n\"
wait
cd /tmp/PSO2ENPatchCSV.outputPO/
find JP -name "*.csv" -print0|sort -z|WC/_tools/mp.sh -0 WC/_py/outputPO.py $TagBranch
