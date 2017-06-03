#!/bin/sh
rm -rf /tmp/PSO2ENPatchCSV.outputPO
git archive --format=tar --prefix=PSO2ENPatchCSV.outputPO/JP/ upstream/JP | tar xf - -C /tmp
git archive --format=tar --prefix=PSO2ENPatchCSV.outputPO/EN/ upstream/EN | tar xf - -C /tmp
rsync -a . /tmp/PSO2ENPatchCSV.outputPO/WC/ --exclude ".git" --del
buildJP="$(git describe --always --tags upstream/JP)"
buildEN="$(git describe --always --tags upstream/EN)"
buildWC="$(git describe --always --tags)"
POTCommitID=`echo $buildWC | cut -f 1-2 -d -`
POTDate="$(git --no-pager show -s --format='%ad' --date=format:'%Y-%m-%d %H:%M:%S%z' $POTCommitID)"
PODate="$(git --no-pager show -s --format='%ad' --date=format:'%Y-%m-%d %H:%M:%S%z')"
LastTranslator="$(git --no-pager show -s --format='%an <%ae>')"
TagBranch="$(git describe --always --tags|cut -f 1 -d -|tr [A-Z] [a-z])"
cd /tmp/PSO2ENPatchCSV.outputPO/WC/Files
find .. -name "*.csv" -not -path "../Files/*" -print0|../../WC/_tools/mp.sh -0 ln -s {} . \;
cd /tmp/PSO2ENPatchCSV.outputPO/EN/Files
find .. -name "*.csv" -not -path "../Files/*" -print0|../../WC/_tools/mp.sh -0 ln -s {} . \;
cd /tmp/PSO2ENPatchCSV.outputPO/
echo \#, fuzzy
echo msgid \"\"
echo msgstr \"\"
echo \"Project-Id-Version: PSO2 CSV $buildJP	$buildEN	$buildWC\\\\n\"
echo \"Report-Msgid-Bugs-To: https://github.com/Arks-Layer/PSO2ENPatchCSV/issues\\\\n\"
echo \"POT-Creation-Date: $POTDate\\\\n\"
echo \"PO-Revision-Date: $PODate\\\\n\"
echo \"Last-Translator: $LastTranslator\\\\n\"
echo \"Language-Team: None\\\\n\"
echo \"Language: $TagBranch\\\\n\"
echo \"MIME-Version: 1.0\\\\n\"
echo \"Content-Type: text/plain\; charset=UTF-8\\\\n\"
echo \"Content-Transfer-Encoding: 8bit\\\\n\"
find JP -name "*.csv" -print0|sort -z|WC/_tools/mp.sh -0 WC/_py/outputPO.py $TagBranch
