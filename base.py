# -*- coding: utf-8 -*-

"""
Description
"""

__author__ = 'T'

from model import Base, Baidu, Lohas, Download, Tencent, Want, init_schema,session
from baidu import BaiduMusic
from sqlalchemy.exc import SQLAlchemyError
from init_artist_file import cn_male
import datetime

sql_err = open('sql_err.log', 'a+')
record = open('cn_male_record.txt', 'a+')
log = open('cn_male_fetch.log', 'a+')
# init_schema()

baidu = BaiduMusic(cn_male)
artist_list = baidu.get_artist_list()

for artist in artist_list:
    log.write('{}\t{}'.format(datetime.datetime.today(), artist))
    count = baidu.get_artist_song_count(artist)
    if count == 0:
        continue
    start = 0
    while start < count:
        song_list = baidu.get_song_list(artist, start)
        for song in song_list:
            down_url, artist_name, song_name = baidu.get_download_url(song)
            lrc_url = baidu.get_lrc_url(song)
            record.write('{}\t{}\t{}\t{}\n'.format(song_name.decode('utf8'), artist_name.decode('utf8'), down_url, lrc_url))
            b = Baidu(name=song_name.decode('utf8'), singer=artist_name.decode('utf8'), url=down_url, lrc=lrc_url)
            session.add(b)
        start += 25
    try:
        session.commit()
    except SQLAlchemyError as e:
        sql_err.write('{}\t{}\n'.format(artist, e))


