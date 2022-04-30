import pandas as pd
import numpy as np
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

pd.platform_table_df.to_csv('platform_table.csv', encoding='utf-8')
pd.genre_table_df.to_csv('genre_table.csv', encoding='utf-8')
pd.gamemode_table_df.to_csv('gamemode_table.csv', encoding='utf-8')

pd.split_genre_df.to_csv('game_genre.csv', encoding='utf-8')
pd.split_gamemode_df.to_csv('game_gamemode.csv', encoding='utf-8')
pd.split_platforms_df.to_csv('game_platform.csv', encoding='utf-8')
