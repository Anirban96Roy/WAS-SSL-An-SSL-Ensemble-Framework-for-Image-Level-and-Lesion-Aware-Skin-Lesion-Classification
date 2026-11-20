# Reproducibility and public notebook policy

- **Original code and markdown cell source are unchanged.** Per-notebook `cell_source_sha256` in `metadata/notebook_manifest.csv` hashes the original cell types and source text and verifies equality in the public copy.
- The original uploaded notebook SHA256 is listed separately; the public notebook file will have a different checksum because metadata and inline figure binaries have been removed.
- Text outputs from executed cells remain where provided. Missing numeric output indicates it was not in the uploaded notebook; no synthetic metrics were inserted into notebook cells.
- Inline image/png, HTML display payloads and widget metadata were removed. Actual figures are generated at run time and may depend on licensed dataset imagery.
- Intended environment is Kaggle. Code includes frozen paths under `/kaggle/input` and often `/kaggle/working`; it will not run unmodified from an arbitrary local working directory without compatible input mounts.
- `requirements.txt` is a package overview, not a complete conda-lock of the original historical Kaggle environments. TensorFlow/Keras and PyTorch runtime versions should match checkpoint conventions. Prefer separately managed GPU environments for TF original and PyTorch lesion-aware training.
- External datasets and trained checkpoints are not in this repository. Git LFS or an archived dataset with the publisher's terms is appropriate if releasing large derived binaries; do not distribute third-party images without permission.
- Use `python scripts/verify_repository.py` to validate all notebooks, source hashes, file hashes, result CSVs and absence of embedded image media.
