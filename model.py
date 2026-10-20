
 
import pandas as pd
from tensorflow import keras
from sklearn.model_selection import train_test_split
from steam_api import get_all_games
from cleaner import clean_games
from enricher import enrich_games
 
 
def price_to_float(price_str):
    if not price_str or price_str == "Free":
        return 0.0
    try:
        return float(price_str.replace("$", "").replace(",", ""))
    except (ValueError, AttributeError):
        return None
 
 
def prepare_data(df):
    # Only keep rows where we actually have a score to predict
    df = df.dropna(subset=["metacritic"]).copy()

    df["price_num"] = df["price"].apply(price_to_float)
    df = df.dropna(subset=["price_num"])
 
    # Turn comma-separated genres into one-hot columns
    genre_dummies = df["genres"].str.get_dummies(sep=", ")
 
    X = pd.concat([genre_dummies, df["price_num"]], axis=1)
    y = df["metacritic"]
 
    return X, y
 
 
def build_model(input_dim):
    model = keras.Sequential([
        keras.layers.Dense(16, activation="relu", input_shape=(input_dim,)),
        keras.layers.Dense(1)
    ])
    model.compile(optimizer="adam", loss="mse", metrics=["mae"])
    return model
 
 
if __name__ == "__main__":
    print("Fetching and preparing data...")
    games = get_all_games()
    cleaned = clean_games(games)
    enriched = enrich_games(cleaned, sample_size=100)
 
    X, y = prepare_data(enriched)
    print(f"Usable training samples (had a metacritic score): {len(X)}")
 
    if len(X) < 10:
        print("Not enough labeled samples yet -- this is expected at this stage.")
    else:
        X_train, X_val, y_train, y_val = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
 
        model = build_model(X.shape[1])
        model.fit(X_train, y_train, epochs=10,
                   validation_data=(X_val, y_val), verbose=1)
 
        preds = model.predict(X_val[:5])
        print("\nSample predictions vs actual metacritic scores:")
        for p, a in zip(preds, y_val[:5]):
            print(f"Predicted: {p[0]:.1f}  Actual: {a}")
 
