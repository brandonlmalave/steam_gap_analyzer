[README (3).md](https://github.com/user-attachments/files/32974917/README.3.md)
# Steam Gap Analyzer

A Python tool that pulls game data from Steam, cleans and enriches it, and looks for **underserved genre combinations**: types of games that few developers are making, which could point to gaps in the market.

## Why
Steam has tens of thousands of games, but they aren't spread evenly across genres. This project asks: *which genre combinations have the least competition?* The next step is to pair that with a predicted-interest signal, so a "gap" means low competition **and** likely player interest, not just "nobody has made this yet."

## How It Works

```
Steam Web API ──► Clean ──► Enrich (sample) ──► Analyze gaps
```

1. **Fetch** (`steam_api.py`): Pulls the full Steam app list (up to 50,000 games) from the `IStoreService/GetAppList` endpoint.
2. **Clean** (`cleaner.py`): Removes duplicate app IDs and games with missing or blank names.
3. **Enrich** (`enricher.py`): Takes a random sample and calls the Steam Store `appdetails` API for each game to get its type, price, genres, and Metacritic score. Requests are rate-limited so the tool doesn't overload Steam's servers.
4. **Analyze** (`analyzer.py`): Counts games per genre combination and flags the bottom 25% by count as underserved.
An experimental model (`model.py`) is also included. See **Future Work** below.

## Project Structure

| File | Purpose |
|---|---|
| `steam_api.py` | Entry point: fetches the app list and runs the full pipeline |
| `cleaner.py` | Data cleaning functions |
| `enricher.py` | Fetches per-game details from the Steam Store API |
| `analyzer.py` | Genre distribution and gap detection |
| `model.py` | Predictive model (Keras) |
| `charter.md` | Project scope, definition of done, and what's out of scope |
| `backlog.md` | Planned work for the modeling phase |
| `reflection.md`, `spring1_reflection.md` | Progress reflections and lessons learned |

## Getting Started

**Requirements:** Python 3.10+ and a free [Steam Web API key](https://steamcommunity.com/dev/apikey).

```bash
pip install -r requirements.txt
```

Set your API key as an environment variable (never commit it to the repo):

```bash
# macOS / Linux
export STEAM_API_KEY="your_key_here"

# Windows (PowerShell)
$env:STEAM_API_KEY="your_key_here"
```

Run the pipeline:

```bash
python steam_api.py   # fetch, clean, enrich, and find gaps
python model.py       # experimental: attempt to train the predictive model
```

## Status
The core pipeline is complete: it runs end to end, from fetching live Steam data to flagging underserved genre combinations, and the results are reproducible.

## Future Work
The next phase is a predictive model so that a "gap" means low competition **and** likely player interest. `model.py` contains an early version: a Keras neural network that predicts a game's Metacritic score from its genres and price, to be evaluated against a naive per-genre-average baseline using mean absolute error (MAE).

**What I learned so far:** most Steam games don't have a Metacritic score. A random 100-game sample produced only 4 labeled rows, so the model step detects this and skips training rather than fitting on too little data. A better interest signal, like Steam user review scores, would likely fix this.

Planned steps:
- [ ] Switch to (or add) a more widely available interest signal, such as Steam user review scores
- [ ] Compute a naive per-genre-mean baseline MAE
- [ ] Train the Keras model and compare it to the baseline
- [ ] Identify the epoch where validation MAE stops improving
- [ ] Combine predicted interest with the count-based heuristic for a stronger gap signal

## Scope
To keep the project focused, it intentionally does **not** fetch details for every game (it uses a rate-limited sample), build a recommendation engine or dashboard, or handle every currency and pricing edge case.

## Tech
Python, pandas, Requests, Keras/TensorFlow, scikit-learn, Steam Web API

## Author
Brandon Malave – [GitHub](https://github.com/brandonlmalave)
