import streamlit as st
import pandas as pd
import numpy as np


df = pd.read_csv('./Visual data/game_load_data.csv')
df.set_index("id", inplace=True)

def recommender(year, rating, mode, genre, platform):
    df_mask1 = ((df['Release Year'] >= year) & (df['Score Rating'] >= rating) & (df[mode]>0) & (df[genre]>0)& (df[platform]>0))
    recommend_df = df[df_mask1]
    recommend_df = recommend_df[['name', 'Release Year', 'Score Rating', 'summary']]
    recommend_df = recommend_df.sort_values(by=['Score Rating'], ascendng=False)
    return recommend_df

st.title('Video Game Recommender')
st.sidebar.header('User Input Features')
