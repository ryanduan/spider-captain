# -*- coding: utf-8 -*-

"""
Description
"""

__author__ = 'T'

from tornado.httpclient import HTTPClient
import re
import datetime
import json

re_artist = r'href="/artist/(\d+?)"'
re_song = r'href="(/song/\d+?)"'
re_lrc = r'"href":"(/.+?)"'
re_down = r'href="/data/music/file\?link=(.+?)"  id="320"'
re_song_name = r'<a target="_blank" title="(.+?)" class="song-link-hook" href'
re_artist_name = r'target = "_blank"hidefocus="true" href="/artist/\d+">(.+?)</a>'
re_song_num = r'<a class="list" hidefocus="true" href="#">歌曲\((\d+?)\)</a>'

log = open('./log/spider.log', 'a+')
record = open('./log/record.txt', 'a+')
http_log = open('log/http.log', 'a+')
error = open('log/error.log', 'a+')
re_err = open('log/re_err.log', 'a+')


base = 'http://music.baidu.com'

download_suffix = '/download?__o=%2Fsong%2F'

URL = 'http://music.baidu.com/artist'
ARTIST = 'http://music.baidu.com/artist/{}'
DOWNLOAD = 'http://music.baidu.com/{}/download?__o=%2Fsong%2F'
SONG = 'http://music.baidu.com/{}'

get_song_list_url = 'http://music.baidu.com/data/user/getsongs?start={}&ting_uid={}&order=hot'


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 UBrowser/5.1.1591.57 Safari/537.36',
    'Cookie':'BDUSS=0Z4TW0wbWxkLUo3aWMyTS1TYTIxeWpHUWQwZTU1RmxkYjhGNFYwZG5qbjNxN1JWQVFBQUFBJCQAAAAAAAAAAAEAAAAFOLwJZHl3NTY0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPcejVX3Ho1VM; PSTM=1435316128; BIDUPSID=78B6837AAE38FF3BB8704DA450D41DF1; BAIDUID=985DAB4F3DF60FB5208658BD6562E2B7:FG=1; TOPMSG=1436082389-0; BDRCVFR[kJlVbOKdoAC]=mk3SLVN4HKm; H_PS_PSSID=13834_16061_1443_12658_16030_10813_12868_16166_14871_16211_11595_13932_13768_15964; Hm_lvt_d0ad46e4afeacf34cd12de4c9b553aa6=1435150270,1435214455,1435215745,1435222067; Hm_lpvt_d0ad46e4afeacf34cd12de4c9b553aa6=1436088307; tracesrc=-1%7C%7C-1; u_lo=0; u_id=; u_t=; batch=1; u_vip=1'
}


class BaiduMusic(object):
    """"""

    def __init__(self, url=None):
        if url is None:
            self.url = URL
        else:
            self.url = url
        self.client = HTTPClient()

    def get_html_body(self, url, method='GET', headers=None):
        try:
            res = self.client.fetch(url, method=method, headers=headers)
            http_log.write('lohas_t_baidu_0:\t{}\n\t{}\n'.format(datetime.datetime.today(), url))
            return res.body
        except Exception as e:
            error.write('\nlohas_t_baidu_001:\t{}\n\t{}\n'.format(datetime.datetime.today(), e))
            return None

    def get_artist_list(self):
        """:return artist id list"""
        body = self.get_html_body(self.url)
        if body is None:
            return []
        return list(set(re.findall(re_artist, body)))

    def get_artist_song_count(self, artist_id):
        """"""
        body = self.get_html_body(ARTIST.format(artist_id))
        if body is None:
            return 0
        try:
            return int(re.findall(re_song_num, body)[0])
        except (ValueError, TypeError, IndexError) as e:
            re_err.write('lohas_t_baidu_002:\t{}\n\t{}\n\t{}\n\n'.format(datetime.datetime.today(),
                                                                         ARTIST.format(artist_id), e))
            return 0

    def get_song_list(self, artist_id, start):
        """"""
        body = self.get_html_body(get_song_list_url.format(start, artist_id))
        if body is None:
            return []
        res = json.loads(body)
        return list(set(re.findall(re_song, res.get('data').get('html'))))

    def get_download_url(self, song):
        body = self.get_html_body(DOWNLOAD.format(song), headers=HEADERS)
        if body is None:
            return None, None, None
        try:
            down_url = re.findall(re_down, body)[0]
            artist_name = re.findall(re_artist_name, body)[0]
            song_name = re.findall(re_song_name, body)[0]
            return down_url, artist_name, song_name
        except IndexError as e:
            re_err.write('lohas_t_baidu_003:\t{}\n\t{}\n\t{}\n\n'.format(datetime.datetime.today(),
                                                                         DOWNLOAD.format(song), e))
            return None, None, None

    def get_lrc_url(self, song):
        body = self.get_html_body(SONG.format(song))
        if body is None:
            return None
        try:
            return re.findall(re_lrc, body)[0]
        except IndexError as e:
            re_err.write('lohas_t_baidu_003:\t{}\n\t{}\n\t{}\n\n'.format(datetime.datetime.today(),
                                                                         SONG.format(song), e))
            return None



# def get_html_body(url, method='GET'):
#     """"""
#     client = HTTPClient()
#     res = client.fetch(url, method=method, headers=headers)
#     return res.body
#
#
# def find_sub_url(r, s):
#     """"""
#     return list(set(re.findall(r, s)))
#
#
# def download(url, name):
#     """"""
#     log.write('{}\t Start wget {}\t{}\n'.format(datetime.datetime.today(), url, name))
#     os.system('wget {} 2>/dev/null'.format(url))
#     # os.system('mv {} {}'.format(url.split('/')[-1], name))
#     record.write('{}\t{}\t{}\n'.format(datetime.datetime.today(), url.split('/')[-1], name))
#
# if __name__ == '__main__':
#     artist_body = get_html_body(url)
#     artist_list = find_sub_url(re_artist, artist_body)
#     for artist in artist_list:
#         aurl = base + artist
#         song_body = get_html_body(aurl)
#         song_list = find_sub_url(re_song, song_body)
#         for song in song_list:
#             surl = base + song
#             down_body = get_html_body(surl + download_suffix)
#             try:
#                 down_url = find_sub_url(re_down, down_body)[0]
#                 song_name = find_sub_url(re_song_name, down_body)[0]
#                 artist_name = find_sub_url(re_artist_name, down_body)[0]
#                 name = '{}-{}'.format(song_name, artist_name)
#                 download(down_url, '{}.mp3'.format(name))
#                 try:
#                     lrc_body = get_html_body(surl)
#                     lrc = find_sub_url(re_lrc, lrc_body)[0]
#                     lurl = base + lrc
#                     download(lurl, '{}.lrc'.format(name))
#                 except IndexError:
#                     log.write('{}\t ERROR, Cant get lrc {}\n'.format(datetime.datetime.today(), name))
#
#             except IndexError:
#                 log.write('{}\tERROR, Cant get song {}\n'.format(datetime.datetime.today(), song))
#
