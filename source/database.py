#!/usr/bin/python3

import pymysql
import account

class Database:

    def __init__(self):
        a = Account()
        self.db = pymysql.connect(a.getLink(),
            a.getUser(),a.getPass(),a.getDB(), charset="utf8mb4")
        self.cursor = self.db.cursor()
        # Use below line in MySQL to create the table
        # CREATE TABLE IF NOT EXISTS USERS (USERHASH VARCHAR(191), ANIME VARCHAR(191), SCORE INT(10), UNIQUE (USERHASH, ANIME));

    def write(self, username, anime, score):
        try:
            if(type(anime) is str and anime.find('"') != -1):
                self.cursor.execute("REPLACE INTO USERS VALUES ('{}','{}','{}')".format(username,anime,score))
            else:
                self.cursor.execute('REPLACE INTO USERS VALUES ("{}","{}","{}")'.format(username,anime,score))
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()

    def close(self):
        self.db.close()
