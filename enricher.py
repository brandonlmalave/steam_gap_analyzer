import requests
import time
import pandas as pd

# How many games to enrich per run, and the seed that makes the sample repeatable
# Sample size can be changed, higher number for better results, but slower
SAMPLE_SIZE = 100
RANDOM_SEED = 42

# Seconds to wait between Store API requests so Steam doesn't block us
REQUEST_DELAY = 0.5


def get_game_details(appid):
    url = "https://store.steampowered.com/api/appdetails"

    try:
        response = requests.get(url, params={"appids": appid}, timeout=10)
    except requests.RequestException:
        return None

    if response.status_code != 200:
        return None

    data = response.json()

    app_data = data.get(str(appid), {})
    if not app_data.get("success", False):
        return None

    game = app_data["data"]

    name = game.get("name", None)
    game_type = game.get("type", None)
    price = game.get("price_overview", {}).get("final_formatted", "Free")
    metacritic = game.get("metacritic", {}).get("score", None)

    genres = game.get("genres", [])
    genre_names = ", ".join([g["description"] for g in genres])

    return {
        "appid": appid,
        "name": name,
        "type": game_type,
        "price": price,
        "metacritic": metacritic,
        "genres": genre_names
    }


def enrich_games(df, sample_size=SAMPLE_SIZE, seed=RANDOM_SEED):
    # Take a random sample so we don't hammer Steam's servers.
    # The seed picks the same games every run, as long as the app list hasn't changed.
    sample = df.sample(sample_size, random_state=seed)

    enriched = []

    for index, row in sample.iterrows():
        print(f"Fetching details for: {row['name']}")

        details = get_game_details(row["appid"])

        if details:
            enriched.append(details)

        # Pause between requests so Steam doesn't block us
        time.sleep(REQUEST_DELAY)

    return pd.DataFrame(enriched)


if __name__ == "__main__":
    print("This file is a tool, import it from steam_api.py")
