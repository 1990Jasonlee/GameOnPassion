import psycopg2

conn = psycopg2.connect(
   database="postgres", user='postgres', password='password', host='127.0.0.1', port= '5432'
)
conn.autocommit = True
cursor = conn.cursor()
cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'gameon'")
exists = cursor.fetchone()
print('database exist')
if not exists:
    cursor.execute('CREATE DATABASE gameon')
conn.close()

conn = psycopg2.connect(
   database="gameon", user='postgres', password='password', host='127.0.0.1', port= '5432'
)
conn.autocommit = True

cursor.execute('DROP TABLE IF EXISTS "game_gamemode";')
create_table = '''CREATE TABLE IF NOT EXISTS game_gamemode(
                            id serial,
                            user_id int NOT NULL,
                            mode_id int NOT NULL,
                            mode1 int NOT NULL,
                            mode2 int NOT NULL,
                            mode3 int NOT NULL,
                            mode4 int NOT NULL,
                            mode5 int NOT NULL,
                            PRIMARY KEY(user_id)
                            )'''

cursor.execute('DROP TABLE IF EXISTS "game_genre";')
create_table1 = '''CREATE TABLE IF NOT EXISTS game_genre(
                            id serial,
                            game_id int NOT NULL,
                            genre1 int NOT NULL,
                            genre2 int NOT NULL,
                            genre3 int NOT NULL,
                            genre4 int NOT NULL,
                            genre5 int NOT NULL,
                            genre6 int NOT NULL,
                            genre7 int NOT NULL,
                            genre8 int NOT NULL,
                            genre9 int NOT NULL,
                            PRIMARY KEY(game_id)
                            )'''

cursor.execute('DROP TABLE IF EXISTS "game_platform";')
create_table2 = '''CREATE TABLE IF NOT EXISTS game_platform(
                            user_id serial,
                            plat_id int NOT NULL,
                            plat_1 int NOT NULL,
                            plat_2 int NOT NULL,
                            plat_3 int NOT NULL,
                            plat_4 int NOT NULL,
                            plat_5 int NOT NULL,
                            plat_6 int NOT NULL,
                            plat_7 int NOT NULL,
                            plat_8 int NOT NULL,
                            plat_9 int NOT NULL,
                            plat_10 int NOT NULL,                            
                            plat_11 int NOT NULL,
                            plat_12 int NOT NULL,
                            plat_13 int NOT NULL,
                            plat_14 int NOT NULL,
                            plat_15 int NOT NULL,
                            plat_16 int NOT NULL,
                            plat_17 int NOT NULL,
                            plat_18 int NOT NULL,
                            plat_19 int NOT NULL,
                            PRIMARY KEY(plat_id)
                            )'''

cursor.execute('DROP TABLE IF EXISTS "gamemode_info";')
create_table3 = '''CREATE TABLE IF NOT EXISTS gamemode_info(
                            id serial,
                            mode_id int NOT NULL,
                            mode_name VARCHAR(100) NOT NULL,
                            PRIMARY KEY(mode_id)
                            )'''

cursor.execute('DROP TABLE IF EXISTS "genre_info";')
create_table4 = '''CREATE TABLE IF NOT EXISTS genre_info(
                            id serial,
                            genre_id int NOT NULL,
                            genre_name VARCHAR(100) NOT NULL,
                            PRIMARY KEY(genre_id)
                            )'''
cursor.execute('DROP TABLE IF EXISTS "platform_info";')
create_table5 = '''CREATE TABLE IF NOT EXISTS platform_info(
                            id serial,
                            platform_id int NOT NULL,
                            platform_name VARCHAR(100) NOT NULL,
                            PRIMARY KEY(platform_id)
                            )'''
cursor.execute(create_table)
cursor.execute(create_table1)
cursor.execute(create_table2)
cursor.execute(create_table3)
cursor.execute(create_table4)
cursor.execute(create_table5)
conn.commit()
conn.close()
