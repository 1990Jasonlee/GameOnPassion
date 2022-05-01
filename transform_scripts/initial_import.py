import pandas as pd
import numpy as np
import json

df = pd.read_json('../data/data.json')
df.set_index("id", inplace=True)
cover_df = pd.read_json('../data/data_url.json')
cover_df.set_index("id", inplace=True)
platform_table_df = pd.read_json('../data/data_platforms.json')
platform_table_df.set_index("id", inplace=True)
genre_table_df = pd.read_json('../data/data_genre.json')
genre_table_df.set_index("id", inplace=True)
gamemode_table_df = pd.read_json('../data/data_gamemode.json')
gamemode_table_df.set_index("id", inplace=True)

df['Release Year'] = pd.to_datetime(df['first_release_date'], unit='s').dt.year
df['Score Rating'] = (df['total_rating'] + (df['total_rating_count'] / 1000)).round(2)
df = df.drop(columns=['first_release_date', 'aggregated_rating', 'aggregated_rating_count',
                      'rating', 'rating_count'])
df = df.dropna()

genre_df = pd.DataFrame(df['genres'])
split_genre = pd.DataFrame(df['genres'].values.tolist(), index=genre_df.index)
split_genre_df = split_genre.fillna(0)
split_genre_df.columns = ['g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'g9']
split_genre_df[['g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'g9']] = \
    split_genre_df[['g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'g9']].apply(lambda x: x.astype(np.int64))

platforms_df = pd.DataFrame(df['platforms'])
split_platforms = pd.DataFrame(df['platforms'].values.tolist(), index=platforms_df.index)
split_platforms_df = split_platforms.fillna(0)
split_platforms_df.columns = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13', 'p14',
                              'p15', 'p16', 'p17', 'p18', 'p19']
split_platforms_df[['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13', 'p14', 'p15',
                    'p16', 'p17', 'p18', 'p19']] = \
    split_platforms_df[['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8',
                        'p9', 'p10', 'p11', 'p12', 'p13', 'p14', 'p15',
                        'p16', 'p17', 'p18', 'p19']].apply(lambda x: x.astype(np.int64))

gamemode_df = pd.DataFrame(df['game_modes'])
split_gamemode = pd.DataFrame(df['game_modes'].values.tolist(), index=gamemode_df.index)
split_gamemode_df = split_gamemode.fillna(0)
split_gamemode_df.columns = ['gm1', 'gm2', 'gm3', 'gm4', 'gm5']
split_gamemode_df[['gm1', 'gm2', 'gm3', 'gm4', 'gm5']] = \
    split_gamemode_df[['gm1', 'gm2', 'gm3', 'gm4', 'gm5']].apply(lambda x: x.astype(np.int64))


platform_table_df.to_csv('platform_table.csv', encoding='utf-8')
genre_table_df.to_csv('genre_table.csv', encoding='utf-8')
gamemode_table_df.to_csv('gamemode_table.csv', encoding='utf-8')

split_genre_df.to_csv('game_genre.csv', encoding='utf-8')
split_gamemode_df.to_csv('game_gamemode.csv', encoding='utf-8')
split_platforms_df.to_csv('game_platform.csv', encoding='utf-8')
