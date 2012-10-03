if [ -z "$CM_BUILD" ]; then
  ## Use jenkins' variable
  CM_BUILD=$LUNCH
fi

MYPATH=$(dirname $0)
rm $WORKSPACE/archive/CHANGES.txt 2>/dev/null

prevts=
for ts in `python2 $MYPATH/getdates.py $CM_BUILD`; do

export ts
(echo "============================="
date -d @$ts 
echo "============================="
if [ -z "$prevts" ]; then
  repo forall -c 'L=$(git log --oneline --no-merges --since $ts -n 1); if [ "n$L" != "n" ]; then echo -e "\n   * $REPO_PATH\n"; git log --oneline --no-merges --since $ts; echo; fi'
else
  repo forall -c 'L=$(git log --oneline --no-merges --since $ts --until $prevts -n 1); if [ "n$L" != "n" ]; then echo -e "\n   * $REPO_PATH\n"; git log --oneline --no-merges --since $ts --until $prevts; echo; fi'
fi
echo "============================="
echo) >> $WORKSPACE/archive/CHANGES.txt
export prevts=$ts

done
