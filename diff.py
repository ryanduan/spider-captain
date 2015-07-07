<<<<<<< HEAD
# -*- coding: utf-8 -*-

"""
Description
"""

__author__ = 'T'



from model import Baidu, BaiduBakup, Lohas, Want, session

# want = open('want.txt', 'w')

# baidu_list = session.query(BaiduBakup.singer, BaiduBakup.name).all()
# lohas_list = session.query(Lohas.singer, Lohas.name).all()
#
# want_list = [music for music in baidu_list if music not in lohas_list]
# want.write('\n'.join(want_list))
# want.close()

baidu_list = session.query(Baidu.bid, Baidu.singer, Baidu.name, Baidu.url, Baidu.lrc).all()

#want_list = [music for music in baidu_list if music not in lohas_list]
want = open('want.txt', 'a+')
song = open('download_song.txt', 'a+')
lyric = open('download_lrc.txt', 'a+')
for bid, singer, name, url, lrc in baidu_list:
    if url and url.startswith('http://'):
        lohas = session.query(Lohas).filter_by(name=name, singer=singer).first()
        if lohas:
            continue
        print singer, name
        want.write('{}\t{}\n'.format(singer.encode('utf8'), name.encode('utf8')))
        song.write('{}\n'.format(url))
        lyric.write('{}\n'.format(lrc))
        w = Want(sub_id=bid, name=name, singer=singer, url=url, lrc=lrc)
        session.add(w)
want.close()
song.close()
lyric.close()
session.commit()

