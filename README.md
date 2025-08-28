# distro-test-containers

Distribution specific containers for Ansible testing.

## Directory Structure

Each directory under `containers` corresponds to a [quay.io](https://quay.io/organization/ansible) repository.
The suffix `-test-container` is appended to each directory name to derive the repository name.

Within each directory is one or more version subdirectories.
Each version becomes the first component of the container tag.
The branch name or release version becomes the second component of the container tag.

This results in container and tag names of the form:

`{container_name}-test-container:{container_version}-{branch_or_release_version}`

> NOTE: Prior to ansible-core 2.20, a different container naming and tagging scheme was used.

## Branch Names

The primary development branch is the `main` branch. 
Additionally, there are `stable-X.Y` branches for each associated ansible-core release.

## Release Names

Release names are of the form `vX.Y-N`.
The `X.Y` component corresponds to the associated ansible-core release.
The `N` component is incremented with each container release for the same ansible-core release, starting from zero.

> NOTE: Prior to ansible-core 2.20, a different release versioning scheme was used.

## Default Container

If you are looking for the `default` test container then see:

* [ansible/default-test-container](https://github.com/ansible/default-test-container/) - Used for collections.
* [ansible/ansible-core-test-container](https://github.com/ansible/ansible-core-test-container/) - Used for ansible-core.
