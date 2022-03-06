# Contributing to Signal Backtester
We love your input! We want to make contributing to this project as easy and transparent as possible, whether it's:
  - Reporting a bug
  - Discussing the current state of the code
  - Submitting a fix
  - Proposing new features
  - Becoming a maintainer
## We Develop with Github
We use github to host code, to track issues and feature requests, as well as accept pull requests.
### Issues
Issues should be used to report problems with the library, request a new feature, or to discuss potential changes before a PR is created. When you create a new Issue, a template will be loaded that will guide you through collecting and providing the information we need to investigate.

If you find an Issue that addresses the problem you're having, please add your own reproduction information to the existing issue rather than creating a new one. Adding a [reaction](https://github.blog/2016-03-10-add-reactions-to-pull-requests-issues-and-comments/) can also help be indicating to our maintainers that a particular problem is affecting more than just the reporter.
### Pull Requests
PRs to our libraries are always welcome and can be a quick way to get your fix or improvement slated for the next release. In general, PRs should:

  - Only fix/add the functionality in question **OR** address wide-spread whitespace/style issues, not both.
  - Add unit or integration tests for fixed or changed functionality (if a test suite already exists).
  - Address a single concern in the least number of changed lines as possible.
  - Include documentation in the repo or on our [docs site](https://auth0.com/docs).
  - Be accompanied by a complete Pull Request template (loaded automatically when a PR is created).

For changes that address core functionality or would require breaking changes (e.g. a major release), it's best to open an Issue to discuss your proposal first. This is not required but can save time creating and reviewing changes.

In general, we follow the ["fork-and-pull" Git workflow](https://github.com/susam/gitpr)

 1. Fork the repository to your own Github account
 2. Clone the project to your machine
 3. Create a branch locally with a succinct but descriptive name
 4. Commit changes to the branch
 5. Following any formatting and testing guidelines specific to this repo
 6. Push changes to your fork
 7. Open a PR in our repository and follow the PR template so that we can efficiently review the changes.
## Report bugs using Github's [issues](https://github.com/xibalbas/signal_backtester/issues)
We use GitHub issues to track public bugs. Report a bug by [opening a new issue](); it's that easy!
## Write bug reports with detail, background, and sample code
[This is an example](http://stackoverflow.com/q/12488905/180626) of a bug report I wrote, and I think it's not a bad model. Here's [another example from Craig Hockenberry](http://www.openradar.me/11905408), an app developer whom I greatly respect.

**Great Bug Reports** tend to have:
  - A quick summary and/or background
  - Steps to reproduce
    - Be specific!
    - Give sample code if you can. [My stackoverflow question](http://stackoverflow.com/q/12488905/180626) includes sample code that *anyone* with a base R setup can run to reproduce what I was seeing
  - What you expected would happen
  - What actually happens
  - Notes (possibly including why you think this might be happening, or stuff you tried that didn't work)

People *love* thorough bug reports. I'm not even kidding.