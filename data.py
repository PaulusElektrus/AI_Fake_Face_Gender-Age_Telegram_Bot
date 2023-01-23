"""
Helper Functions for the User Management <--> DB connection of the Telegram Bot in main.py
"""

import sqlite3 as sql

DB = sql.connect('user.db', check_same_thread=False)

with DB:
    DB.execute("""
        CREATE TABLE if NOT EXISTS USER (
            cid INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            username TEXT,
            userstep INTEGER
        );
    """)

user_query = 'INSERT INTO USER (cid, first_name, last_name, username, userstep) values (?, ?, ?, ?, ?)'
emotion_query = 'INSERT INTO USER=? (PK, number, description) values (?, ?, ?)'
userStep_query = 'UPDATE USER SET userstep = ? WHERE cid = ?'

def store_user(data):
    with DB:
        DB.executemany(user_query, data)

def store_userStep(cid, data):
    data = [(data, cid)]
    with DB:
        DB.executemany(userStep_query, data)

def get_user(cid):
    with DB:
        cursor = DB.cursor()
        data = cursor.execute("SELECT cid FROM USER WHERE cid=?", (cid,))
        data = data.fetchall()
        for x in data:
            return int(x[0])

def get_all_users():
    with DB:
        cursor = DB.cursor()
        data = cursor.execute("SELECT cid, first_name FROM USER")
        data = data.fetchall()
        return data

def get_userstep(cid):
    with DB:
        cursor = DB.cursor()
        data = cursor.execute("SELECT userstep FROM USER WHERE cid=?", (cid,))
        data = data.fetchall()
        for x in data:
            return int(x[0])

def store_emotion(cid, data):
    with DB:
        DB.execute("""
        CREATE TABLE if NOT EXISTS USER=? (
            PK INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            number INTEGER,
            description TEXT
        );
        """, (cid,))
        DB.executemany(emotion_query, data)

def get_emotion(cid):
    with DB:
        cursor = DB.cursor()
        data = cursor.execute("SELECT cid, first_name FROM cid=?", (cid,))
        data = data.fetchall()
        return data