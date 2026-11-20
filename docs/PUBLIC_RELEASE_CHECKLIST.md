# Before publishing the GitHub repository

- [ ] Verify author order, permission from all contributors and institution affiliation details.
- [ ] Choose a source-code license; **no license is assumed** by this package. Read `LICENSE_RECOMMENDATION.md`.
- [ ] Check rights to redistribute figures generated from ISIC/HAM/BCN images. The bundled notebooks omit inline image payloads, **but the now-bundled XAI figure PDFs and PNGs explicitly include dermoscopic photographs**. Remove them before release if permission is uncertain.
- [ ] Inspect paths, Kaggle usernames and notebook printouts for any personal information you do not want public. Automated screening found no obvious hard-coded credential assignment in the uploaded code, but it is not a security guarantee.
- [ ] Decide whether to publish intermediate metrics/artifacts or only the research scripts and documented summaries.
- [ ] Fill `CITATION.cff.template` with author names and ORCIDs if applicable; rename to `CITATION.cff` after validation.
- [ ] Include permanent download instructions, dataset licenses and model-weight licenses if full replication is desired.
- [ ] Confirm open research claims and correct manuscript tables before sharing DOI/accepted-paper information.
- [ ] Run `python scripts/verify_repository.py` from the repository root; check no large binary was accidentally added to Git.

**How to upload:** Create a new GitHub repository (suggested name `WAS-SSL`), extract this ZIP **locally**, then use `git init`, `git add .`, commit and push. Upload repository *contents*, not the ZIP file as one artifact. GitHub's web upload may be inconvenient for many files; Git is recommended.

```bash
git init
git add .
git commit -m "Organize WAS-SSL research notebooks and results"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/WAS-SSL.git
git push -u origin main
```
