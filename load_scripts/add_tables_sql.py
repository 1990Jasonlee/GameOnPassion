import psycopg2

conn = psycopg2.connect(
   database="gameon", user='postgres', password='password', host='127.0.0.1', port= '5432'
)
conn.autocommit = True
cursor = conn.cursor()

create_main_game = '''CREATE TABLE IF NOT EXISTS game_main(
                            id serial,
                            game_id int NOT NULL,
                            cover int NOT NULL,
                            summary VARCHAR(2200) NOT NULL,
                            year int NOT NULL,
                            Score NUMERIC(5,2) NOT NULL,
                            PRIMARY KEY(game_id)
                            )'''

create_main_genre = '''CREATE TABLE IF NOT EXISTS mode_main(
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

create_table = '''CREATE TABLE IF NOT EXISTS plat_main(
                            id serial,
                            game_id int NOT NULL,
                            3do int NOT NULL,
                            archimedes int NOT NULL,
                            electron int NOT NULL,
                            amazon int NOT NULL,
                            amiga int NOT NULL,
                            amiga_cd32 int NOT NULL,
                            amstrad int NOT NULL,
                            
                            PRIMARY KEY(game_id)
                            )'''


cursor.execute(genre_table8)
cursor.execute(genre_table9)
conn.commit()
conn.close()