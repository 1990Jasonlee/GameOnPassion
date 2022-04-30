import psycopg2

conn = psycopg2.connect(
   database="gameon", user='postgres', password='password', host='127.0.0.1', port= '5432'
)
conn.autocommit = True
cursor = conn.cursor()

genre_info_table = '''COPY(
                           genre_info(genre_id, name)
                           from './genre_table.csv' delimiter ',' csv header;
                           )'''

genre_table = '''COPY(
                           game_genre(game_id, genre1, genre2, genre3, genre4, 
                           genre5, genre6, genre7, genre8, genre9) 
                           from './game_genre.csv' delimiter ',' csv header;
                           )'''

genre_table1 = '''COPY(
                           SELECT game_genre.game_id, genre_info.genre_name
                           FROM game_genre 
                           JOIN genre_info 
                           ON game_genre.genre1 = genre_info.genre_id) 
                           TO './Data/genre1.csv'(FORMAT csv);
                            )'''

genre_table2 = '''COPY(
                           SELECT game_genre.game_id, genre_info.genre_name
                           FROM game_genre 
                           JOIN genre_info 
                           ON game_genre.genre2 = genre_info.genre_id) 
                           TO './Data/genre2.csv'(FORMAT csv);
                            )'''
genre_table3 = '''COPY(
                           SELECT game_genre.game_id, genre_info.genre_name
                           FROM game_genre 
                           JOIN genre_info 
                           ON game_genre.genre3 = genre_info.genre_id) 
                           TO './Data/genre3.csv'(FORMAT csv);
                            )'''

genre_table4 = '''COPY(
                           SELECT game_genre.game_id, genre_info.genre_name
                           FROM game_genre 
                           JOIN genre_info 
                           ON game_genre.genre4 = genre_info.genre_id) 
                           TO './Data/genre4.csv'(FORMAT csv);
                            )'''

genre_table5 = '''COPY(
                           SELECT game_genre.game_id, genre_info.genre_name
                           FROM game_genre 
                           JOIN genre_info 
                           ON game_genre.genre5 = genre_info.genre_id) 
                           TO './Data/genre5.csv'(FORMAT csv);
                            )'''

genre_table6 = '''COPY(
                           SELECT game_genre.game_id, genre_info.genre_name
                           FROM game_genre 
                           JOIN genre_info 
                           ON game_genre.genre6 = genre_info.genre_id) 
                           TO './Data/genre6.csv'(FORMAT csv);
                            )'''

genre_table7 = '''COPY(
                           SELECT game_genre.game_id, genre_info.genre_name
                           FROM game_genre 
                           JOIN genre_info 
                           ON game_genre.genre7 = genre_info.genre_id) 
                           TO './Data/genre7.csv'(FORMAT csv);
                            )'''

genre_table8 = '''COPY(
                           SELECT game_genre.game_id, genre_info.genre_name
                           FROM game_genre 
                           JOIN genre_info 
                           ON game_genre.genre8 = genre_info.genre_id) 
                           TO './Data/genre8.csv'(FORMAT csv);
                            )'''

genre_table9 = '''COPY(
                           SELECT game_genre.game_id, genre_info.genre_name
                           FROM game_genre 
                           JOIN genre_info 
                           ON game_genre.genre9 = genre_info.genre_id) 
                           TO './Data/genre9.csv'(FORMAT csv);
                            )'''

cursor.execute(genre_table)
cursor.execute(genre_table1)
cursor.execute(genre_table2)
cursor.execute(genre_table3)
cursor.execute(genre_table4)
cursor.execute(genre_table5)
cursor.execute(genre_table6)
cursor.execute(genre_table7)
cursor.execute(genre_table8)
cursor.execute(genre_table9)
