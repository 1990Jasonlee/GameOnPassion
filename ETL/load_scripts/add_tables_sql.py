import psycopg2

conn = psycopg2.connect(
   database="gameon", user='postgres', password='password', host='127.0.0.1', port= '5432'
)
conn.autocommit = True
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS "game_main";')

# create game database
create_main_game = '''CREATE TABLE IF NOT EXISTS game_main(
                            id serial,
                            game_id int NOT NULL,
                            cover int NOT NULL,
                            summary VARCHAR(2200) NOT NULL,
                            year int NOT NULL,
                            Score NUMERIC(5,2) NOT NULL,
                            PRIMARY KEY(game_id)
                            )'''
cursor.execute('DROP TABLE IF EXISTS "mode_main";')
# create game mode database
create_main_mode = '''CREATE TABLE IF NOT EXISTS mode_main(
                            id serial,
                            game_id int NOT NULL,
                            battle_royale int NOT NULL,
                            co_op int NOT NULL,
                            mmo int NOT NULL,
                            multiplayer int NOT NULL,
                            single_player int NOT NULL,
                            split_screen int NOT NULL,                            
                            PRIMARY KEY(game_id)
                            )'''
cursor.execute('DROP TABLE IF EXISTS "plat_main";')

# create platform database
create_main_plat = '''CREATE TABLE IF NOT EXISTS plat_main(
                            id serial,
                            game_id int NOT NULL,
                            3do int NOT NULL,
                            archimedes int NOT NULL,
                            electron int NOT NULL,
                            amazon int NOT NULL,
                            amiga int NOT NULL,
                            amiga_cd32 int NOT NULL,
                            amstrad int NOT NULL,
                            android int NOT NULL,
                            apple_ii int NOT NULL,
                            apple_iigs int NOT NULL,
                            arcade_platform int NOT NULL,
                            atari_2600 int NOT NULL,
                            atari_8 int NOT NULL,
                            atari_jag int NOT NULL,
                            atari_lynx int NOT NULL,
                            atari_ste int NOT NULL,
                            bbc int NOT NULL,
                            blackberry int NOT NULL,
                            colecovision int NOT NULL,
                            commodore_16 int NOT NULL,
                            commodore_c64 int NOT NULL,
                            commodore_vic int NOT NULL,
                            stadia int NOT NULL,
                            dvd int NOT NULL,
                            daydream int NOT NULL,
                            donner int NOT NULL,
                            dragon int NOT NULL,
                            dreamcast int NOT NULL,
                            fm_towns int NOT NULL,
                            fm_7 int NOT NULL,
                            family int NOT NULL,
                            family_ds int NOT NULL,
                            gameboy int NOT NULL,
                            gameboy_color int NOT NULL,
                            gameboy_advance int NOT NULL,
                            gear_vr int NOT NULL,
                            google_stadia int NOT NULL,
                            intellivision int NOT NULL,
                            legacy int NOT NULL,
                            linux int NOT NULL,
                            msx int NOT NULL,
                            msx2 int NOT NULL,
                            mac int NOT NULL,
                            n_gage int NOT NULL,
                            nec int NOT NULL,
                            neogeo_aes int NOT NULL,
                            negeo_cd int NOT NULL,
                            negeo_mvs int NOT NULL,
                            new_n3ds int NOT NULL,
                            n3ds int NOT NULL,
                            n64 int NOT NULL,
                            nds int NOT NULL,
                            ndsi int NOT NULL,
                            nes int NOT NULL,
                            gamecube int NOT NULL,
                            switch int NOT NULL,
                            ooparts int NOT NULL,
                            oculus int NOT NULL,
                            oculus2 int NOT NULL,
                            oculus_rift int NOT NULL,
                            oculus_vr int NOT NULL,
                            onlive int NOT NULL,
                            ouya int NOT NULL,
                            pc int NOT NULL,
                            pc_dos int NOT NULL,
                            pc_8801 int NOT NULL,
                            pc-98 int NOT NULL,
                            playstation int NOT NULL,
                            ps2 int NOT NULL,
                            ps3 int NOT NULL,
                            ps4 int NOT NULL,
                            ps5 int NOT NULL,
                            psp int NOT NULL,
                            playstation_vr int NOT NULL,
                            psv int NOT NULL,
                            s int NOT NULL,
                            satellaview int NOT NULL,
                            sega int NOT NULL,
                            sega_gamegear int NOT NULL,
                            sega_master int NOT NULL,
                            sega_mega int NOT NULL,
                            sega_saturn int NOT NULL,
                            sharpx1 int NOT NULL,
                            sharpx68000 int NOT NULL,
                            steam_vr int NOT NULL,
                            snes int NOT NULL,
                            tapwave int NOT NULL,
                            tatung int NOT NULL,
                            turbografx int NOT NULL,
                            turbografx_cd int NOT NULL,
                            web int NOT NULL,
                            wii int NOT NULL,
                            wii_u int NOT NULL,
                            mixed_reality int NOT NULL,
                            windows_phone int NOT NULL,
                            wonderswan int NOT NULL,
                            wonderswan_color int NOT NULL,
                            xbox int NOT NULL,
                            xbox360 int NOT NULL,
                            xbox_one int NOT NULL,
                            xbox_x int NOT NULL,
                            zx_spectrum int NOT NULL,
                            ios int NOT NULL,
                            PRIMARY KEY(game_id)
                            )'''
cursor.execute('DROP TABLE IF EXISTS "genre_main";')

# create genre database
create_main_genre = '''CREATE TABLE IF NOT EXISTS genre_main(
                            id serial,
                            game_id int NOT NULL,
                            adventure int NOT NULL,
                            arcade int NOT NULL,
                            card_board int NOT NULL,
                            fighting int NOT NULL,
                            hack_slash int NOT NULL,
                            indie int NOT NULL,                            
                            music int NOT NULL,                            
                            pinball int NOT NULL,                            
                            platform_game int NOT NULL,                            
                            point_click int NOT NULL,                            
                            puzzle int NOT NULL,                            
                            quiz int NOT NULL,                            
                            racing int NOT NULL,                            
                            rts int NOT NULL,                            
                            rpg int NOT NULL,                            
                            shooter int NOT NULL,                            
                            simulator int NOT NULL,                            
                            sports int NOT NULL,                            
                            strategy int NOT NULL,                            
                            tactical int NOT NULL,                            
                            tbs int NOT NULL,                            
                            visual_novel int NOT NULL,                                 
                            PRIMARY KEY(game_id)
                            )'''
cursor.execute(create_main_genre)
cursor.execute(create_main_plat)
cursor.execute(create_main_mode)
cursor.execute(create_main_game)
conn.commit()
conn.close()
