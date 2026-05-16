import requests
import time 
import pandas as pd 

def get_game_details(appid): 
    url = f"https://store.steampowered.com/api/appdetails?appids={appid}"

    response =  requests.get(url)

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

def enrich_games(df, sample_size=100):
    # Take a random sample so we don't hammer Steam's servers
    sample = df.sample(sample_size)
    
    enriched = []
    
    for index, row in sample.iterrows():
        print(f"Fetching details for: {row['name']}")
        
        details = get_game_details(row["appid"])
        
        if details:
            enriched.append(details)
        
        # Wait 1 second between each request so Steam doesn't block us
        time.sleep(0.5)
    
    return pd.DataFrame(enriched)



if __name__ == "__main__":
    print("This file is a tool, import it from steam_api.py")



   