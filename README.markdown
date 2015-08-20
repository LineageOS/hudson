# Adding or updating a device

This repository is preconfigured to use the git-review plugin. More information can be found at:
https://pypi.python.org/pypi/git-review

Edit cm-build-targets and submit a change to gerrit for review. The
syntax for that file is documented in its first few lines.
You can upload your change to gerrit with commands like these:

    git add cm-build-targets
    git commit
    git review

Once you have submitted your change add the group "Release" to the reviewers.
