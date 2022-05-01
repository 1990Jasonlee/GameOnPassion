import pandas as pd
import numpy as np

df = pd.read_json('./Data/data.json')
df.set_index("id", inplace=True)
df['Release Year'] = pd.to_datetime(df['first_release_date'], unit='s').dt.year
df['Score Rating'] = (df['total_rating'] + (df['total_rating_count'] / 1000)).round(2)
df = df.drop(columns=['first_release_date', 'aggregated_rating', 'aggregated_rating_count',
                      'rating', 'rating_count'])
df = df.dropna()

genre1 = pd.read_csv('./Data/genre1.csv', header=None)
genre1.columns = ['id', 'genre']
genre1.set_index("id", inplace=True)
genre2 = pd.read_csv('./Data/genre2.csv', header=None)
genre2.columns = ['id', 'genre']
genre2.set_index("id", inplace=True)
genre3 = pd.read_csv('./Data/genre3.csv', header=None)
genre3.columns = ['id', 'genre']
genre3.set_index("id", inplace=True)
genre4 = pd.read_csv('./Data/genre4.csv', header=None)
genre4.columns = ['id', 'genre']
genre4.set_index("id", inplace=True)
genre5 = pd.read_csv('./Data/genre5.csv', header=None)
genre5.columns = ['id', 'genre']
genre5.set_index("id", inplace=True)
genre6 = pd.read_csv('./Data/genre6.csv', header=None)
genre6.columns = ['id', 'genre']
genre6.set_index("id", inplace=True)
genre7 = pd.read_csv('./Data/genre7.csv', header=None)
genre7.columns = ['id', 'genre']
genre7.set_index("id", inplace=True)
genre8 = pd.read_csv('./Data/genre8.csv', header=None)
genre8.columns = ['id', 'genre']
genre8.set_index("id", inplace=True)
genre9 = pd.read_csv('./Data/genre9.csv', header=None)
genre9.columns = ['id', 'genre']
genre9.set_index("id", inplace=True)

gen1 = genre1['genre'].str.get_dummies().astype(int)
gen2 = genre2['genre'].str.get_dummies().astype(int)
gen3 = genre3['genre'].str.get_dummies().astype(int)
gen4 = genre4['genre'].str.get_dummies().astype(int)
gen5 = genre5['genre'].str.get_dummies().astype(int)
gen6 = genre6['genre'].str.get_dummies().astype(int)
gen7 = genre7['genre'].str.get_dummies().astype(int)
gen8 = genre8['genre'].str.get_dummies().astype(int)
gen9 = genre9['genre'].str.get_dummies().astype(int)
genres_combined = gen1.add(gen2, fill_value=0).add(gen3, fill_value=0).add(gen4, fill_value=0) \
    .add(gen5, fill_value=0).add(gen6, fill_value=0).add(gen7, fill_value=0).add(gen8, fill_value=0) \
    .add(gen9, fill_value=0).replace(np.nan, 0).astype(int)

mode1 = pd.read_csv('./Data/mode1.csv', header=None)
mode1.columns = ['id', 'Game Mode']
mode1.set_index("id", inplace=True)
mode2 = pd.read_csv('./Data/mode2.csv', header=None)
mode2.columns = ['id', 'Game Mode']
mode2.set_index("id", inplace=True)
mode3 = pd.read_csv('./Data/mode3.csv', header=None)
mode3.columns = ['id', 'Game Mode']
mode3.set_index("id", inplace=True)
mode4 = pd.read_csv('./Data/mode4.csv', header=None)
mode4.columns = ['id', 'Game Mode']
mode4.set_index("id", inplace=True)
mode5 = pd.read_csv('./Data/mode5.csv', header=None)
mode5.columns = ['id', 'Game Mode']
mode5.set_index("id", inplace=True)

gmode1 = mode1['Game Mode'].str.get_dummies().astype(int)
gmode2 = mode2['Game Mode'].str.get_dummies().astype(int)
gmode3 = mode3['Game Mode'].str.get_dummies().astype(int)
gmode4 = mode4['Game Mode'].str.get_dummies().astype(int)
gmode5 = mode5['Game Mode'].str.get_dummies().astype(int)
mode_combined = gmode1.add(gmode2, fill_value=0).add(gmode3, fill_value=0).add(gmode4, fill_value=0) \
    .add(gmode5, fill_value=0).replace(np.nan, 0).astype(int)

