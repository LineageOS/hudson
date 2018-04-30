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

### roomservice-initial-lunch-repo.json
`Roomservice` is the LineageOS utility for automatically downloading
device repositories, and populating
`.repo/local_manifests/roomservice.xml` with them. It is not invoked
directly by the user, but instead it runs automatically whenever the
`lunch` command is invoked at the beginning of the build process and at
least one repository is not available locally and must be downloaded.

To accomplish this task, `roomservice` looks up the
`roomservice-initial-lunch-repo.json` file on
https://github.com/LineageOS/hudson in order to determine the
association between the `lunch` target requested by the user, and the
initial repository it should download. After the initial repository is
downloaded, `roomservice` searches for a file called
`lineage.dependencies` in the root of this repository. There it finds
other repositories to download. `Roomservice` searches for
`lineage.dependencies` files recursively in the roots of repositories,
until the main device repository and its full tree of dependencies has
been downloaded.

The `lineage.dependencies` file that each repository may optionally have
in its root has the following syntax:

```
[
  {
    "repository": "${repo}",
    "target_path": "${path}"
  },
  ...
]
```

Where `https://github.com/LineageOS/${repo}` is the source that will be
used to download the repository's dependency specified by the current
JSON entry, and `${path}` is a local filesystem path to the folder where
`roomservice` will `repo sync` this dependency to.

The singular `roomservice-initial-lunch-repo.json` file on Hudson has the
following syntax:

```
{
  "${device1}": {
    "repository": "${repo1}",
    "target_path": "${path1}"
  },
  "${device2}": {
    "repository": "${repo2}",
    "target_path": "${path2}"
  },
  ...
}
```

Where `${device1}`, `${device2}` are the lookup key that `roomservice`
uses, based on command invocations such as `lunch ${device1}`.

Inside each nodes on the level with `${device1}` in this JSON lies a
structure that shares the same syntax as the `lineage.dependencies`
file.

In the case of both `roomservice-initial-lunch-repo.json` and
`lineage.dependencies`, the source for `${repo1}`, `${repo2}` etc is
implicitly https://github.com/LineageOS. Drawing dependencies from other
sources is not permitted.

Developers are expected to populate the
`roomservice-initial-lunch-repo.json` with an entry connecting their
`lunch` device target name with the repository name on
https://github.com/LineageOS where its main repository resides (the one
containing the `AndroidProducts.mk` file). All further repositories
necessary for a successful build shall be downloaded by means of
`lineage.dependencies`.

If `roomservice` cannot find the device in
`roomservice-initial-lunch-repo.json` during lookup, it will attempt to
guess the name of the initial repository from the `lunch ${device}`
target. It does this by assuming that the `repository` name takes a
`android_device_${vendor}_${device}` form, and searching for all
repositories on https://github.com/LineageOS that match the
`android_device_*_${device}` pattern. It then deduces the `${vendor}`
name by extrapolating from the matched pattern, and the `target_path`
becomes `device/${vendor}/${device}`.

After syncing a repository, `roomservice` will add an entry to the
`.repo/local_manifests/roomservice.xml` file denoting it has done so,
and removing the need to perform the lookup on subsequent `lunch`
invocations.

The presence of a device in the `roomservice-initial-lunch-repo.json`
file does not depend upon, or influence, its shipping status (official
or unofficial). It is only an indication for `roomservice` on what
repository path corresponds to the `lunch` target being built.

