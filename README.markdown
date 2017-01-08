# Adding or updating a device

This repository is preconfigured to use the git-review plugin. More information can be found at:
https://pypi.python.org/pypi/git-review

**Note:** Sort device listings in lineage-build-targets alphanumerically by codename.  
Steps:  
1. Edit lineage-build-targets with your device codename and branch.  
2. Update the lineageos_updater repository according to the instructions there.  
3. Submit both changes to gerrit for review.  

You can upload your change to gerrit with commands like these:

    git add lineage-build-targets
    git commit
    git review