p1 = pd.read_csv('./Data/plat1.csv', header=None)
p1.columns = ['id', 'Platform Name']
p1.set_index("id", inplace=True)
p2 = pd.read_csv('./Data/plat2.csv', header=None)
p2.columns = ['id', 'Platform Name']
p2.set_index("id", inplace=True)
p3 = pd.read_csv('./Data/plat3.csv', header=None)
p3.columns = ['id', 'Platform Name']
p3.set_index("id", inplace=True)
p4 = pd.read_csv('./Data/plat4.csv', header=None)
p4.columns = ['id', 'Platform Name']
p4.set_index("id", inplace=True)
p5 = pd.read_csv('./Data/plat5.csv', header=None)
p5.columns = ['id', 'Platform Name']
p5.set_index("id", inplace=True)
p6 = pd.read_csv('./Data/plat6.csv', header=None)
p6.columns = ['id', 'Platform Name']
p6.set_index("id", inplace=True)
p7 = pd.read_csv('./Data/plat7.csv', header=None)
p7.columns = ['id', 'Platform Name']
p7.set_index("id", inplace=True)
p8 = pd.read_csv('./Data/plat8.csv', header=None)
p8.columns = ['id', 'Platform Name']
p8.set_index("id", inplace=True)
p9 = pd.read_csv('./Data/plat9.csv', header=None)
p9.columns = ['id', 'Platform Name']
p9.set_index("id", inplace=True)
p10 = pd.read_csv('./Data/plat10.csv', header=None)
p10.columns = ['id', 'Platform Name']
p10.set_index("id", inplace=True)
p11 = pd.read_csv('./Data/plat11.csv', header=None)
p11.columns = ['id', 'Platform Name']
p11.set_index("id", inplace=True)
p12 = pd.read_csv('./Data/plat12.csv', header=None)
p12.columns = ['id', 'Platform Name']
p12.set_index("id", inplace=True)
p13 = pd.read_csv('./Data/plat13.csv', header=None)
p13.columns = ['id', 'Platform Name']
p13.set_index("id", inplace=True)
p14 = pd.read_csv('./Data/plat14.csv', header=None)
p14.columns = ['id', 'Platform Name']
p14.set_index("id", inplace=True)
p15 = pd.read_csv('./Data/plat15.csv', header=None)
p15.columns = ['id', 'Platform Name']
p15.set_index("id", inplace=True)
p16 = pd.read_csv('./Data/plat16.csv', header=None)
p16.columns = ['id', 'Platform Name']
p16.set_index("id", inplace=True)
p17 = pd.read_csv('./Data/plat17.csv', header=None)
p17.columns = ['id', 'Platform Name']
p17.set_index("id", inplace=True)
p18 = pd.read_csv('./Data/plat18.csv', header=None)
p18.columns = ['id', 'Platform Name']
p18.set_index("id", inplace=True)
p19 = pd.read_csv('./Data/plat19.csv', header=None)
p19.columns = ['id', 'Platform Name']
p19.set_index("id", inplace=True)

plat1 = p1['Platform Name'].str.get_dummies().astype(int)
plat2 = p2['Platform Name'].str.get_dummies().astype(int)
plat3 = p3['Platform Name'].str.get_dummies().astype(int)
plat4 = p4['Platform Name'].str.get_dummies().astype(int)
plat5 = p5['Platform Name'].str.get_dummies().astype(int)
plat6 = p6['Platform Name'].str.get_dummies().astype(int)
plat7 = p7['Platform Name'].str.get_dummies().astype(int)
plat8 = p8['Platform Name'].str.get_dummies().astype(int)
plat9 = p9['Platform Name'].str.get_dummies().astype(int)
plat10 = p10['Platform Name'].str.get_dummies().astype(int)
plat11 = p11['Platform Name'].str.get_dummies().astype(int)
plat12 = p12['Platform Name'].str.get_dummies().astype(int)
plat13 = p13['Platform Name'].str.get_dummies().astype(int)
plat14 = p14['Platform Name'].str.get_dummies().astype(int)
plat15 = p15['Platform Name'].str.get_dummies().astype(int)
plat16 = p16['Platform Name'].str.get_dummies().astype(int)
plat17 = p17['Platform Name'].str.get_dummies().astype(int)
plat18 = p18['Platform Name'].str.get_dummies().astype(int)
plat19 = p19['Platform Name'].str.get_dummies().astype(int)
plat_combined = plat1.add(plat2, fill_value=0).add(plat3, fill_value=0).add(plat4, fill_value=0) \
    .add(plat5, fill_value=0).add(plat6, fill_value=0).add(plat7, fill_value=0).add(plat8, fill_value=0) \
    .add(plat9, fill_value=0).add(plat10, fill_value=0).add(plat11, fill_value=0).add(plat12, fill_value=0) \
    .add(plat13, fill_value=0).add(plat14, fill_value=0).add(plat15, fill_value=0).add(plat16, fill_value=0) \
    .add(plat17, fill_value=0).add(plat18, fill_value=0).add(plat19, fill_value=0).replace(np.nan, 0).astype(int)
