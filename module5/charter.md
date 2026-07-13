# Project Charter: Steam Gap Analyzer

## What we're building (one sentence)
A tool that pulls Steam game data, cleans it, enriches it with price/review/genre details, and identifies underserved genre combinations — genres with low game counts but (once modeled) high predicted player interest.

## Cohort
Tabular

## The data or tools we'll use
- Steam Web API (`IStoreService/GetAppList`) for the full game list
- Steam Store API (`appdetails`) to enrich a sample with price, metacritic score, and genres
- pandas for cleaning (dedup by appid, drop missing names) and aggregation
- Keras for the predictive model (Module 6)
- k-fold or train/val split for honest evaluation

## Definition of "good enough"
Before we build further, we agree this project is good enough when:
- The current heuristic (genre counts, bottom-25%-by-count = "underserved") is working and reproducible — **done**
- A trained model predicts a game's metacritic score (or another interest signal) from its genre + price, with validation MAE beating a naive per-genre-mean baseline
- Validation MAE stops improving (turnaround epoch identified)
- The combined output (low game count + high predicted score) is a more meaningful "gap" signal than count alone, and makes sense on spot-check

## What we are NOT doing (scope guard)
- Not fetching detail data for all 50k games — sticking with a rate-limited sample (currently 100) to avoid hammering Steam's servers
- Not building a full recommendation engine or live dashboard
- Not handling every price/currency edge case — treating "Free" and formatted price strings as-is for now

## Team & roles
Solo — Brandon Malave
