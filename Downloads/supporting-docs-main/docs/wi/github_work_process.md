---
layout: default
title: GitHub Work Process
parent: Work Instruction
has_children: false
---

# Github: Outline Work/Review Process
## Issue
Clearly describe the unit of work (e.g., small change, bugfix, feature) you think needs to be executed (and why, if it's not clear).
## Branch
### Creating
GitHub Desktop app is great, but if you want to use the terminal: Navigate to your local repo, and in the bash terminal:
1. `git checkout main`
2. `git pull origin main` (ensures the most recent remote/approved version of the project is on your local machine)
3. `git checkout -b <xx-short-descriptor>` where `xx` is the Issue number (other naming conventions are allowed, but this is useful to keep track of the issue you're working on). This command allows you to create a branch and switch to it at the same time.
4. Begin your work on this branch.

### Working
- Commit "little and often"
- Only commit _working_ code
- Careful not to commit code that won't work on production( eg. development connection strings) (ideally we'd have `development`/`staging`/`production` environments setup for the project to mitigate this risk)
- Test your own code (think about test cases) 
## Pull Request
Ensure you're comparing the `xx-short-descriptor` branch with `main`, then...

Describe it:
- give it a meaningful title (related to the Issue)
- what you've done
- why you've done it that way (if it's not clear)
- why you've used certain syntax (if it's not common)
- how to test it (if we require manual tests) - outline the test cases.
- if it has a UI, provide a screenshot of the change
- Include `closes #xx` in the description: where `xx` is the Issue number (this automatically links the github issue to the PR) 

## Review
- Do a line by line review, and write a concise summary
- Ask questions if you don't understand whats going on
- Write helpful and constructive comments if you think something's not right
- Be nice (we're all (_always_) learning). 
- Test it properly (in dev/staging) 
## Merge and Deploy
If you think the PR is production quality: 
- Approve it with a positive review
- Deploy it to staging/production (elaborate on this)


# Github Repos
- Set up some branch rules: 
  - so they can't be merged without an approved PR 
  - so that approved branches are deleted automatically. 
- Set up an approved list of code reviewers (so that unauthorized users can't merge unapproved code).
