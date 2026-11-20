# README and figures design notes

The README contains the user-supplied research figures converted from PDF to PNG so GitHub renders them inline. All twelve source PDF files remain under `assets/figures/source-pdfs/`; source hashes are in `metadata/figure_manifest.csv`. The supplied confusion matrices were mathematically verified against recorded WAS-SSL balanced accuracies (83.29% and 61.69%). `figure07_confusion.pdf` differs and is placed only in a collapsed supplementary section.

All publication claims retain the original distinctions: J1 image-aware **test**, N01 lesion-aware **validation**, source-attributed HAM/BCN (not external transfer), and untouched N01 **test not evaluated**.

GitHub renders `<img>` relative paths from the repository's root README without a webpage generator. The original SVG banner and older data-derived charts remain in `assets/figures/` for reference; newly supplied figures are in `assets/figures/research/`.

**Before public release:** confirm medical-image redistribution rights for the two XAI PDF and PNG pairs, final author metadata and the preferred open-source license. This repository contains no actual data or trained binary checkpoints.
