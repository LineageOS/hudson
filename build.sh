#!/usr/bin/env bash

echo script path: $MYPATH

if [ -z "$WORKSPACE" ]
then
  echo WORKSPACE not specified
  exit 1
fi

cd $WORKSPACE

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

echo Syncing...
repo sync

. build/envsetup.sh
lunch $JOB_NAME

make -j$(cat /proc/cpuinfo | grep processor | wc -l) bacon

echo Done!
