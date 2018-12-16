#!/usr/bin/python3

import pymysql
from account import Account

class Database:

    def __init__(self):
        self.db = pymysql.connect(Account.link,
            Account.user, Account.password, Account.db, charset="utf8mb4")
        self.cursor = self.db.cursor()
        # Use below line in MySQL to create the table
        # CREATE TABLE IF NOT EXISTS USERS (USERHASH VARCHAR(191), ANIME VARCHAR(191), SCORE INT(10), UNIQUE (USERHASH, ANIME));
        # ALTER TABLE USERS CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

    def write(self, username, anime, score):
        anime = anime.encode('utf-8')
        anime = anime.replace('"', '\\"')
        anime = anime.replace("'", "\\'")
        try:
            self.cursor.execute('REPLACE INTO USERS VALUES ("{}","{}","{}")'.format(username,anime,score))
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()

    def close(self):
        self.db.close()
