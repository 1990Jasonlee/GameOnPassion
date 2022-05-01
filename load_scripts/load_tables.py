import psycopg2

conn = psycopg2.connect(
   database="gameon", user='postgres', password='password', host='127.0.0.1', port='5432'
)
conn.autocommit = True
cursor = conn.cursor()


load_game = '''COPY(
                     game_main(game_id, cover, summary, year, Score)
                     from './gamemode_table.csv' delimiter ',' csv header;
                     )'''


load_genre = '''COPY(
                     genre_main(game_id, adventure, arcade, card_board, fighting, hack_slash, indie, music,
                     pinball, platform_game, point_click, puzzle, quiz, racing, rts, rpg, shooter, simulator, sports,
                     strategy, tactical, tbs, visual_novel)
                     from './genre_load_data.csv' delimiter ',' csv header;
                     )'''

load_mode = '''COPY(
                     mode_main(game_id, battle_royale, co_op, mmo, multiplayer, single_player, split_screen) 
                     from './game_gamemode.csv' delimiter ',' csv header;
                      )'''

load_plat = '''COPY(
                     plat_main(game_id, 3do, archimedes, electron, amazon, amiga, amiga_cd32, amstrad, android, 
                     apple_ii, apple_iigs, arcade_platform, atari_2600, atari_8, atari_jag, atari_lynx, atari_ste, bbc, 
                     blackberry, colecovision, commodore_16, commodore_c64, commodore_vic, stadia, dvd, daydream, 
                     donner, dragon, dreamcast, fm_towns, fm_7, family, family_ds, gameboy, gameboy_color, 
                     gameboy_advance, gear_vr, google_stadia, intellivision, legacy, linux, msx, msx2, mac, n_gage, 
                     nec, neogeo_aes, negeo_cd, negeo_mvs, new_n3ds, n3ds, n64, nds, ndsi, nes, gamecube, switch, 
                     ooparts, oculus, oculus2, oculus_rift, oculus_vr, onlive, ouya, pc, pc_dos, pc_8801, pc - 98, 
                     playstation, ps2, ps3, ps4, ps5, psp, playstation_vr, psv, s, satellaview, sega, sega_gamegear, 
                     sega_master, sega_mega, sega_saturn, sharpx1, sharpx68000, steam_vr, snes, tapwave, tatung, 
                     turbografx, turbografx_cd, web, wii, wii_u, mixed_reality, windows_phone, wonderswan, 
                     wonderswan_color, xbox, xbox360, xbox_one, xbox_x, zx_spectrum, ios) 
                     from './plat_load_data.csv' delimiter ',' csv header;
                      )'''


cursor.execute(load_game)
cursor.execute(load_genre)
cursor.execute(load_mode)
cursor.execute(load_plat)

conn.commit()
conn.close()
