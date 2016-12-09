# Adding or updating a device

This repository is preconfigured to use the git-review plugin. More information can be found at:
https://pypi.python.org/pypi/git-review

**Note:** Sort device listings in cm-build-targets and devices.json alphanumerically by codename.  
1. Edit cm-build-targets with your device codename and branch.  
2. Add a PNG 109x124 image of your device to getcm-devices/static/img directory.  
3. Add your device's information to devices.json.  
4. Submit a change to gerrit for review.  

You can upload your change to gerrit with commands like these:

    git add cm-build-targets
    git add getcm-devices/devices.json
    git add getcm-devices/static/img/image.png
    git commit
    git review

Once you have submitted your change add the group "Release" to the reviewers.
