if [ -z "$HOME" ]
then
  echo HOME not in environment, guessing...
  export HOME=$(awk -F: -v v="$USER" '{if ($1==v) print $6}' /etc/passwd)
fi

cd $WORKSPACE
mkdir -p ../android
cd ../android
export WORKSPACE=$PWD

if [ ! -d hudson ]
then
  git clone git://github.com/CyanogenMod/hudson.git
fi

cd hudson
git pull

exec ./build.sh
