=========
Changelog
=========

version 1.0.8 (2024-09-18)
--------------------------
- Use a `src`-based library structure.
- Many internal improvements to the codebase:
    * Migrated more configurations to the `pyproject.toml` file.
    * Use dependency groups to reduce the number of PRs opened for dependabot.
    * Add caching and cache-cleaning for test builds on GitHub Actions.
    * Use commit hashes for all CI dependencies and Actions.
    * Use `ruff` for coding standards, replace `isort` with `ruff`
    * Replace `versioneer` with `setuptools-scm` for version tracking.
    * Add `codespell` and `pygrep-hooks` to pre-commit configuration.

version 1.0.7 (2024-08-27)
--------------------------
- Fix algorithm convergence for the `kappa` distribution.
- Added Python 3.12 to the test suite and supported versions.
- Avoid inplace modifications of input arrays in ``lmom_ratios``.
- Adjusted the base dependency pins for the development environment.

version 1.0.6 (2023-07-06)
--------------------------
- Adopted `pyproject.toml` with `setuptools` backend for build configuration (PEP 517 and PEP 621)
- Various coding style standard improvements
- Added GutHub Workflows for automated deployment to PyPI

version 1.0.5 (2023-02-28)
--------------------------
- Rename `frechet_r_gen` to `weibull_min_r`, `frechet_r` being deprecated with SciPy 1.6
- Migrated organisations from OpenHydrology to Ouranosinc:
    * Added Continuous Integration checks, pre-commit configurations, package metadata adjustments
    * Code style now follows Black v2023.1
    * ReadTheDocs documentation for lmoments3 no longer nested within OpenHydrology
    * Documentation is now structured across pages
- Updated versioneer to v0.28

version 1.0.3 (2015-09-24)
--------------------------
- Test on Python 3.5
- Simplify doc config

version 1.0.2 (2015-02-11)
--------------------------
- Conda package build fix

version 1.0.1 (2014-12-02)
--------------------------
- Fix `lmom_fit` for `gev` distribution. Did not return `OrderedDict` in some cases.

version 1.0.0 (2014-12-01)
--------------------------
- Major rewrite with all distributions now being standard scipy `rv_continous` classes
- `samlmu` renamed to `lmom_ratios`
- Replaced many functions by standard scipy implementations
- General bugfixes, code improvements and test

version 0.3.1 (2014-09-25)
--------------------------
- Fixed setup
- Refactored unit tests

version 0.3.0 (2014-09-24)
--------------------------
- First release for Python 3.x

version 0.2.2 (2014-09-23)
--------------------------
- Improved samlmu function to support any value of nmom
- Added Bayesian Information Criterion (BIC) function
- Fixed import glitch that allowed users to import container files
- General Bugfixes

version 0.2.1 (2014-01-15)
--------------------------
- Support for lists as F inputs for all QUA functions
- Added Random Number Generator (rand) for all functions
- Split the main lmoments.py file into several files, as the project is getting to large to maintain as one single file.

version 0.2.0 (2014-01-13)
--------------------------
- Added Probability Density Functions (PDF)
- Added Reverse Lmoment Estimation Functions (LMOM)
- Added Negative Log-Likelihood Function (NlogL)
- Included Unit Tests
- Implemented better version of PELWAK function
- Support for lists as x inputs for all CDF functions
- Bugfixes
- Now licensed under the GPLv3

version 0.1.1
-------------
- Corrected Small Errors and Typos

version 0.1.0
-------------
- Initial Release
