import sqlite3 as sq

# with sq.connect('horoscope.db') as con:
#     cur = con.cursor()
    # cur.execute('DROP TABLE IF EXISTS horoscope')
    # cur.execute('''CREATE TABLE IF NOT EXISTS horoscope(
    # id INTEGER PRIMARY KEY AUTOINCREMENT,
    # user_id INTEGER NOT NULL,
    # name TEXT,
    # sign TEXT NOT NULL
    # )''')
    #
    # cur.execute('''INSERT INTO horoscope(user_id, name, sign) VALUES(123, 'Николай', 'Лев')''')
    # cur.execute('''INSERT INTO horoscope(user_id, name, sign) VALUES(345, 'Андрей', 'Дева')''')
    # cur.execute('''UPDATE horoscope SET user_id = 777 WHERE id == 1 ''')
    # cur.execute('''SELECT * FROM horoscope''')
    # print(cur.fetchmany(3))


# class Database:
#     def __init__(self, path_to_db = 'horoscope.db'):
#         self.path_to_db = path_to_db
#
#     @property
#     def connection(self):
#         return sq.connect(self.path_to_db)

def horoscope_db(user_id, name, sign):
    with sq.connect(f'D:/BOT_HARRY/data/db/horoscope.db') as con:
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS horoscope(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        sign TEXT NOT NULL
        )''')
        cur.execute('''
        INSERT INTO horoscope (user_id, name, sign) VALUES (?, ?, ?)
        ''', (user_id, name, sign))
        res = cur.execute('''
        SELECT * FROM horoscope
        ''')
        print(res.fetchall())
        con.commit()

