import os
import sys

import requests
import pandas as pd
from cleaner import clean_games
from analyzer import analyze_genres, find_gaps
from enricher import enrich_games, SAMPLE_SIZE

# Read the key from an environment variable so it never ends up in the repo
API_KEY = os.environ.get("STEAM_API_KEY")


def get_all_games():
    if not API_KEY:
        sys.exit("STEAM_API_KEY is not set. See 'Getting Started' in README.md.")

    url = "https://api.steampowered.com/IStoreService/GetAppList/v1/"
    params = {"key": API_KEY, "max_results": 50000, "include_games": "true"}

    response = requests.get(url, params=params, timeout=30)

    print(f"Status Code: {response.status_code}")

    if response.status_code != 200:
        sys.exit(f"Steam returned an error. Check that your API key is valid. "
                 f"Response: {response.text[:200]}")

    data = response.json()

    apps = data["response"]["apps"]

    df = pd.DataFrame(apps)

    return df


if __name__ == "__main__":
    print("Fetching games from Steam...")
    games = get_all_games()
    print(f"Raw games found: {len(games)}")

    cleaned = clean_games(games)
    print(f"Cleaned games: {len(cleaned)}")

    print(f"Enriching sample of {SAMPLE_SIZE} games...")
    enriched = enrich_games(cleaned)
    print(f"Enriched games: {len(enriched)}")
    print(enriched.head())

    analyze_genres(enriched)
    find_gaps(enriched)
