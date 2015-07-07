
from model import Baidu, BaiduBakup, Lohas, Want, session


baidu_list = session.query(BaiduBakup.singer, BaiduBakup.name, BaiduBakup.url, BaiduBakup.lrc).all()

#want_list = [music for music in baidu_list if music not in lohas_list]
want = open('want.txt', 'a+')
down = open('download.txt', 'a+')
for singer, name, url, lrc in baidu_list:
    if url and url.startswith('http://'):
        lohas = session.query(Lohas).filter_by(name=name, singer=singer).first()
        if lohas:
            continue
        print singer, name
        want.write('{}\t{}\n'.format(singer.encode('utf8'), name.encode('utf8')))
        down.write('{}\n{}\n'.format(url, lrc))
want.close()
down.close()

