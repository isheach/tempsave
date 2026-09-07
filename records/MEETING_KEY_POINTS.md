# Supervisor Meeting Key Points — 2026-08-31

Source: exact transcript at `voice/逐句会议记录_2026-08-31.txt`.

The following points should guide future manuscript edits:

- Do **not** describe the Downsampling tree search as `recursive`. The supervisor reserved recursion for time/index recursion such as a relation involving `y_k` and `y_{k-1}`.
- Avoid the term `interleaved` for the Downsampling partition. Use a direct mathematical set partition. A suggested style was: divide dataset `D` into `M` disjoint subsets `D_j`.
- Parent / child / tree / leaf terminology is acceptable when the concepts are defined before use.
- The paper should clearly move through: data → partition → model → parameter estimation → prediction/residual → detection.
- Symbols and concepts should be defined before they appear in formulas.
- The continuous-time system, sampling/discretization, system identification, prediction, and residual must be explained consistently.
- The paper equations and MATLAB implementation must match.
- Residual calculation should not appear as an isolated concept detached from the identification objective.
- Use `Section`, not `Chapter`, for paper organization.
- Final method organization accepted in the meeting: Section II Problem Formulation, Section III Downsampling, Section IV Patch, then simulation.
- `Downsampling` was ultimately accepted as the method name.

For wording-level decisions or disputed interpretation, return to the exact transcript rather than relying only on this summary.
