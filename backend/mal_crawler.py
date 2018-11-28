#!/usr/bin/python3

""" MyAnimeList Crawler Python 3.6 """
import threading
from time import sleep
import json
from bs4 import BeautifulSoup
import requests
from database import Database

def get_url(usr):
    """ Returns Anime List URL """
    return 'https://myanimelist.net/animelist/{}'.format(usr)

def get_url_2(usr):
    """ Returns Anime List URL Default Implementation """
    return 'https://myanimelist.net/malappinfo.php?u={}&status=all&type=anime'.format(usr)

def get_recent_users():
    """ Returns recent users """
    r = requests.get('https://myanimelist.net/users.php', timeout=10)

    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'lxml')

        # Finds recent users td
        td = soup.find_all('td', attrs={'align':'center', 'class':'borderClass'})
        users = []

        # Appends users to a list
        for e in td:
            users.append(e.find('div').text)
        return users

# Version 1 is a lot faster and will work for the majority of searchs
# Version 2 is slower and seems to not pick up some info
def download_list(user):
    """ Downloads anime list per user and writes to path """
    animelist = get_animelist(user)
    if animelist is not None and len(animelist) != 0:
        write_to_db(user, animelist)
        return "Found"
    else:
        animelist2 = get_animelist_2(user)
        if animelist2 is not None and len(str(animelist2)) > 2:
            write_to_db2(user, animelist2)
            return "Found"
    return "Not Found"

def get_animelist(user):
    """ Gets animelist from string user """
    r = requests.get(get_url(user), timeout=10)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'lxml')
        # Gets table that contains anime list data
        table = soup.find('table', attrs={'class', 'list-table'})
        # table sometimes returns NoneType because not all users have same animelist format
        try:
            string = table['data-items']
            return json.loads(string)
        except:
            return
    return

def get_animelist_2(user):
    """ Gets animelist from string user default """
    r = requests.get(get_url_2(user), timeout=10)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'lxml')
        # ResultSet containing tags with anime
        animelist = soup.find_all('anime')
        return animelist
    return

def write_to_db(user, animelist):
    """ Writes to database and puts in info """
    anime = Database()
    for a in animelist:
        if a.get("score") == 0:
            continue
        anime.write(user, a.get("anime_title"), a.get("score"))
    anime.close()

def write_to_db2(user, animelist):
    """ Writes to database and puts in info """
    anime = Database()
    for a in animelist:
        if int(a.my_score.text) == 0:
            continue
        anime.write(user, a.series_title.text, int(a.my_score.text))
    anime.close()

def crawl(request_delay, iterations):
    """ Crawls MAL
     Waits request_delay for each loop
     Executes # of iterations """
    for i in range(iterations):
        users = get_recent_users()
        if users is None:
            continue
        for user in users:
            sleep(request_delay)
            # (user,) parameterizes the string instead of making it a tuple
            thread = threading.Thread(target=download_list, args=(user,))
            thread.start()