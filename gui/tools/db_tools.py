import os
import sqlite3

path = '\\'.join(os.path.realpath('db_tools.py').split('\\')[:-1])
con = sqlite3.connect(f'{path}\\db\\events_db.sqlite')
cur = con.cursor()


def db_add_event(user, event, dt):
    query = f'''
INSERT INTO event (user_id, title, datetime)
VALUES ({user}, '{event}', '{dt}');
    '''
    try:
        cur.execute(query)
        con.commit()
        return True
    except sqlite3.OperationalError as err:
        print(err)
        return False


def db_get_events(user_id):
    query = f'''
SELECT datetime, title
FROM event
WHERE user_id = {user_id}
'''
    events = cur.execute(query).fetchall()
    res = []
    for event in events:
        dt, text = event
        res.append(f'{dt} - {text}')
    return res


def db_check_and_add_user(name):
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


def db_delete_event(events):
    for event in events:
        dt, title = event.text().split(' - ')
        query = f'''
DELETE FROM event
WHERE title = '{title}' AND datetime = '{dt}';
'''
        try:
            cur.execute(query)
            con.commit()
        except sqlite3.OperationalError as err:
            print(err)
            return False
    return True


def db_search_event(user_id, dt, text):
    query = f'''
SELECT *
FROM event
WHERE user_id = {user_id} AND title = '{text}' AND datetime = '{dt}';
'''
    res = cur.execute(query).fetchall()
    assert len(res) == 1, 'Ошибка при добавлении события!'
    event_id, *_ = res[0]
    return event_id

