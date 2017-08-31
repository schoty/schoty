# Schoty

[![Build Status](https://travis-ci.org/schoty/schoty.svg?branch=master)](https://travis-ci.org/schoty/schoty)


A monorepo builder and synchronisation engine 

This package contains the builder for the schoty project. It provides a unified view for multiple user-repositories and implements a synchronisation mechanism between the monorepo and the individual repositories.

**Warning:** this package is an early developpement / prototype phase

## Installation notes

Schoty requires git and Python 3.6 and can be installed with,

```bash
pip install git+https://github.com/schoty/schoty.git
```

## Quick start guide

1. Making a new monorepo

```bash
schoty clone repo1 repo2 new-monorepo
```

2. Change some files in the monorepo (it is a regular git repository) and commit

```bash
cd new-monorepo/
git checkout -b new-feature
touch repo1/new-file
git add repo1/new-file
git commit -m 'Added new-file'
```

3. Synchronize the monorepo with local repositories under `new-monorepo/.repos/`

```bash
schoty scatter
```
or 

```bash
schoty gather 
```

4. Any of the following commands (`pull`, `push`, `fetch`) will be applied to local repositories under
`new-monorepo/.repos/`

```bash
schoty <command>
```

## Limitations

 * Git history rewrites are not supported 

## Related projects
 
  - https://github.com/beberlei/composer-monorepo-plugin
  - https://conda-forge.github.io/ (for the Github integration procedures)
  - https://greenkeeper.io/
