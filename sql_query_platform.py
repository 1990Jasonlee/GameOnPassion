import psycopg2

conn = psycopg2.connect(
   database="gameon", user='postgres', password='password', host='127.0.0.1', port= '5432'
)
conn.autocommit = True
cursor = conn.cursor()

platform_info_table = '''COPY(
                           platform_info(platform_id, name)
                           from './platform_table.csv' delimiter ',' csv header;
                           )'''
platform_table = '''COPY(
                           game_platform(plat_id, plat_1, plat_2, plat_3, plat_4, 
                           plat_5, plat_6, plat_7, plat_8, plat_9, plat_10, plat_11, 
                           plat_12, plat_13, plat_14, plat_15, plat_16, plat_17, plat_18, plat_19) 
                           from './game_platform.csv' delimiter ',' csv header;
                            )'''

platform1_table1 = '''COPY(
                           SELECT game_platform.plat_id, platform_info.platform_name
                           FROM game_platform 
                           JOIN platform_info 
                           ON game_platform.plat_1 = platform_info.platform_id)
                           TO './plat1.csv'(FORMAT csv);
                            )'''

platform1_table2 = '''COPY(
                           SELECT game_platform.plat_id, platform_info.platform_name
                           FROM game_platform 
                           JOIN platform_info 
                           ON game_platform.plat_2 = platform_info.platform_id)
                           TO './plat2.csv'(FORMAT csv);
                            )'''

platform1_table3 = '''COPY(
                           SELECT game_platform.plat_id, platform_info.platform_name
                           FROM game_platform 
                           JOIN platform_info 
                           ON game_platform.plat_3 = platform_info.platform_id)
                           TO './plat3.csv'(FORMAT csv);
                            )'''

platform1_table4 = '''COPY(
                           SELECT game_platform.plat_id, platform_info.platform_name
                           FROM game_platform 
                           JOIN platform_info 
                           ON game_platform.plat_4 = platform_info.platform_id)
                           TO './plat4.csv'(FORMAT csv);
                            )'''

platform1_table5 = '''COPY(
                           SELECT game_platform.plat_id, platform_info.platform_name
                           FROM game_platform 
                           JOIN platform_info 
                           ON game_platform.plat_5 = platform_info.platform_id)
                           TO './plat5.csv'(FORMAT csv);
                            )'''

platform1_table6 = '''COPY(
                           SELECT game_platform.plat_id, platform_info.platform_name
                           FROM game_platform 
                           JOIN platform_info 
                           ON game_platform.plat_6 = platform_info.platform_id)
                           TO './plat6.csv'(FORMAT csv);
                            )'''

platform1_table7 = '''COPY(
                           SELECT game_platform.plat_id, platform_info.platform_name
                           FROM game_platform 
                           JOIN platform_info 
                           ON game_platform.plat_7 = platform_info.platform_id)
                           TO './plat7.csv'(FORMAT csv);
                            )'''

platform1_table8 = '''COPY(
                           SELECT game_platform.plat_id, platform_info.platform_name
                           FROM game_platform 
                           JOIN platform_info 
                           ON game_platform.plat_8 = platform_info.platform_id)
                           TO './plat8.csv'(FORMAT csv);
                            )'''

platform1_table9 = '''COPY(
                           SELECT game_platform.plat_id, platform_info.platform_name
                           FROM game_platform 
                           JOIN platform_info 
                           ON game_platform.plat_9 = platform_info.platform_id)
                           TO './plat9.csv'(FORMAT csv);
                            )'''

platform1_table10 = '''COPY(
                           SELECT game_platform.plat_id, platform_info.platform_name
                           FROM game_platform 
                           JOIN platform_info 
                           ON game_platform.plat_10 = platform_info.platform_id)
                           TO './plat10.csv'(FORMAT csv);
                            )'''

platform1_table11 = '''COPY(
                           SELECT game_platform.plat_id, platform_info.platform_name
                           FROM game_platform 
                           JOIN platform_info 
                           ON game_platform.plat_11 = platform_info.platform_id)
                           TO './plat11.csv'(FORMAT csv);
                            )'''

platform1_table12 = '''COPY(
                           SELECT game_platform.plat_id, platform_info.platform_name
                           FROM game_platform 
                           JOIN platform_info 
                           ON game_platform.plat_12 = platform_info.platform_id)
                           TO './plat12.csv'(FORMAT csv);
                            )'''

platform1_table13 = '''COPY(
                           SELECT game_platform.plat_id, platform_info.platform_name
                           FROM game_platform 
                           JOIN platform_info 
                           ON game_platform.plat_13 = platform_info.platform_id)
                           TO './plat13.csv'(FORMAT csv);
                            )'''

platform1_table14 = '''COPY(
                           SELECT game_platform.plat_id, platform_info.platform_name
                           FROM game_platform 
                           JOIN platform_info 
                           ON game_platform.plat_14 = platform_info.platform_id)
                           TO './plat14.csv'(FORMAT csv);
                            )'''

platform1_table15 = '''COPY(
                           SELECT game_platform.plat_id, platform_info.platform_name
                           FROM game_platform 
                           JOIN platform_info 
                           ON game_platform.plat_15 = platform_info.platform_id)
                           TO './plat15.csv'(FORMAT csv);
                            )'''

platform1_table16 = '''COPY(
                           SELECT game_platform.plat_id, platform_info.platform_name
                           FROM game_platform 
                           JOIN platform_info 
                           ON game_platform.plat_16 = platform_info.platform_id)
                           TO './plat16.csv'(FORMAT csv);
                            )'''

platform1_table17 = '''COPY(
                           SELECT game_platform.plat_id, platform_info.platform_name
                           FROM game_platform 
                           JOIN platform_info 
                           ON game_platform.plat_17 = platform_info.platform_id)
                           TO './plat17.csv'(FORMAT csv);
                            )'''

platform1_table18 = '''COPY(
                           SELECT game_platform.plat_id, platform_info.platform_name
                           FROM game_platform 
                           JOIN platform_info 
                           ON game_platform.plat_18 = platform_info.platform_id)
                           TO './plat18.csv'(FORMAT csv);
                            )'''

platform1_table19 = '''COPY(
                           SELECT game_platform.plat_id, platform_info.platform_name
                           FROM game_platform 
                           JOIN platform_info 
                           ON game_platform.plat_19 = platform_info.platform_id)
                           TO './plat19.csv'(FORMAT csv);
                            )'''

cursor.execute(platform_info_table)
cursor.execute(platform_table)
cursor.execute(platform1_table1)
cursor.execute(platform1_table2)
cursor.execute(platform1_table3)
cursor.execute(platform1_table4)
cursor.execute(platform1_table5)
cursor.execute(platform1_table6)
cursor.execute(platform1_table7)
cursor.execute(platform1_table8)
cursor.execute(platform1_table9)
cursor.execute(platform1_table10)
cursor.execute(platform1_table11)
cursor.execute(platform1_table12)
cursor.execute(platform1_table13)
cursor.execute(platform1_table14)
cursor.execute(platform1_table15)
cursor.execute(platform1_table16)
cursor.execute(platform1_table17)
cursor.execute(platform1_table18)
cursor.execute(platform1_table19)
conn.commit()
conn.close()