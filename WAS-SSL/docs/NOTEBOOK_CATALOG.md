# Notebook catalog

The 35 notebooks below are the selected **executed** uploads, not draft versions with missing output. Files have normalized public filenames. Original upload names and SHA256 hashes are available in [`../metadata/notebook_manifest.csv`](../metadata/notebook_manifest.csv). Cell source text is unchanged; embedded image/HTML/widget output has been removed.

| Group | Notebook | Purpose | Code cells | Printed output cells |
|---|---|---|---:|---:|
| 01 original thesis | [`01_supervised_resnet50.ipynb`](../notebooks/01_original_thesis/01_supervised_resnet50.ipynb) | Plain supervised ResNet50 baseline, multiple seeds | 7 | 6 |
| 01 original thesis | [`02_original_trained_ensemble.ipynb`](../notebooks/01_original_thesis/02_original_trained_ensemble.ipynb) | Original image-level SSL, fusion and CalStack trained-weights ensemble | 39 | 39 |
| 01 original thesis | [`03_confidence_gated_ensemble.ipynb`](../notebooks/01_original_thesis/03_confidence_gated_ensemble.ipynb) | Original fitted ensemble replay and final configuration | 30 | 26 |
| 01 original thesis | [`04_per_image_results.ipynb`](../notebooks/01_original_thesis/04_per_image_results.ipynb) | Historical per-image predictions and metrics | 9 | 2 |
| 01 original thesis | [`05_ham10000_model_evaluation.ipynb`](../notebooks/01_original_thesis/05_ham10000_model_evaluation.ipynb) | Earlier separate HAM10000 domain evaluation; not independently comparable | 12 | 6 |
| 02 journal extension | [`01_j1_original_protocol_lock.ipynb`](../notebooks/02_journal_extension/01_j1_original_protocol_lock.ipynb) | Original thesis split and reproducibility checks | 9 | 9 |
| 02 journal extension | [`02_j2_dinov2.ipynb`](../notebooks/02_journal_extension/02_j2_dinov2.ipynb) | DINOv2 representation and downstream evaluation | 18 | 15 |
| 02 journal extension | [`03_j3_progressive_ablation.ipynb`](../notebooks/02_journal_extension/03_j3_progressive_ablation.ipynb) | Original thesis progressive ablation analysis | 16 | 15 |
| 02 journal extension | [`04_j4_significance_tests.ipynb`](../notebooks/02_journal_extension/04_j4_significance_tests.ipynb) | Paired statistical significance testing | 15 | 13 |
| 02 journal extension | [`05_j5_representation_complementarity.ipynb`](../notebooks/02_journal_extension/05_j5_representation_complementarity.ipynb) | Representation similarity and prediction complementarity | 18 | 16 |
| 02 journal extension | [`06_j6_calibration.ipynb`](../notebooks/02_journal_extension/06_j6_calibration.ipynb) | Calibration, reliability and selective prediction | 16 | 13 |
| 02 journal extension | [`07_j7_xai.ipynb`](../notebooks/02_journal_extension/07_j7_xai.ipynb) | Original thesis XAI and ensemble contribution analysis | 18 | 15 |
| 02 journal extension | [`08_j8_results_consolidation.ipynb`](../notebooks/02_journal_extension/08_j8_results_consolidation.ipynb) | Original thesis final journal results pack | 15 | 15 |
| 02 journal extension | [`09_j9_manuscript_results.ipynb`](../notebooks/02_journal_extension/09_j9_manuscript_results.ipynb) | Original thesis manuscript tables and result pack | 27 | 27 |
| 03 lesion aware | [`00_n01_split_audit.ipynb`](../notebooks/03_lesion_aware/00_n01_split_audit.ipynb) | ISIC 2019 lesion-level split and identity audit | 10 | 10 |
| 03 lesion aware | [`00_n01_archive_stage1.ipynb`](../notebooks/03_lesion_aware/00_n01_archive_stage1.ipynb) | Archived lesion-aware staged inputs | 7 | 6 |
| 03 lesion aware | [`01_r01_supervised_resnet50.ipynb`](../notebooks/03_lesion_aware/01_r01_supervised_resnet50.ipynb) | Lesion-aware R01 supervised ResNet50 training | 6 | 6 |
| 03 lesion aware | [`04_r04_ssl_classification.ipynb`](../notebooks/03_lesion_aware/04_r04_ssl_classification.ipynb) | Lesion-aware Rotation and SimCLR classification | 5 | 5 |
| 03 lesion aware | [`05_r05_dual_ssl_featurebank.ipynb`](../notebooks/03_lesion_aware/05_r05_dual_ssl_featurebank.ipynb) | Saved lesion-aware SSL feature bank | 5 | 5 |
| 03 lesion aware | [`06_r06_ssl_feature_fusion.ipynb`](../notebooks/03_lesion_aware/06_r06_ssl_feature_fusion.ipynb) | Lesion-aware fusion heads | 5 | 5 |
| 03 lesion aware | [`07_r07_thesis_style_ensemble.ipynb`](../notebooks/03_lesion_aware/07_r07_thesis_style_ensemble.ipynb) | N01 thesis-style calibrated ensemble | 8 | 8 |
| 03 lesion aware | [`08_r07_all_ensembles.ipynb`](../notebooks/03_lesion_aware/08_r07_all_ensembles.ipynb) | 205 lesion-aware ensemble candidates | 11 | 11 |
| 04 cross protocol | [`01_g01_provenance_audit.ipynb`](../notebooks/04_cross_protocol/01_g01_provenance_audit.ipynb) | HAM/BCN source provenance across image/lesion protocols | 4 | 4 |
| 04 cross protocol | [`02_g02a_image_aware_sources.ipynb`](../notebooks/04_cross_protocol/02_g02a_image_aware_sources.ipynb) | Image-aware source-specific inference | 10 | 8 |
| 04 cross protocol | [`03_g02b_lesion_aware_sources.ipynb`](../notebooks/04_cross_protocol/03_g02b_lesion_aware_sources.ipynb) | Lesion-aware source-specific inference | 8 | 6 |
| 04 cross protocol | [`04_g03a_image_aware_ensembles.ipynb`](../notebooks/04_cross_protocol/04_g03a_image_aware_ensembles.ipynb) | Image-level ensemble benchmark, 121 candidates | 6 | 2 |
| 04 cross protocol | [`05_g03b_lesion_aware_ensembles.ipynb`](../notebooks/04_cross_protocol/05_g03b_lesion_aware_ensembles.ipynb) | Lesion-aware ensemble benchmark, 205 candidates | 7 | 4 |
| 04 cross protocol | [`06_g04_unified_six_source.ipynb`](../notebooks/04_cross_protocol/06_g04_unified_six_source.ipynb) | Exploratory generic unified ensemble benchmark | 10 | 9 |
| 04 cross protocol | [`07_g04_thesis_derived_families.ipynb`](../notebooks/04_cross_protocol/07_g04_thesis_derived_families.ipynb) | Thesis-family ensemble comparison; includes WAS-SSL candidate | 6 | 2 |
| 04 cross protocol | [`08_g05_frozen_was_ssl.ipynb`](../notebooks/04_cross_protocol/08_g05_frozen_was_ssl.ipynb) | Full ISIC and HAM/BCN frozen WAS-SSL evaluation | 5 | 2 |
| 05 reporting and xai | [`10_j10_all_journal_metrics.ipynb`](../notebooks/05_reporting_and_xai/10_j10_all_journal_metrics.ipynb) | Metrics and confidence intervals across evaluation cohorts | 6 | 2 |
| 05 reporting and xai | [`11_j11_original_supervised_sources.ipynb`](../notebooks/05_reporting_and_xai/11_j11_original_supervised_sources.ipynb) | Original five-seed supervised HAM/BCN results | 3 | 3 |
| 05 reporting and xai | [`12_j12_lesion_supervised_sources.ipynb`](../notebooks/05_reporting_and_xai/12_j12_lesion_supervised_sources.ipynb) | Lesion-aware R01 supervised HAM/BCN results | 3 | 3 |
| 05 reporting and xai | [`13_j13_lesion_aware_xai.ipynb`](../notebooks/05_reporting_and_xai/13_j13_lesion_aware_xai.ipynb) | Lesion-aware six-model Grad-CAM/Grad-CAM++/Score-CAM | 5 | 4 |
| 05 reporting and xai | [`14_j14_original_xai.ipynb`](../notebooks/05_reporting_and_xai/14_j14_original_xai.ipynb) | Original TensorFlow/Keras XAI from trained checkpoints | 7 | 5 |
