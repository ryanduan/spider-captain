# -*- coding: utf-8 -*-

"""
Description
"""

__author__ = 'T'

from tornado.httpclient import HTTPClient
from model import Tencent, Lohas, Want
import re
import os
import datetime

re_artist = r'href="(/artist/\d+?)"'
re_song = r'href="(/song/\d+?)"'
re_lrc = r'"href":"(/.+?)"'
re_down = r'href="/data/music/file\?link=(.+?)"  id="320"'
re_song_name = r'<a target="_blank" title="(.+?)" class="song-link-hook" href'
re_artist_name = r'target = "_blank"hidefocus="true" href="/artist/\d+">(.+?)</a>'

log = open('./spider.log', 'a+')
record = open('./record.txt', 'a+')


base = 'http://music.baidu.com'

download_suffix = '/download?__o=%2Fsong%2F'

url = 'http://music.baidu.com/artist'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 UBrowser/5.1.1591.57 Safari/537.36',
    'Cookie':'BAIDUID=F913F1630F07C4E7C93BD5945D4BEAB2:FG=1; BDUSS=0Z4TW0wbWxkLUo3aWMyTS1TYTIxeWpHUWQwZTU1RmxkYjhGNFYwZG5qbjNxN1JWQVFBQUFBJCQAAAAAAAAAAAEAAAAFOLwJZHl3NTY0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPcejVX3Ho1VM; Hm_lvt_d0ad46e4afeacf34cd12de4c9b553aa6=1435150270,1435214455,1435215745,1435222067; Hm_lpvt_d0ad46e4afeacf34cd12de4c9b553aa6=1435311866; tracesrc=-1%7C%7C-1; u_lo=0; u_id=; u_t=; batch=1; u_vip=1; TOPMSG=1435311866-0'
}


def get_html_body(url, method='GET'):
    """"""
    client = HTTPClient()
    res = client.fetch(url, method=method, headers=headers)
    return res.body


def find_sub_url(r, s):
    """"""
    return list(set(re.findall(r, s)))


def download(url, name):
    """"""
    log.write('{}\t Start wget {}\t{}\n'.format(datetime.datetime.today(), url, name))
    os.system('wget {} 2>/dev/null'.format(url))
    # os.system('mv {} {}'.format(url.split('/')[-1], name))
    record.write('{}\t{}\t{}\n'.format(datetime.datetime.today(), url.split('/')[-1], name))

if __name__ == '__main__':
    artist_body = get_html_body(url)
    artist_list = find_sub_url(re_artist, artist_body)
    for artist in artist_list:
        aurl = base + artist
        song_body = get_html_body(aurl)
        song_list = find_sub_url(re_song, song_body)
        for song in song_list:
            surl = base + song
            down_body = get_html_body(surl + download_suffix)
            try:
                down_url = find_sub_url(re_down, down_body)[0]
                song_name = find_sub_url(re_song_name, down_body)[0]
                artist_name = find_sub_url(re_artist_name, down_body)[0]
                name = '{}-{}'.format(song_name, artist_name)
                download(down_url, '{}.mp3'.format(name))
                try:
                    lrc_body = get_html_body(surl)
                    lrc = find_sub_url(re_lrc, lrc_body)[0]
                    lurl = base + lrc
                    download(lurl, '{}.lrc'.format(name))
                except IndexError:
                    log.write('{}\t ERROR, Cant get lrc {}\n'.format(datetime.datetime.today(), name))

            except IndexError:
                log.write('{}\tERROR, Cant get song {}\n'.format(datetime.datetime.today(), song))
