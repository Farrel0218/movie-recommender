import pandas as pd
import random

df = pd.read_csv('movie.csv')

genre = input("Enter a genre (Action/Romance/Sci-Fi): ")

filtered = df[df['genre'].str.lower() == genre.lower()]

if not filtered.empty:
    sorted_movies = filtered.sort_values(by='rating', ascending=False)
    top_movies = sorted_movies.head(3)
    print("🎬 Top Recommendations in", genre)
    for i, row in top_movies.iterrows():
        print(f"- {row['title']} (⭐ {row['rating']})")
else:
    print("❌ Genre not found")