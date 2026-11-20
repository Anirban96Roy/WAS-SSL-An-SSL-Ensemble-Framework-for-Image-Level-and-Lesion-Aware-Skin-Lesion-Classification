# Research figure gallery and provenance

This repository includes **all twelve uploaded PDF figures** (including both source-pipeline variants) and rendered GitHub-friendly PNGs. Figures have **not been modified** beyond rasterization. The original uploaded file name, SHA256 and exported file paths appear in [`metadata/figure_manifest.csv`](../metadata/figure_manifest.csv).

| No. | Figure | GitHub image | Original PDF | Role |
|---:|---|---|---|---|
| 01 | Primary architecture | [View PNG](../assets/figures/research/was_ssl_framework.png) | [Source PDF](../assets/figures/source-pdfs/was_ssl_framework.pdf) | primary |
| 02 | Image-aware methodology | [View PNG](../assets/figures/research/image_aware_prediction_pipeline.png) | [Source PDF](../assets/figures/source-pdfs/image_aware_prediction_pipeline.pdf) | primary |
| 03 | Archive of source figure | [View PNG](../assets/figures/research/image_aware_prediction_pipeline_full.png) | [Source PDF](../assets/figures/source-pdfs/image_aware_prediction_pipeline_full.pdf) | appendix |
| 04 | Lesion-aware methodology | [View PNG](../assets/figures/research/lesion_aware_prediction_pipeline.png) | [Source PDF](../assets/figures/source-pdfs/lesion_aware_prediction_pipeline.pdf) | primary |
| 05 | Feature fusion architectures | [View PNG](../assets/figures/research/feature_fusion_architectures.png) | [Source PDF](../assets/figures/source-pdfs/feature_fusion_architectures.pdf) | primary |
| 06 | Source-stratified performance | [View PNG](../assets/figures/research/source_stratified_bacc.png) | [Source PDF](../assets/figures/source-pdfs/source_stratified_bacc.pdf) | primary |
| 07 | Class-wise analysis | [View PNG](../assets/figures/research/per_class_recall.png) | [Source PDF](../assets/figures/source-pdfs/per_class_recall.pdf) | primary |
| 08 | WAS-SSL image-aware confusion matrix | [View PNG](../assets/figures/research/confusion_image_aware_was.png) | [Source PDF](../assets/figures/source-pdfs/confusion_image_aware_was.pdf) | primary |
| 09 | WAS-SSL lesion-aware confusion matrix | [View PNG](../assets/figures/research/confusion_lesion_aware_was.png) | [Source PDF](../assets/figures/source-pdfs/confusion_lesion_aware_was.pdf) | primary |
| 10 | Qualitative image-level XAI | [View PNG](../assets/figures/research/xai_image_aware.png) | [Source PDF](../assets/figures/source-pdfs/xai_image_aware.pdf) | primary |
| 11 | Qualitative lesion-aware XAI | [View PNG](../assets/figures/research/xai_lesion_aware.png) | [Source PDF](../assets/figures/source-pdfs/xai_lesion_aware.pdf) | primary |
| 12 | Alternative comparison (do not conflate with WAS-SSL confusion matrices) | [View PNG](../assets/figures/research/additional_confusion_comparison.png) | [Source PDF](../assets/figures/source-pdfs/additional_confusion_comparison.pdf) | appendix |

## Figure interpretation

- **Main WAS-SSL confusion matrices** are `confusion_image_aware_was` (2,534 J1 test images) and `confusion_lesion_aware_was` (2,186 N01 validation images). Direct calculation from their displayed diagonal counts gives BACC 83.286% and 61.693%, respectively (rounded to 83.29% and 61.69%).
- **Additional confusion comparison:** The supplied `figure07_confusion.pdf` has different matrix cell counts from those two G05 WAS-SSL diagrams. It is archived only as supplementary evidence, **not** asserted to be the same ensemble prediction run. Resolve its generating model if including it in a paper.
- **Source-stratified results:** `source_stratified_bacc` uses four ISIC2019 source-attributed HAM/BCN cohorts. These are **not** independent external datasets.
- **XAI panels:** `xai_image_aware` and `xai_lesion_aware` reproduce original dermoscopic images plus Grad-CAM, Grad-CAM++ and Score-CAM overlays. These are qualitative visualizations, not pixel-level clinical localization validation.

## Copyright and clinical image reuse

The uploaded XAI figures visibly contain dermoscopic photographs. Before publicly distributing them, confirm the original image owners' terms for **redistribution of photographs and derivatives** and check whether attribution is required. If uncertain, exclude the XAI PNGs and PDFs until permissions are confirmed. The dataset sources, experimental notebooks and research paper should receive their proper citations. A public repository may be free to view while its contained data images still have separate licensing conditions.

The diagrams and plots are provided by the research author. This ZIP does not assign a new license to them.
