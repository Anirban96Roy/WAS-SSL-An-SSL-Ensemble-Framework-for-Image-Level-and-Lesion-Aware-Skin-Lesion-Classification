# Data provenance, split leakage and cohort interpretation

- Original image-aware thesis uses the canonical J1 image-level split, with 2,534 test images. A lesion may be represented by more than one image; the original split must **not** be described as lesion-isolated.
- The later N01 protocol separates lesion identities across train/meta_train/validation/test where identified, and sets aside 2,144 quarantined rows. N01 has 16,490 train, 2,267 meta_train, 2,186 validation and 2,244 locked test images. The N01 test has **no reported model performance** in the supplied executed notebooks.
- G01 identifies HAM10000 and BCN20000 identities among ISIC 2019 images. G02-A resolves renamed Hugging Face image IDs through content/provenance matching; G02-B uses N01 manifest identities and exact prepared preprocessing.
- Source-subset cohort sizes are image-level HAM=999 and BCN=1,240; N01 validation HAM=1,060 and BCN=1,049. These four evaluated cohorts share dataset lineage; none is a totally unseen clinical domain.
- Original image-aware and lesion-aware trained models use **different partitions and training histories**, not just a changed test split. Any apparent loss of BACC cannot be attributed solely to leakage without a controlled paired design.
- Avoid presenting the HAM/BCN slices as an externally collected validation set. The earlier separate HAM pipeline notebook may use its own evaluation protocol: keep it separate and describe its actual splits before comparison.
- Source-specific class distributions are imbalanced. Report BACC, macro-F1 and class-wise recall with uncertainty; accuracy alone can obscure minority-class errors.
- Medical classification results are research-only, **not evidence of clinical deployment readiness**.
