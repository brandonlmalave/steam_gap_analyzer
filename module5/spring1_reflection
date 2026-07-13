# Spring 1 Reflection — Steam Gap Analyzer

## What I'm building
A tool that finds underserved Steam genre combinations by combining a genre-count
heuristic with a model that predicts a game's expected interest (metacritic score)
from its genre and price.

## What runs today
Right now the full pipeline runs start to finish: it fetches the Steam app list,
cleans it (dedup, drop missing names), enriches a sample of 100 games with price/
genre/metacritic data from the Steam Store API, and attempts to train a model on
that sample. Out of 100 sampled games, only 4 had a metacritic score, so the model
step correctly detects there isn't enough labeled data yet and reports that instead
of training on too few rows.

## What's broken or missing
- Not enough labeled samples per batch — most Steam games don't have a metacritic
  score, so a random 100-game sample only yields a handful of usable rows.
- No model has actually been trained yet as a result.
- The existing genre-count heuristic (from analyzer.py) still works fine on its own.

## Am I still on track?
Mostly yes — the pipeline architecture matches the charter (fetch, clean, enrich,
analyze). The one change: I need a bigger enrichment sample (or a filter that
biases toward games likely to have a score) before I can actually train anything.
Scope hasn't changed, just the sample size assumption.

## What I'm doing next
Increase the enrichment sample size (or add a filter for games with reviews) so
there are enough labeled rows to actually train the Keras model before Check-In 2.


