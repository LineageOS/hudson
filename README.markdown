# Adding or updating a device

This repository is preconfigured to use the git-review plugin. More information can be found at:
https://pypi.python.org/pypi/git-review

**Note:** Sort device listings in lineage-build-targets alphanumerically by codename.  
Steps:  
1. Edit lineage-build-targets with your device codename and branch.  
2. Update `updater/devices.json` according to the instructions below.  
3. Submit the change to gerrit for review.  

You can upload your change to gerrit with commands like these:

    git add lineage-build-targets updater/devices.json
    git commit
    git review

### devices.json
devices.json is an array of objects, each with several fields:

* `model`: should be the first thing on the line, and is the device's codename (`PRODUCT_DEVICE`) - e.g. `i9300`.
* `oem`: the manufacturer of the device. (`PRODUCT_BRAND`) - e.g. `Samsung`.
* `name`: the user-friendly name of the device - e.g. `Galaxy S III (International)`.
* `has_recovery`: (*optional*) whether or not the device has a separate recovery partition. Defaults to `true`.

### roomservice-main-device-repos.json
`roomservice-main-device-repos.json` is used by roomservice to figure out the
initial repository to download for a specific device. It is used for non-deps-only
mode downloading during lunch targets. Only the main repository should be specified
(the one where the `lineage.mk` and `lineage.dependencies` files for the device lie).
All further repositories are downloaded by roomservice through the regular process
of processing `lineage.dependencies`.
