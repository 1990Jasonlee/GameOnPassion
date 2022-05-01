import psycopg2

conn = psycopg2.connect(
   database="gameon", user='postgres', password='password', host='127.0.0.1', port= '5432'
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


cursor.execute(load_game)
cursor.execute(load_genre)


conn.commit()
conn.close()
