import psycopg2

conn = psycopg2.connect(
   database="gameon", user='postgres', password='password', host='127.0.0.1', port= '5432'
)
conn.autocommit = True
cursor = conn.cursor()

gamemode_info_table = '''COPY(
                           platform_info(platform_id, name)
                           from './platform_table.csv' delimiter ',' csv header;
                           )'''