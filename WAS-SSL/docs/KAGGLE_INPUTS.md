# Kaggle inputs and external artifacts

This repository contains notebook **source and recorded outputs**, not model binaries. The original runs expect Kaggle notebook/dataset inputs attached in the interface. Required names are grounded in notebook source and execution logs. The names below refer to **Kaggle run outputs**, not GitHub notebook filenames.

| Run | Most important required Kaggle inputs |
|---|---|
| N01 | Original ISIC 2019 images/metadata and lesion-ID source; see N01 code for official acquisition and split rules |
| R01 | N01 dataset audit/split artifacts (including prepared images and split manifests) |
| R04 | N01 outputs + prior SSL encoder checkpoints; earlier SSL pretraining artifacts may be absent from this GitHub archive |
| R05 | N01 + R04 encoder output |
| R06 | N01 + R04 + R05 as required by saved feature/fusion loaders |
| R07 | R04/R06 trained predictions and meta-trained stacking artifacts; the two R07 variants are separate experiments |
| G01 | Original J1, N01 master manifest and official ISIC/HAM/BCN metadata |
| G02-A | `last-part-of-the-previous-one` + original image archive/official source metadata; historical image filenames require content matching |
| G02-B | `lesion-n01` + R04 + R06 outputs |
| G03-A | completed `g02-a-v2-ham10000-bcn20000-source-evaluation` + original thesis fitted ensemble |
| G03-B | completed `g02-b-v2-lesion-aware-n01-ham-bcn` + `lesion-r07-n01-all-ensembles-s42` |
| G04 | completed `g03a-image-level-all-ensembles-s42` and `g03b-lesion-aware-all-ensembles-s42` |
| G05 | completed `last-part-of-the-previous-one`, `confidence-gated-ensemble`, `lesion-r07-n01-all-ensembles-s42`, `g03a-image-level-all-ensembles-s42`, `g03b-lesion-aware-all-ensembles-s42` |
| J11 | G02-A + original `supervised-classification-for-journal` five-seed model files |
| J12 | G03-B + `lesion-r01-supervised-resnet50-s42` trained **best** checkpoint, optionally N01 prepared images |
| J13 | G03-B + R04 + R06 trained models, official original images, optionally N01 prepared images |
| J14 | G02-A + `last-part-of-the-previous-one` genuine TensorFlow/Keras model checkpoints; original images |
| J10 | completed G03-A and G03-B, optionally J11/J12 and other journal output archives |

**Checkpoint specificity:** J12 uses `models/best.pt` from R01 (not `training_state/last.pt` and never R04 as a surrogate). That was established by the executed J12 log. The actual checkpoint file is **not included** in this GitHub archive.

**Data:** Official ISIC images/metadata, HAM/BCN provenance and Kaggle-generated model files must be obtained from their respective source downloads or attached Kaggle outputs under their applicable licenses. A valid `requirements.txt` installation does **not** reproduce archived weights without those inputs.

**Execution:** Kaggle GPU/Internet requirements vary by notebook. N01 downloads many gigabytes of imagery, and J12/J13/J14 may reconstruct images from the official archive if not attached. Keep runs under Kaggle's session constraints and save intermediate datasets/checkpoints after each stage.
