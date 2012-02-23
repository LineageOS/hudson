#!/usr/bin/env bash

echo script path: $MYPATH

if [ -z "$WORKSPACE" ]
then
  echo WORKSPACE not specified
  exit 1
fi

cd $WORKSPACE
export BUILD_NO=$BUILD_NUMBER
unset BUILD_NUMBER

export PATH=~/bin:$PATH

REPO=$(which repo)
if [ -z "$REPO" ]
then
  mkdir -p ~/bin
  curl https://dl-ssl.google.com/dl/googlesource/git-repo/repo > ~/bin/repo
  chmod a+x ~/bin/repo
fi

if [ -z "$REPO_BRANCH" ]
then
  echo REPO_BRANCH not specified
  exit 1
fi

if [ ! -d $REPO_BRANCH ]
then
  mkdir $REPO_BRANCH
  cd $REPO_BRANCH
  repo init -u git://github.com/CyanogenMod/android.git -b $REPO_BRANCH
else
  cd $REPO_BRANCH
fi

cp $WORKSPACE/hudson/$REPO_BRANCH.xml .repo/local_manifest.xml
if [ -f $WORKSPACE/hudson/$REPO_BRANCH-setup.sh ]
then
  $WORKSPACE/hudson/$REPO_BRANCH-setup.sh
fi

echo Syncing...
repo sync

. build/envsetup.sh
lunch $LUNCH

UNAME=$(uname)

if [ "$UNAME" = "Darwin" ]
then
  THREADS=$(sysctl hw.ncpu | cut -f 2 -d :)
else
  THREADS=$(cat /proc/cpuinfo | grep processor | wc -l)
fi

if [ "$RELEASE_TYPE" = "CM_NIGHTLY" ]
then
  export CM_NIGHTLY=true
elif [ "$RELEASE_TYPE" = "CM_SNAPSHOT" ]
  export CM_SNAPSHOT=true
elif [ "$RELEASE_TYPE" = "CM_RELEASE" ]
  export CM_RELEASE=true
fi

make -j$THREADS bacon

exit $?