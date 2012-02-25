# In your Jenkins/Hudson job, simply put:
# $(curl https://raw.github.com/CyanogenMod/hudson/master/job.sh)
# This will run the contents of this script as the job.

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