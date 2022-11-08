import os
import sqlite3

path = '\\'.join(os.path.realpath('db_update.py').split('\\')[:-1])
con = sqlite3.connect(f'{path}\\db\\events_db.sqlite')
cur = con.cursor()


def add_event(user, event, dt):
    global con, cur
    query = f'''
INSERT INTO event (user_id, title, datetime)
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
    global con, cur
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


def delete_event(events):
    global con, cur
    for event in events:
        dt, title = event.split(' - ')
        query = f'''
DELETE FROM event
WHERE title = '{title}' AND datetime = '{dt}';
'''
        try:
            cur.execute(query)
            con.commit()
        except sqlite3.OperationalError as e:
            print(e)
            return False
        else:
            return True
    return True
