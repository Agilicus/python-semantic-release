# Changelog

<!--next-version-placeholder-->

## v7.12.0 (2021-01-25)
### Feature
* **github:** Retry GitHub API requests on failure ([#314](https://github.com/relekang/python-semantic-release/issues/314)) ([`ac241ed`](https://github.com/relekang/python-semantic-release/commit/ac241edf4de39f4fc0ff561a749fa85caaf9e2ae))

### Documentation
* **actions:** PAT must be passed to checkout step too ([`e2d8e47`](https://github.com/relekang/python-semantic-release/commit/e2d8e47d2b02860881381318dcc088e150c0fcde))

## v7.11.0 (2021-01-08)
### Feature
* **print-version:** Add print-version command to output version ([`512e3d9`](https://github.com/relekang/python-semantic-release/commit/512e3d92706055bdf8d08b7c82927d3530183079))

### Fix
* **actions:** Fix github actions with new main location ([`6666672`](https://github.com/relekang/python-semantic-release/commit/6666672d3d97ab7cdf47badfa3663f1a69c2dbdf))
* Avoid Unknown bump level 0 message ([`8ab624c`](https://github.com/relekang/python-semantic-release/commit/8ab624cf3508b57a9656a0a212bfee59379d6f8b))
* Add dot to --define option help ([`eb4107d`](https://github.com/relekang/python-semantic-release/commit/eb4107d2efdf8c885c8ae35f48f1b908d1fced32))

## v7.10.0 (2021-01-08)
### Feature
* **build:** Allow falsy values for build_command to disable build step ([`c07a440`](https://github.com/relekang/python-semantic-release/commit/c07a440f2dfc45a2ad8f7c454aaac180c4651f70))

### Documentation
* Fix incorrect reference syntax ([`42027f0`](https://github.com/relekang/python-semantic-release/commit/42027f0d2bb64f4c9eaec65112bf7b6f67568e60))
* Rewrite getting started page ([`97a9046`](https://github.com/relekang/python-semantic-release/commit/97a90463872502d1207890ae1d9dd008b1834385))

## v7.9.0 (2020-12-21)
### Feature
* **hvcs:** Add hvcs_domain config option ([`ab3061a`](https://github.com/relekang/python-semantic-release/commit/ab3061ae93c49d71afca043b67b361e2eb2919e6))

### Fix
* **history:** Coerce version to string ([#298](https://github.com/relekang/python-semantic-release/issues/298)) ([`d4cdc3d`](https://github.com/relekang/python-semantic-release/commit/d4cdc3d3cd2d93f2a78f485e3ea107ac816c7d00))
* **history:** Require semver >= 2.10 ([`5087e54`](https://github.com/relekang/python-semantic-release/commit/5087e549399648cf2e23339a037b33ca8b62d954))

## v7.8.2 (2020-12-19)
### Fix
* **cli:** Skip remove_dist where not needed ([`04817d4`](https://github.com/relekang/python-semantic-release/commit/04817d4ecfc693195e28c80455bfbb127485f36b))

## v7.8.1 (2020-12-18)
### Fix
* **logs:** Fix TypeError when enabling debug logs ([`2591a94`](https://github.com/relekang/python-semantic-release/commit/2591a94115114c4a91a48f5b10b3954f6ac932a1))
* Filenames with unknown mimetype are now properly uploaded to github release ([`f3ece78`](https://github.com/relekang/python-semantic-release/commit/f3ece78b2913e70f6b99907b192a1e92bbfd6b77))

## v7.8.0 (2020-12-18)
### Feature
* Add `upload_to_pypi_glob_patterns` option ([`42305ed`](https://github.com/relekang/python-semantic-release/commit/42305ed499ca08c819c4e7e65fcfbae913b8e6e1))

### Fix
* **netrc:** Prefer using token defined in GH_TOKEN instead of .netrc file ([`3af32a7`](https://github.com/relekang/python-semantic-release/commit/3af32a738f2f2841fd75ec961a8f49a0b1c387cf))
* **changelog:** Use "issues" link vs "pull" ([`93e48c9`](https://github.com/relekang/python-semantic-release/commit/93e48c992cb8b763f430ecbb0b7f9c3ca00036e4))

## v7.7.0 (2020-12-12)
### Feature
* **changelog:** Add PR links in markdown ([#282](https://github.com/relekang/python-semantic-release/pull/282)) ([`0448f6c`](https://github.com/relekang/python-semantic-release/commit/0448f6c350bbbf239a81fe13dc5f45761efa7673))

## v7.6.0 (2020-12-06)
### Feature
* Add `major_on_zero` option ([`d324154`](https://github.com/relekang/python-semantic-release/commit/d3241540e7640af911eb24c71e66468feebb0d46))

### Documentation
* Add documentation for option `major_on_zero` ([`2e8b26e`](https://github.com/relekang/python-semantic-release/commit/2e8b26e4ee0316a2cf2a93c09c783024fcd6b3ba))

## v7.5.0 (2020-12-04)
### Feature
* **logs:** Include scope in changelogs (#281) ([`21c96b6`](https://github.com/relekang/python-semantic-release/commit/21c96b688cc44cc6f45af962ffe6d1f759783f37))

## v7.4.1 (2020-12-04)
### Fix
* Add "changelog_capitalize" to flags (#279) ([`37716df`](https://github.com/relekang/python-semantic-release/commit/37716dfa78eb3f848f57a5100d01d93f5aafc0bf))

## v7.4.0 (2020-11-24)
### Feature
* Add changelog_capitalize configuration ([`7cacca1`](https://github.com/relekang/python-semantic-release/commit/7cacca1eb436a7166ba8faf643b53c42bc32a6a7))

### Documentation
* Fix broken internal references (#270) ([`da20b9b`](https://github.com/relekang/python-semantic-release/commit/da20b9bdd3c7c87809c25ccb2a5993a7ea209a22))
* Update links to Github docs (#268) ([`c53162e`](https://github.com/relekang/python-semantic-release/commit/c53162e366304082a3bd5d143b0401da6a16a263))

## v7.3.0 (2020-09-28)
### Feature
* Generate `changelog.md` file (#266) ([`2587dfe`](https://github.com/relekang/python-semantic-release/commit/2587dfed71338ec6c816f58cdf0882382c533598))

### Documentation
* Fix docstring ([`5a5e2cf`](https://github.com/relekang/python-semantic-release/commit/5a5e2cfb5e6653fb2e95e6e23e56559953b2c2b4))