plat_combined = plat_combined.rename(columns={'Arcade': 'Arcade Platform'})

# df = df.join(genres_combined).join(plat_combined).join(mode_combined)
# df_mask = df['category'] == 0
# df1 = df[df_mask]
# df_mask1 = df1['Score Rating'] >= 70
# df2 = df1[df_mask1]
# gameon_df = df2.drop(columns=['category', 'game_modes', 'genres',
#                               'platforms', 'total_rating', 'total_rating_count'])
#
# gameon_df[['Cover','Release Year', 'Score Rating', 'Adventure', 'Arcade', 'Card & Board Game',
#   'Fighting', "Hack and slash/Beat 'em up", 'Indie', 'Music', 'Pinball', 'Platform', 'Point-and-click',
#   'Puzzle', 'Quiz/Trivia', 'Racing', 'Real Time Strategy (RTS)', 'Role-playing (RPG)', 'Shooter',
#   'Simulator', 'Sport', 'Strategy', 'Tactical', 'Turn-based strategy (TBS)', 'Visual Novel',
#   '3DO Interactive Multiplayer', 'Acorn Archimedes', 'Acorn Electron', 'Amazon Fire TV', 'Amiga',
#   'Amiga CD32', 'Amstrad CPC', 'Android', 'Apple II', 'Apple IIGS', 'Arcade Platform', 'Atari 2600',
#   'Atari 8-bit', 'Atari Jaguar', 'Atari Lynx', 'Atari ST/STE', 'BBC Microcomputer System', 'BlackBerry OS',
#   'ColecoVision', 'Commodore 16', 'Commodore C64/128', 'Commodore VIC-20', 'DUPLICATE Stadia', 'DVD Player',
#   'Daydream', 'Donner Model 30', 'Dragon 32/64', 'Dreamcast', 'FM Towns', 'FM-7', 'Family Computer',
#   'Family Computer Disk System', 'Game Boy', 'Game Boy Advance', 'Game Boy Color', 'Gear VR',
#   'Google Stadia', 'Intellivision', 'Legacy Mobile Device', 'Linux', 'MSX', 'MSX2', 'Mac', 'N-Gage',
#   'NEC PC-6000 Series', 'Neo Geo AES', 'Neo Geo CD', 'Neo Geo MVS', 'New Nintendo 3DS', 'Nintendo 3DS',
#   'Nintendo 64', 'Nintendo DS', 'Nintendo DSi', 'Nintendo Entertainment System (NES)', 'Nintendo GameCube',
#   'Nintendo Switch', 'OOParts', 'Oculus Quest', 'Oculus Quest 2', 'Oculus Rift', 'Oculus VR',
#   'OnLive Game System', 'Ouya', 'PC (Microsoft Windows)', 'PC DOS', 'PC-8801', 'PC-98', 'PlayStation',
#   'PlayStation 2', 'PlayStation 3', 'PlayStation 4', 'PlayStation 5', 'PlayStation Portable',
#   'PlayStation VR', 'PlayStation Vita', 'S', 'Satellaview', 'Sega CD', 'Sega Game Gear',
#   'Sega Master System', 'Sega Mega Drive/Genesis', 'Sega Saturn', 'Sharp X1', 'Sharp X68000', 'SteamVR',
#   'Super Famicom', 'Super Nintendo Entertainment System (SNES)', 'Tapwave Zodiac', 'Tatung Einstein',
#   'TurboGrafx-16/PC Engine', 'Turbografx-16/PC Engine CD', 'Web browser', 'Wii', 'Wii U',
#   'Windows Mixed Reality', 'Windows Phone', 'WonderSwan', 'WonderSwan Color', 'Xbox', 'Xbox 360',
#   'Xbox One', 'Xbox Series X', 'ZX Spectrum', 'iOS', 'Battle Royale', 'Co-operative',
#   'Massively Multiplayer Online (MMO)', 'Multiplayer', 'Single player', 'Split screen']]=\
#     gameon_df[['Cover','Release Year', 'Score Rating', 'Adventure', 'Arcade', 'Card & Board Game',
#   'Fighting', "Hack and slash/Beat 'em up", 'Indie', 'Music', 'Pinball', 'Platform', 'Point-and-click',
#   'Puzzle', 'Quiz/Trivia', 'Racing', 'Real Time Strategy (RTS)', 'Role-playing (RPG)', 'Shooter',
#   'Simulator', 'Sport', 'Strategy', 'Tactical', 'Turn-based strategy (TBS)', 'Visual Novel',
#   '3DO Interactive Multiplayer', 'Acorn Archimedes', 'Acorn Electron', 'Amazon Fire TV', 'Amiga',
#   'Amiga CD32', 'Amstrad CPC', 'Android', 'Apple II', 'Apple IIGS', 'Arcade Platform', 'Atari 2600',
#   'Atari 8-bit', 'Atari Jaguar', 'Atari Lynx', 'Atari ST/STE', 'BBC Microcomputer System', 'BlackBerry OS',
#   'ColecoVision', 'Commodore 16', 'Commodore C64/128', 'Commodore VIC-20', 'DUPLICATE Stadia', 'DVD Player',
#   'Daydream', 'Donner Model 30', 'Dragon 32/64', 'Dreamcast', 'FM Towns', 'FM-7', 'Family Computer',
#   'Family Computer Disk System', 'Game Boy', 'Game Boy Advance', 'Game Boy Color', 'Gear VR',
#   'Google Stadia', 'Intellivision', 'Legacy Mobile Device', 'Linux', 'MSX', 'MSX2', 'Mac', 'N-Gage',
#   'NEC PC-6000 Series', 'Neo Geo AES', 'Neo Geo CD', 'Neo Geo MVS', 'New Nintendo 3DS', 'Nintendo 3DS',
#   'Nintendo 64', 'Nintendo DS', 'Nintendo DSi', 'Nintendo Entertainment System (NES)', 'Nintendo GameCube',
#   'Nintendo Switch', 'OOParts', 'Oculus Quest', 'Oculus Quest 2', 'Oculus Rift', 'Oculus VR',
#   'OnLive Game System', 'Ouya', 'PC (Microsoft Windows)', 'PC DOS', 'PC-8801', 'PC-98', 'PlayStation',
#   'PlayStation 2', 'PlayStation 3', 'PlayStation 4', 'PlayStation 5', 'PlayStation Portable',
#   'PlayStation VR', 'PlayStation Vita', 'S', 'Satellaview', 'Sega CD', 'Sega Game Gear',
#   'Sega Master System', 'Sega Mega Drive/Genesis', 'Sega Saturn', 'Sharp X1', 'Sharp X68000', 'SteamVR',
#   'Super Famicom', 'Super Nintendo Entertainment System (SNES)', 'Tapwave Zodiac', 'Tatung Einstein',
#   'TurboGrafx-16/PC Engine', 'Turbografx-16/PC Engine CD', 'Web browser', 'Wii', 'Wii U',
#   'Windows Mixed Reality', 'Windows Phone', 'WonderSwan', 'WonderSwan Color', 'Xbox', 'Xbox 360',
#   'Xbox One', 'Xbox Series X', 'ZX Spectrum', 'iOS', 'Battle Royale', 'Co-operative',
#   'Massively Multiplayer Online (MMO)', 'Multiplayer', 'Single player',
#   'Split screen']].apply(lambda x : x.astype(np.int64))
#
# header = [['Game Info', 'Game Info', 'Game Info', 'Game Info', 'Game Info', 'Genre', 'Genre', 'Genre', 'Genre',
# 'Genre', 'Genre', 'Genre', 'Genre', 'Genre', 'Genre', 'Genre', 'Genre', 'Genre', 'Genre', 'Genre', 'Genre',
# 'Genre', 'Genre', 'Genre', 'Genre', 'Genre', 'Genre', 'Platform', 'Platform', 'Platform', 'Platform', 'Platform',
# 'Platform', 'Platform', 'Platform', 'Platform', 'Platform', 'Platform', 'Platform', 'Platform', 'Platform',
# 'Platform', 'Platform', 'Platform', 'Platform', 'Platform', 'Platform', 'Platform', 'Platform', 'Platform',
# 'Platform', 'Platform', 'Platform', 'Platform', 'Platform', 'Platform', 'Platform', 'Platform', 'Platform',
# 'Platform', 'Platform', 'Platform', 'Platform', 'Platform', 'Platform', 'Platform', 'Platform', 'Platform',
# 'Platform', 'Platform', 'Platform', 'Platform', 'Platform', 'Platform', 'Platform', 'Platform', 'Platform',
# 'Platform', 'Platform', 'Platform', 'Platform', 'Platform', 'Platform', 'Platform', 'Platform', 'Platform',
# 'Platform', 'Platform', 'Platform', 'Platform', 'Platform', 'Platform', 'Platform', 'Platform', 'Platform',
# 'Platform', 'Platform', 'Platform', 'Platform', 'Platform', 'Platform', 'Platform', 'Platform', 'Platform',
# 'Platform', 'Platform', 'Platform', 'Platform', 'Platform', 'Platform', 'Platform', 'Platform', 'Platform',
# 'Platform', 'Platform', 'Platform', 'Platform', 'Platform', 'Platform', 'Platform', 'Platform', 'Platform',
# 'Platform', 'Platform', 'Platform', 'Platform', 'Platform', 'Platform', 'Platform', 'Platform', 'Platform',
# 'Game Mode', 'Game Mode', 'Game Mode', 'Game Mode', 'Game Mode', 'Game Mode'], [ 'Cover', 'Name', 'Summary',
# 'Release Year', 'Score Rating', 'Adventure', 'Arcade', 'Card & Board Game', 'Fighting', "Hack and slash/Beat 'em
# up", 'Indie', 'Music', 'Pinball', 'Platform', 'Point-and-click', 'Puzzle', 'Quiz/Trivia', 'Racing', 'Real Time
# Strategy (RTS)', 'Role-playing (RPG)', 'Shooter', 'Simulator', 'Sport', 'Strategy', 'Tactical', 'Turn-based
# strategy (TBS)', 'Visual Novel', '3DO Interactive Multiplayer', 'Acorn Archimedes', 'Acorn Electron', 'Amazon Fire
# TV', 'Amiga', 'Amiga CD32', 'Amstrad CPC', 'Android', 'Apple II', 'Apple IIGS', 'Arcade Platform', 'Atari 2600',
# 'Atari 8-bit', 'Atari Jaguar', 'Atari Lynx', 'Atari ST/STE', 'BBC Microcomputer System', 'BlackBerry OS',
# 'ColecoVision', 'Commodore 16', 'Commodore C64/128', 'Commodore VIC-20', 'DUPLICATE Stadia', 'DVD Player',
# 'Daydream', 'Donner Model 30', 'Dragon 32/64', 'Dreamcast', 'FM Towns', 'FM-7', 'Family Computer', 'Family Computer
# Disk System', 'Game Boy', 'Game Boy Advance', 'Game Boy Color', 'Gear VR', 'Google Stadia', 'Intellivision',
# 'Legacy Mobile Device', 'Linux', 'MSX', 'MSX2', 'Mac', 'N-Gage', 'NEC PC-6000 Series', 'Neo Geo AES', 'Neo Geo CD',
# 'Neo Geo MVS', 'New Nintendo 3DS', 'Nintendo 3DS', 'Nintendo 64', 'Nintendo DS', 'Nintendo DSi', 'Nintendo
# Entertainment System (NES)', 'Nintendo GameCube', 'Nintendo Switch', 'OOParts', 'Oculus Quest', 'Oculus Quest 2',
# 'Oculus Rift', 'Oculus VR', 'OnLive Game System', 'Ouya', 'PC (Microsoft Windows)', 'PC DOS', 'PC-8801', 'PC-98',
# 'PlayStation', 'PlayStation 2', 'PlayStation 3', 'PlayStation 4', 'PlayStation 5', 'PlayStation Portable',
# 'PlayStation VR', 'PlayStation Vita', 'S', 'Satellaview', 'Sega CD', 'Sega Game Gear', 'Sega Master System',
# 'Sega Mega Drive/Genesis', 'Sega Saturn', 'Sharp X1', 'Sharp X68000', 'SteamVR', 'Super Famicom', 'Super Nintendo
# Entertainment System (SNES)', 'Tapwave Zodiac', 'Tatung Einstein', 'TurboGrafx-16/PC Engine', 'Turbografx-16/PC
# Engine CD', 'Web browser', 'Wii', 'Wii U', 'Windows Mixed Reality', 'Windows Phone', 'WonderSwan', 'WonderSwan
# Color', 'Xbox', 'Xbox 360', 'Xbox One', 'Xbox Series X', 'ZX Spectrum', 'iOS', 'Battle Royale', 'Co-operative',
# 'Massively Multiplayer Online (MMO)', 'Multiplayer', 'Single player', 'Split screen']] gameon_df.columns = header
