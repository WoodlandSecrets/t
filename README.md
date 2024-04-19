# dsapwd

[![Release](https://img.shields.io/github/v/release/dsa/dsapwd)](https://img.shields.io/github/v/release/dsa/dsapwd)
[![Build status](https://img.shields.io/github/actions/workflow/status/dsa/dsapwd/main.yml?branch=main)](https://github.com/dsa/dsapwd/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/dsa/dsapwd/branch/main/graph/badge.svg)](https://codecov.io/gh/dsa/dsapwd)
[![Commit activity](https://img.shields.io/github/commit-activity/m/dsa/dsapwd)](https://img.shields.io/github/commit-activity/m/dsa/dsapwd)
[![License](https://img.shields.io/github/license/dsa/dsapwd)](https://img.shields.io/github/license/dsa/dsapwd)

This is a template repository for Python projects that use Poetry for their dependency management.

- **Github repository**: <https://github.com/dsa/dsapwd/>
- **Documentation** <https://dsa.github.io/dsapwd/>

## Getting started with your project

First, create a repository on GitHub with the same name as this project, and then run the following commands:

```bash
git init -b main
git add .
git commit -m "init commit"
git remote add origin git@github.com:dsa/dsapwd.git
git push -u origin main
```

Finally, install the environment and the pre-commit hooks with

```bash
make install
```

You are now ready to start development on your project!
The CI/CD pipeline will be triggered when you open a pull request, merge to main, or when you create a new release.

To finalize the set-up for publishing to PyPi or Artifactory, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/publishing/#set-up-for-pypi).
For activating the automatic documentation with MkDocs, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/mkdocs/#enabling-the-documentation-on-github).
To enable the code coverage reports, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/codecov/).

## Releasing a new version

- Create an API Token on [Pypi](https://pypi.org/).
- Add the API Token to your projects secrets with the name `PYPI_TOKEN` by visiting [this page](https://github.com/dsa/dsapwd/settings/secrets/actions/new).
- Create a [new release](https://github.com/dsa/dsapwd/releases/new) on Github.
- Create a new tag in the form `*.*.*`.

For more details, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/cicd/#how-to-trigger-a-release).

---

Repository initiated with [fpgmaas/cookiecutter-poetry](https://github.com/fpgmaas/cookiecutter-poetry).
