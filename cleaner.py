import pandas as pd

def clean_games(df):
    # Remove duplicate games
    df = df.drop_duplicates(subset="appid")

    # Remove games with no name
    df = df.dropna(subset=["name"])

    # Remove empty string names
    df = df[df["name"].str.strip() != ""]

    # Reset index so it's clean after all removals
    df = df.reset_index(drop=True)

    print(f"Games after cleaning: {len(df)}")

    return df

if __name__ == "__main__":
    print("This file is a tool, import it from steam_api.py")
