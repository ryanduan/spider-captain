# -*- coding: utf-8 -*-

"""
Description
"""

__author__ = 'T'

from model import Base, Baidu, Lohas, Download, Tencent, Want, init_schema,session
from baidu import BaiduMusic
from sqlalchemy.exc import SQLAlchemyError
from init_artist_file import url_dict
import datetime

print('please input: ', url_dict.keys())

key = raw_input()

kr = False
if key.startswith('kr'):
    kr = True

url, txt = url_dict.get(key)

sql_err = open('log/sql_err.log', 'a+')
record = open('record/{}'.format(txt), 'a+')
log = open('log/{}'.format(txt), 'a+')
art = open('artist/{}'.format(txt), 'a+')
down = open('down/{}'.format(txt), 'a+')
init_schema()

baidu = BaiduMusic(url)
artist_list = baidu.get_artist_list()

artist_list.sort()
if key == 'cn_group':
    artist_list = artist_list[857:]
elif key == 'cn_male':
    artist_list = artist_list[4891:]
elif key == 'cn_female':
    artist_list = artist_list[384:]
elif key == 'jp_group':
    artist_list = artist_list[153:]
elif key == 'jp_male':
    artist_list = artist_list[66:]
elif key == 'jp_female':
    artist_list = artist_list[95:]
elif key == 'kr_group':
    artist_list = artist_list[328:]
elif key == 'kr_male':
    artist_list = artist_list[372:]
elif key == 'kr_female':
    artist_list = artist_list[212:]

for artist in artist_list:
    print '{}\t{}\n'.format(datetime.datetime.today(), artist)
    log.write('{}\t{}\n'.format(datetime.datetime.today(), artist))
    if kr:
        count = 9999
    else:
        count = baidu.get_artist_song_count(artist)
    if count == 0:
        continue
    start = 0
    while start < count:
        song_list = baidu.get_song_list(artist, start)
        if not song_list or len(song_list) == 0:
            break
        for song in song_list:
            down_url, artist_name, song_name = baidu.get_download_url(song)
            try:
                lrc_url = 'http://music.baidu.com' + baidu.get_lrc_url(song)
            except:
                lrc_url = ''
            if not down_url or not down_url.startswith('http://yinyueshiting.baidu.com'):
                continue
            down.write('{}\n{}\n'.format(down_url, lrc_url))
            try:
                record.write('{}\t{}\t{}\t{}\n'.format(song_name, artist_name, down_url, lrc_url))
                b = Baidu(name=song_name.decode('utf8'), singer=artist_name.decode('utf8'), url=down_url, lrc=lrc_url)
                session.add(b)
            except Exception as e:
                continue
        start += 25
    try:
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        sql_err.write('{}\t{}\n'.format(artist, e))


