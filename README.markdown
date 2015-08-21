# Adding or updating a device

This repository is preconfigured to use the git-review plugin. More information can be found at:
https://pypi.python.org/pypi/git-review

Edit cm-build-targets with your device codename and frequency.
Add an image to getcm-devices/static/img directory, or use the no-image.jpg.
Add your device's information to devices.json. Images should be 109x124.
Submit a change to gerrit for review.

You can upload your change to gerrit with commands like these:

    git add cm-build-targets
    git add getcm-devices/devices.json
    git add getcm-devices/static/img/image.png
    git commit
    git-review

Once you have submitted your change add the group "Release" to the reviewers.
