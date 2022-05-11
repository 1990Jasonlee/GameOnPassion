import psycopg2

conn = psycopg2.connect(
   database="gameon", user='postgres', password='password', host='127.0.0.1', port= '5432'
)
conn.autocommit = True
cursor = conn.cursor()

gamemode_info_table = '''COPY(
                           gamemode_info(mode_id, name)
                           from './gamemode_table.csv' delimiter ',' csv header;
                           )'''

mode_table = '''COPY(
                           game_gamemode(mode_id, mode1, mode2, mode3, mode4, mode5) 
                           from './game_gamemode.csv' delimiter ',' csv header;
                            )'''

mode_table1 = '''COPY(
                           SELECT game_gamemode.mode_id, gamemode_info.mode_name
                           FROM game_gamemode 
                           JOIN gamemode_info 
                           ON game_gamemode.mode1 = gamemode_info.mode_id)
                           TO './data/mode1.csv'(FORMAT csv);
                            )'''
mode_table2 = '''COPY(
                           SELECT game_gamemode.mode_id, gamemode_info.mode_name
                           FROM game_gamemode 
                           JOIN gamemode_info 
                           ON game_gamemode.mode2 = gamemode_info.mode_id)
                           TO './data/mode2.csv'(FORMAT csv);
                            )'''
mode_table3 = '''COPY(
                           SELECT game_gamemode.mode_id, gamemode_info.mode_name
                           FROM game_gamemode 
                           JOIN gamemode_info 
                           ON game_gamemode.mode3 = gamemode_info.mode_id)
                           TO './data/mode3.csv'(FORMAT csv);
                            )'''
mode_table4 = '''COPY(
                           SELECT game_gamemode.mode_id, gamemode_info.mode_name
                           FROM game_gamemode 
                           JOIN gamemode_info 
                           ON game_gamemode.mode4 = gamemode_info.mode_id)
                           TO './data/mode4.csv'(FORMAT csv);
                            )'''
mode_table5 = '''COPY(
                           SELECT game_gamemode.mode_id, gamemode_info.mode_name
                           FROM game_gamemode 
                           JOIN gamemode_info 
                           ON game_gamemode.mode5 = gamemode_info.mode_id)
                           TO './data/mode5.csv'(FORMAT csv);
                            )'''

cursor.execute(mode_table)
cursor.execute(mode_table1)
cursor.execute(mode_table2)
cursor.execute(mode_table3)
cursor.execute(mode_table4)
cursor.execute(mode_table5)
conn.commit()
conn.close()