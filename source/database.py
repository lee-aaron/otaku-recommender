#!/usr/bin/python

import sqlite3

class Database:

    def __init__(self):
        self.db = sqlite3.connect('database/anime_storage')
        self.cursor = self.db.cursor()

    def create_table(self):
        # Each anime is unique meaning only should appear once per user
        self.cursor.execute('CREATE TABLE IF NOT EXISTS USERS (USERHASH TEXT, ANIME TEXT, SCORE INT, UNIQUE (USERHASH, ANIME))')

    def write(self, username, anime, score):
        # Sample Code to insert multiple info into table USERS
        # INSERT if record is not present else REPLACE record
        # Single quote or Double quote would mess up the string when running SQL command
        if(type(anime) is str and anime.find('"') != -1):
            self.cursor.execute("INSERT OR REPLACE INTO USERS VALUES ('{}','{}','{}')".format(username,anime,score))
        else:
            self.cursor.execute('INSERT OR REPLACE INTO USERS VALUES ("{}","{}","{}")'.format(username,anime,score))

    def close(self):
        self.db.commit()
        self.cursor.close()
