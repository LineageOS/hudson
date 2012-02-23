#!/usr/bin/env bash

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
  repo init -u git://github.com/CyanogenMod/androig.it -b $REPO_BRANCH
else
  cd $REPO_BRANCH
fi

repo sync

echo success!
