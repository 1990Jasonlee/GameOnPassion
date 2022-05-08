import streamlit as st
import pandas as pd

df = pd.read_csv('/Users/jason/dev/GameOnPassion/Visual data/game_load_data.csv')
df.set_index("id", inplace=True)
df = df.rename(columns={'name': 'Name', 'summary': 'Summary'})
st.title('Video Game Recommender')
st.sidebar.header('User Input Features')

years_sorted = sorted(list(df['Release Year'].unique()))
year = st.sidebar.slider('Year', int(years_sorted[0]), int(years_sorted[-1]), step=int(1))
rating = st.sidebar.slider('Rating', 75, 100)
mode = st.sidebar.radio('Game Mode',
                        ['Single player', 'Battle Royale', 'Co-operative', 'Massively Multiplayer Online (MMO)',
                         'Multiplayer', 'Split screen'])
genre = st.sidebar.selectbox('Genre', ['Adventure', 'Arcade', 'Card & Board Game', 'Fighting',
                                       "Hack and slash/Beat 'em up", 'Indie', 'Music', 'Pinball', 'Platform',
                                       'Point-and-click', 'Puzzle', 'Quiz/Trivia', 'Racing', 'Real Time Strategy (RTS)',
                                       'Role-playing (RPG)', 'Shooter', 'Simulator', 'Sport', 'Strategy', 'Tactical',
                                       'Turn-based strategy (TBS)', 'Visual Novel'])
platform = st.sidebar.selectbox('Platform', ['3DO Interactive Multiplayer', 'Acorn Archimedes', 'Acorn Electron',
                                             'Amazon Fire TV', 'Amiga', 'Amiga CD32', 'Amstrad CPC', 'Android',
                                             'Apple II', 'Apple IIGS', 'Arcade Platform', 'Atari 2600', 'Atari 8-bit',
                                             'Atari Jaguar', 'Atari Lynx', 'Atari ST/STE', 'BBC Microcomputer System',
                                             'BlackBerry OS', 'ColecoVision', 'Commodore 16', 'Commodore C64/128',
                                             'Commodore VIC-20', 'DUPLICATE Stadia', 'DVD Player', 'Daydream',
                                             'Donner Model 30', 'Dragon 32/64', 'Dreamcast', 'FM Towns', 'FM-7',
                                             'Family Computer', 'Family Computer Disk System', 'Game Boy',
                                             'Game Boy Advance', 'Game Boy Color', 'Gear VR', 'Google Stadia',
                                             'Intellivision', 'Legacy Mobile Device', 'Linux', 'MSX', 'MSX2',
                                             'Mac', 'N-Gage', 'NEC PC-6000 Series', 'Neo Geo AES', 'Neo Geo CD',
                                             'Neo Geo MVS', 'New Nintendo 3DS', 'Nintendo 3DS', 'Nintendo 64',
                                             'Nintendo DS', 'Nintendo DSi', 'Nintendo Entertainment System (NES)',
                                             'Nintendo GameCube', 'Nintendo Switch', 'OOParts', 'Oculus Quest',
                                             'Oculus Quest 2', 'Oculus Rift', 'Oculus VR', 'OnLive Game System', 'Ouya',
                                             'PC (Microsoft Windows)', 'PC DOS', 'PC-8801', 'PC-98', 'PlayStation',
                                             'PlayStation 2', 'PlayStation 3', 'PlayStation 4', 'PlayStation 5',
                                             'PlayStation Portable', 'PlayStation VR', 'PlayStation Vita', 'S',
                                             'Satellaview', 'Sega CD', 'Sega Game Gear', 'Sega Master System',
                                             'Sega Mega Drive/Genesis', 'Sega Saturn', 'Sharp X1', 'Sharp X68000',
                                             'SteamVR', 'Super Famicom', 'Super Nintendo Entertainment System (SNES)',
                                             'Tapwave Zodiac', 'Tatung Einstein', 'TurboGrafx-16/PC Engine',
                                             'Turbografx-16/PC Engine CD', 'Web browser', 'Wii', 'Wii U',
                                             'Windows Mixed Reality', 'Windows Phone', 'WonderSwan', 'WonderSwan Color',
                                             'Xbox', 'Xbox 360', 'Xbox One', 'Xbox Series X', 'ZX Spectrum', 'iOS'])


def recommender(year, rating, mode, genre, platform):
    df_mask1 = ((df['Release Year'] >= year) & (df['Score Rating'] >= rating) & (df[mode] > 0) & (df[genre] > 0) & (
                df[platform] > 0))
    recommend_df = df[df_mask1]
    recommend_df = recommend_df[['Name', 'Release Year', 'Score Rating', 'Summary']]
    st.dataframe(recommend_df.style.format({'Score Rating': '{:.2f}'}), width=5000, height=1000)
    return recommend_df


if st.sidebar.button('Generate recommendations'):
    st.write(f'You have chosen to look video games based on the following criteria ')
    st.write(f'Genre: {genre} ')
    st.write(f'Game Mode: {mode} ')
    st.write(f'Year equal to or newer than: {year} ')
    st.write(f'Rating equal to or over: {rating} ')
    st.success('Here are your recommendations')
    recommender(year, rating, mode, genre, platform)