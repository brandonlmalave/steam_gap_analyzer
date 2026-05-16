import requests
import pandas as pd
from cleaner import clean_games
from analyzer import analyze_genres, find_gaps
from enricher import get_game_details, enrich_games

API_KEY = "API_KEY_HERE"

def get_all_games():
    url = f"https://api.steampowered.com/IStoreService/GetAppList/v1/?key={API_KEY}&max_results=50000&include_games=true"

    response = requests.get(url)

    print(f"Status Code: {response.status_code}")
    print(f"Response preview: {response.text[:200]}")

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

    print("Enriching sample of 500 games...")
    enriched = enrich_games(cleaned)
    print(f"Enriched games: {len(enriched)}")
    print(enriched.head())

    analyze_genres(enriched)
    find_gaps(enriched)