import pandas as pd

def analyze_genres(df):
    # Counts games per genre 
    name_counts = df["genres"].value_counts()

    print("Game Distribution:")
    print(name_counts)

    return name_counts

def find_gaps(df):
    # game genres out of 500 samples 
    name_counts = df["genres"].value_counts()

    # Bottom 25% by game count = potential gaps
    threshold = name_counts.quantile(0.25)

    underserved = name_counts[name_counts <= threshold]

    print(f"\nUnderserved games (low competition):")
    print(underserved)

    return underserved

if __name__ == "__main__":
    print("This file is a tool, import it from steam_api.py")