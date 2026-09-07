# Current Context for GPT-6 / Codex

## Purpose

This repository is a public handoff workspace for continuing a journal paper on **model-based outlier detection in continuous-time dynamic systems**. It is not the full archival research repository. The private `isheach/report` repository remains the long-term source of history; this repository contains the current materials needed to continue the work.

## Read in this order

1. `README.md`
2. `records/CURRENT_CONTEXT_FOR_GPT6.md`
3. `paper/current/Revision21_code_aligned_EN.tex`
4. `paper/current/Revision21_code_aligned_CN.tex`
5. `code/README.md`, then restore the MATLAB files
6. `voice/逐句会议记录_2026-08-31.txt`
7. `records/MEETING_KEY_POINTS.md`
8. experiment summaries in `records/`

## Current manuscript

Current working revision: **Revision 21**.

Notation/writing conventions currently in force:

- original measured output: `\bar y_k`;
- Patch repaired outputs: `\bar y_k^{(1)}, \bar y_k^{(2)}, ...`;
- do not introduce `\bar y_k^{(0)}` merely for notation uniformity;
- avoid `record` in manuscript prose; prefer `output` or `sequence` as appropriate;
- use **outlier detection** as the main term;
- do not call the Downsampling tree `recursive`;
- avoid `interleaved` for the sample partition;
- no `Variants` section;
- current redline comparison is Revision 21 versus Revision 20;
- Section III and Section IV begin with a short conceptual overview before detailed equations;
- Downsampling detection subsection wording: **Residual-Based Outlier Detection**;
- introduce the simulation system directly as “The system is ...”, not “The benchmark system ...”.

## Paper structure

- Section I — Introduction
- Section II — Problem Formulation
- Section III — Downsampling Method
- Section IV — Patch Method
- Section V — Simulation / Experiments
- Conclusion

Do not split the simulation section into unnecessary subsections unless there is a later explicit decision to do so.

## Downsampling method

Use the current synthetic MATLAB implementation as the primary algorithm reference.

High-level logic:

1. divide the sampled output by index into `K` disjoint lower-rate child sequences;
2. identify continuous-time models on child sequences and search the tree for a reliable child/model;
3. once a model is obtained, return to the original sampling rate;
4. compute one-step prediction on the original output;
5. form the original-rate residual;
6. use robust center/scale based on median and consistency-corrected MAD for pointwise outlier detection.

Current formal Downsampling does **not** include Patch-style iterative repair/re-identification. It also does not use the failed V3-C quadratic residual detrending repair.

Important known numerical issue from earlier diagnostics: rare contiguous false positives can occur in the noiseless machine-precision regime when the residual and MAD both collapse to approximately machine precision. This was diagnosed as threshold degeneration, not model-identification failure. Do not silently add an arbitrary numerical epsilon to the detector without a mathematical/numerical justification.

## Patch method

High-level logic:

1. robustly identify a continuous-time model from the current output used for identification;
2. generate one-step prediction at the original sampling rate;
3. always form the detection residual against the original measured output `\bar y_k`;
4. analyze residuals with overlapping multi-scale Patches;
5. use robust quadratic local fitting;
6. pool local scale information and form adaptive scores/thresholds;
7. require multi-scale support for detection;
8. repair detected samples using model prediction plus the estimated local residual trend;
9. re-identify the model from the repaired output;
10. iterate until convergence or the configured iteration limit.

The exact formulas and implementation details must be checked against the restored synthetic MATLAB file before changing the paper.

## Continuous-time identification

The manuscript should describe the estimation mathematically, not as a MATLAB API tutorial. The intended chain is:

continuous-time transfer function → state-space realization → ZOH sampling → one-step prediction → prediction-error criterion → stable nonlinear parameter optimization / robust prediction-error estimation.

Use `A_x, B_x, C_x, D_x` for state-space matrices so they are not confused with transfer-function polynomials `A(s)` and `B(s)`.

## Synthetic experiment

Current controlled system:

`G(s)=1/(s^2+2s+1)`

Core setup:

- sampling interval `T_s = 0.01 s`;
- 500 samples;
- unit-step input;
- 100 experiments per condition;
- outlier counts: 5, 10, 15;
- amplitude multipliers: 0.25, 0.5, 1, 2, 4.

Use `records/SYNTHETIC_RESULTS_SUMMARY.md` for the current result summary and verify any manuscript table directly against the MATLAB output before publication.

## Real-data benchmark

The real-data runner is an **adaptation** for generic time-series datasets without a physical exogenous input. It uses autoregressive/VAR-style one-step prediction and must not be presented as direct validation of continuous-time transfer-function identification.

The completed run covered 634 datasets. A known evaluation issue is that MATLAB-style F1 can be NaN when Precision=Recall=0, although on anomalous datasets the conventional classification interpretation should treat that zero-detection case as F1=0. Therefore do not publish one unqualified grand mean from the workbook without applying a clearly stated metric convention.

Use `records/REAL_DATASET_RESULTS_SUMMARY.md` for the current analysis.

## Supervisor meeting

The exact 2026-08-31 transcript is in `voice/逐句会议记录_2026-08-31.txt`. Key decisions are summarized in `records/MEETING_KEY_POINTS.md`.

Important supervisor constraints include:

- do not call the Downsampling tree process `recursive`;
- define the data partition clearly before using child/tree terminology;
- parent / child / tree concepts are acceptable;
- model, parameter estimation, prediction, and residual must follow a clear logical order;
- equations and MATLAB implementation must agree;
- final paper structure: Problem Formulation → Downsampling → Patch → Simulation.

## Working rule for future edits

When paper text and MATLAB disagree, do not silently reconcile them. Identify the exact conflict, inspect the current synthetic MATLAB implementation, and state which side should change and why. Preserve already verified algorithm behavior unless a deliberate new method change is requested.
