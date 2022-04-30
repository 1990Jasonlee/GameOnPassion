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

create_table = '''CREATE TABLE IF NOT EXISTS tablename(
                            '' int NOT NULL,
                            '' int NOT NULL,
                            '' int NOT NULL,
                            '' int NOT NULL)'''