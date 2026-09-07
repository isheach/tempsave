# GPT-6 Paper Handoff — Continuous-Time Outlier Detection

> **Public repository notice:** this repository is public. Keep only materials intended for public AI-assisted paper handoff here. The private `isheach/report` repository remains the archival research workspace.

This repository contains the current manuscript, current MATLAB implementations, experiment summaries, and supervisor-meeting material needed to continue the paper without reconstructing the project from older chat history.

## Start here

Read in this order:

1. [`records/CURRENT_CONTEXT_FOR_GPT6.md`](records/CURRENT_CONTEXT_FOR_GPT6.md)
2. [`paper/current/Revision21_code_aligned_EN.tex`](paper/current/Revision21_code_aligned_EN.tex)
3. [`paper/current/Revision21_code_aligned_CN.tex`](paper/current/Revision21_code_aligned_CN.tex)
4. [`code/README.md`](code/README.md) and restore the MATLAB source
5. [`voice/逐句会议记录_2026-08-31.txt`](voice/逐句会议记录_2026-08-31.txt)
6. [`records/MEETING_KEY_POINTS.md`](records/MEETING_KEY_POINTS.md)
7. synthetic and real-data summaries under [`records/`](records/)

## Current status

- Current manuscript: **Revision 21**
- Current clean English source: `paper/current/Revision21_code_aligned_EN.tex`
- Current clean Chinese source: `paper/current/Revision21_code_aligned_CN.tex`
- Current review baseline: **Revision 21 vs Revision 20**
- Primary method implementation: `code/current/all_in_one_outlier_experiment_500_verified_baseline.m.gz`
- Real-data adaptation: `code/current/run_real_dataset_two_methods_fixed.m.gz`

Restore MATLAB source with:

```bash
python code/restore_current_code.py
```

## Repository layout

```text
paper/current/      Current Revision 21 LaTeX and redline sources
code/current/       Exact compressed MATLAB sources
records/            GPT-6 context, meeting notes, experiment summaries
voice/              Exact 2026-08-31 meeting transcript
meeting_audio/      Historical source audio (large; retained unchanged)
meeting_video/      Historical meeting-video placeholder/material
```

The older `paper/Revision18_notation_repair_EN.tex` is retained as a historical artifact. **Do not use Revision 18 as the current manuscript.**

## Method authority

For the paper's continuous-time methods, the synthetic verified MATLAB implementation is the primary code reference. The real-dataset runner adapts the detection frameworks to generic time series with autoregressive/VAR-style prediction and must not replace the continuous-time formulation in the manuscript.

## Working rule

If LaTeX and MATLAB disagree, do not silently guess. Identify the conflict, inspect the current synthetic implementation, and resolve the mismatch explicitly before editing the manuscript.
