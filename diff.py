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

<<<<<<< HEAD
baidu_list = session.query(Baidu.bid, Baidu.singer, Baidu.name, Baidu.url, Baidu.lrc).all()

#want_list = [music for music in baidu_list if music not in lohas_list]
want = open('want.txt', 'a+')
song = open('download_song.txt', 'a+')
lyric = open('download_lrc.txt', 'a+')
=======
#baidu_list = session.query(BaiduBakup.singer, BaiduBakup.name, BaiduBakup.url, BaiduBakup.lrc).all()
#
##want_list = [music for music in baidu_list if music not in lohas_list]
#want = open('want.txt', 'a+')
#down = open('download.txt', 'a+')
#for singer, name, url, lrc in baidu_list:
#    if url and url.startswith('http://'):
#        lohas = session.query(Lohas).filter_by(name=name, singer=singer).first()
#        if lohas:
#            continue
#        print singer, name
#        want.write('{}\t{}\n'.format(singer.encode('utf8'), name.encode('utf8')))
#        down.write('{}\n{}\n'.format(url, lrc))
#want.close()
#down.close()
#
baidu_list = session.query(Baidu.bid, Baidu.singer, Baidu.name, Baidu.url, Baidu.lrc).all()

#want_list = [music for music in baidu_list if music not in lohas_list]
want = open('download/want.txt', 'a+')
song = open('download/download_song.txt', 'a+')
lyric = open('download/download_lrc.txt', 'a+')
>>>>>>> 8e87f0bb0b7e0fffcca4f412a3ccf52c2d4623c5
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
<<<<<<< HEAD

=======
>>>>>>> 8e87f0bb0b7e0fffcca4f412a3ccf52c2d4623c5
