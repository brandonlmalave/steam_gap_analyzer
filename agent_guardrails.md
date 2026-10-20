# Agent Guardrails — Steam Gap Analyzer

Rules for my AI assistant while working on this project:

1. Stick to the scope in charter.md — don't suggest features listed under "What we are NOT doing."
2. Never hardcode API keys in committed code — always use environment variables.
3. When adding the predictive model, use the same evaluation approach as
   California Housing: train/val split (or k-fold), MAE as the metric,
   compare against a naive per-genre-mean baseline.
4. Explain changes in plain language before writing code — I want to
   understand what's happening, not just get code dropped in.
5. Flag if a suggested change would break the existing cleaner/enricher/
   analyzer pipeline instead of building on top of it.
