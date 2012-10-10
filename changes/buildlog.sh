if [ -z "$CM_BUILD" ]; then
  ## Use jenkins' variable
  CM_BUILD=$LUNCH
fi

MYPATH=$(dirname $0)
export CHANGESPATH=$WORKSPACE/archive/CHANGES.txt
rm $CHANGESPATH 2>/dev/null

prevts=
for ts in `python2 $MYPATH/getdates.py $CM_BUILD`; do

export ts
(echo "==================================="
echo -n "Since ";date -u -d @$ts 
echo "==================================="
if [ -z "$prevts" ]; then
  repo forall -c 'L=$(git log --oneline --since $ts -n 1); if [ "n$L" != "n" ]; then echo; echo "   * $REPO_PATH"; git log --oneline --since $ts; fi'
else
  repo forall -c 'L=$(git log --oneline --since $ts --until $prevts -n 1); if [ "n$L" != "n" ]; then echo; echo "   * $REPO_PATH"; git log --oneline --since $ts --until $prevts; fi'
fi
echo) >> $CHANGESPATH
export prevts=$ts

done

if [ -z "$prevts" ]; then
  echo "This is the first CyanogenMod build of this type for device $CM_BUILD" >> $CHANGESPATH
fi
