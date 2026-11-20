# Results and interpretation

## Source of numbers

The machine-readable G05 CSVs were transcribed from the **executed G05 notebook output** and the build validates that each recorded figure appears in the source output. The data are not a newly rerun experiment. See the notebook SHA in `metadata/notebook_manifest.csv`.

## Main results (BACC %)

| Method | Full J1 image test | Full N01 lesion validation |
|---|---:|---:|
| Original SimCLR anchor, no bias | 84.00 | 59.21 |
| Original/R07 class-bias CalStack | 83.95 | **62.04** |
| WAS-SSL weighted anchor no bias | 83.29 | 61.69 |

## Candidate choice is *not* a demonstrated universal win

WAS-SSL achieves mean 70.19% BACC over four HAM/BCN source/protocol slices vs historical CalStack 70.00%. Their difference is 0.19 percentage points. In full N01 validation and lesion-aware BCN, CalStack class bias is numerically stronger. Different ensembles win in different cohorts, and the four slices do not have independent clinical-domain status.

G03-A compared 121 candidates, G03-B compared 205; G04/G05 compared additional families. Extensive multiple comparisons and use of the original J1 test for post hoc comparison mean that the strongest observed candidate may be optimistically selected. **Do not present WAS-SSL as statistically superior or as validated on the untouched N01 test.**

## What would complete a rigorous final claim

1. Predefine the primary metric (recommend lesion-group BACC, with macro-F1 and calibration as secondary).
2. Fit base models/stackers and select the ensemble family with train/meta_train/validation only; avoid re-tuning based on J1 test and HAM/BCN held-out source labels.
3. Freeze the exact formula, trained weights, thresholds, temperatures and preprocessing.
4. Evaluate once on the untouched 2,244-image N01 test and quantify uncertainty using lesion-group resampling where identity is known.
5. If claiming cross-dataset generalization, use a genuinely held-out source excluded from all training and model selection, not a source-identifiable ISIC 2019 subset.

## XAI

J7/J13/J14 provide qualitative Grad-CAM, Grad-CAM++ and Score-CAM panels for trained convolutional components. No quantitative ground-truth localization overlap score or clinical reader study is reported in this repository. Do not claim a single ensemble Grad-CAM exists for a black-box stacker.

## Additional original results

- [`results/base_model_ham_bcn_bacc.csv`](../results/base_model_ham_bcn_bacc.csv) reproduces the G02-A/G02-B base-model rows and J11/J12 supervised rows. The image-aware supervised prediction is an ensemble of five seeds; R01 is a separate lesion-aware model.
- [`results/j3_original_ablation_bacc.csv`](../results/j3_original_ablation_bacc.csv) summarizes the J3 progressive 13-stage baseline and ensemble analysis. It does **not** establish a controlled isolate-one-component WAS-SSL ablation across all protocols.
- [`results/j10_recorded_full_metric_table.txt`](../results/j10_recorded_full_metric_table.txt) retains all captured J10 metrics as text, because the original run CSV artifact was not uploaded.
