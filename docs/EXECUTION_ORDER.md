# Execution order (Kaggle notebooks)

**Preserve original Kaggle output names:** the notebook code searches under `/kaggle/input` for artifacts generated in preceding runs. Renaming a notebook file inside this GitHub repository **does not rename its Kaggle output directory**. Do not casually change the output paths hard-coded in experiment code.

## Track A — Original image-aware thesis

1. [`01_supervised_resnet50`](../notebooks/01_original_thesis/01_supervised_resnet50.ipynb) — supervised baseline.
2. [`02_original_trained_ensemble`](../notebooks/01_original_thesis/02_original_trained_ensemble.ipynb) — original Rotation/SimCLR/fusion and ensemble experiment; requires outputs from earlier thesis models that may not be uploaded in this repository.
3. [`03_confidence_gated_ensemble`](../notebooks/01_original_thesis/03_confidence_gated_ensemble.ipynb) — trained model probabilities, frozen fitted ensemble configuration and archived results.
4. [`04_per_image_results`](../notebooks/01_original_thesis/04_per_image_results.ipynb) and [`05_ham10000_model_evaluation`](../notebooks/01_original_thesis/05_ham10000_model_evaluation.ipynb) are additional historical analyses with their own input requirements.

## Track B — Original journal extension

Run J1 → J2 → J3 → J4 → J5 → J6 → J7 → J8 → J9, each with the original outputs requested in the first cells. Some extensions are independent once frozen original predictions are available; their numerical results should not be mixed with N01 lesion-aware evaluations.

## Track C — N01 lesion-aware protocol

1. N01 identity audit and split creation (`00_n01_split_audit`); check train/meta_train/validation/test/quarantine manifests.
2. R01 supervised ResNet50 (`01_r01_supervised_resnet50`).
3. R04 Rotation/SimCLR classification (`04_r04_ssl_classification`) following earlier saved SSL pretraining checkpoints; R02/R03 upstream trainer notebooks were **not among the supplied files**.
4. R05 frozen feature bank (`05_r05_dual_ssl_featurebank`).
5. R06 fusion models (`06_r06_ssl_feature_fusion`).
6. R07 thesis-style and comprehensive ensembles (`07_r07_thesis_style_ensemble`, `08_r07_all_ensembles`).

## Track D — Cross-protocol / source-specific comparison

1. G01 provenance/source audit → G02-A/G02-B source-specific predictions.
2. G03-A/G03-B ensemble family replay.
3. G04 unified benchmark and thesis-family comparison (exploratory).
4. G05 frozen thesis-style WAS-SSL evaluation on full ISIC 2019 and source subsets. **G05 evaluates the original image-aware test and N01 validation, not N01 locked test.**

## Track E — Journal metrics and explanations

J10 full tables; J11 original supervised source predictions; J12 N01 supervised source predictions (requires original R01 `models/best.pt`); J13 lesion-aware XAI; J14 original thesis TensorFlow/Keras XAI. Their output artifacts include CSVs, figure files and diagnostic JSON when run on Kaggle.

**Do not rerun training on the final N01 test to choose an ensemble.** Final-test reporting belongs to a separate, preregistered/frozen evaluation after development-only selection.
