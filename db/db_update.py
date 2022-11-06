import os
import sqlite3


def add_event(user, event, dt):
    path = '\\'.join(os.path.realpath('db_update.py').split('\\')[:-2])
    con = sqlite3.connect(f'{path}\\db\\events_db.sqlite')
    cur = con.cursor()
    query = f'''
INSERT INTO event (user_id, event, datetime)
VALUES ({user}, '{event}', '{dt}');
    '''
    try:
        cur.execute(query)
        con.commit()
        return True
    except sqlite3.OperationalError as e:
        print(e)
        return False


def check_and_add_user(name):
    path = '\\'.join(os.path.abspath('db_update.py').split('\\')[:-2])
    con = sqlite3.connect(f'{path}\\db\\events_db.sqlite')
    cur = con.cursor()
    query = f'''
SELECT user_id
FROM users
WHERE name = '{name}';
    '''
    res = cur.execute(query).fetchall()
    if res:
        return res[0][0]
    query = f'''
INSERT INTO users (name)
VALUES ('{name}');
    '''
    try:
        cur.execute(query)
    except sqlite3.OperationalError:
        return False
    query = f'''
SELECT user_id
FROM users
WHERE name = '{name}';
    '''
    res = cur.execute(query).fetchall()
    con.commit()
    return res[0][0]
