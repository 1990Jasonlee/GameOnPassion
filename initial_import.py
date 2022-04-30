import pandas as pd
import numpy as np
import json

df = pd.read_json('./Data/data.json')
df.set_index("id", inplace=True)
cover_df = pd.read_json('./Data/data_url.json')
cover_df.set_index("id", inplace=True)
platform_table_df = pd.read_json('./Data/data_platforms.json')
platform_table_df.set_index("id", inplace=True)
genre_table_df = pd.read_json('./Data/data_genre.json')
genre_table_df.set_index("id", inplace=True)
gamemode_table_df = pd.read_json('./Data/data_gamemode.json')
gamemode_table_df.set_index("id", inplace=True)

df['Release Year'] = pd.to_datetime(df['first_release_date'], unit='s').dt.year
df['Score Rating'] = (df['total_rating'] + (df['total_rating_count'] / 1000)).round(2)
df = df.drop(columns=['first_release_date', 'aggregated_rating', 'aggregated_rating_count',
                      'rating', 'rating_count'])

df = df.dropna()
