import os
import sqlite3
from gui.tools.diff_tools import *
from gui.tools.event import Event
from gui.tools.exceptions import *

path = '\\'.join(os.path.realpath('db_tools.py').split('\\')[:-1])
con = sqlite3.connect(f'{path}\\db\\events_db.sqlite')
cur = con.cursor()
STEP = 17


def db_add_event(user_id, text, dt):
    query = f'''
        INSERT INTO event (user_id, title, datetime)
        VALUES ({user_id}, '{text}', '{dt}');
    '''
    if not db_check_for_event(user_id, dt, text):
        cur.execute(query)
        con.commit()
        return True
    return False


def db_get_events(user_id):
    query = f'''
        SELECT event_id, title, datetime
        FROM event
        WHERE user_id = {user_id};
    '''
    events = cur.execute(query).fetchall()
    res = []
    for event in events:
        event_id, text, dt = event
        res.append(Event(dt, text, event_id, user_id))
    return res


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


def db_check_for_event(user_id, dt, text):
    query = f'''
        SELECT *
        FROM event
        WHERE user_id = {user_id} AND title = '{text}' AND datetime = '{dt}';
    '''
    res = cur.execute(query).fetchall()
    return len(res) > 0


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


def db_login(username, passwd):
    query = f'''
        SELECT user_id, query_encr, passwd_encr
        FROM users
        WHERE username_encr = '{username}';
    '''
    res = cur.execute(query).fetchall()
    if not res:
        raise LoginNotFound
    if passwd != res[0][-1]:
        raise IncorrectPassword
    return res[0]


def db_register(username, passwd, _query, answ):
    query = f'''
        INSERT INTO users (passwd_encr, username_encr, query_encr, answer_encr)
        VALUES ('{passwd}', '{username}', '{_query}', '{answ}');
    '''
    try:
        cur.execute(query)
        con.commit()
        return True
    except sqlite3.IntegrityError as err:
        print(err)
        return False


def db_get_user_data(login):
    login = encrypt(login, STEP)
    query = f'''
        SELECT user_id, passwd_encr, query_encr, answer_encr
        FROM users
        WHERE username_encr = '{login}';
    '''
    res = cur.execute(query).fetchall()
    if len(res) != 1:
        raise LoginNotFound
    return res[0]


def db_check_answer(login, answ):
    query = f'''
        SELECT answer_encr
        FROM users
        WHERE username_encr = '{login}';
    '''
    res = cur.execute(query).fetchall()
    if len(res) != 1:
        raise LoginNotFound
    right_answ = res[0][0]
    return answ == right_answ


def db_change_passwd(login, passwd):
    query = f'''
        UPDATE users
        SET passwd_encr = '{passwd}'
        WHERE username_encr = '{login}';
    '''
    cur.execute(query)
    con.commit()


def db_get_query(login):
    query = f'''
        SELECT query_encr
        FROM users
        WHERE username_encr = '{login}';
    '''
    res = cur.execute(query).fetchall()
    return res[0][0]
