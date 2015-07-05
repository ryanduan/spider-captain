# -*- coding: utf-8 -*-

"""
Description
"""

__author__ = 'T'

from baidu import BaiduMusic

cn_male = 'http://music.baidu.com/artist/cn/male'
cn_female = 'http://music.baidu.com/artist/cn/female'
cn_group = 'http://music.baidu.com/artist/cn/group'

# cn_male_txt = open('cn_male.txt', 'a+')
# cn_female_txt = open('cn_female.txt', 'a+')
# cn_group_txt = open('cn_group.txt', 'a+')

cn_male_txt = 'cn_male.txt'
cn_female_txt = 'cn_female.txt'
cn_group_txt = 'cn_group.txt'



wt_male = 'http://music.baidu.com/artist/western/male'
wt_female = 'http://music.baidu.com/artist/western/female'
wt_group = 'http://music.baidu.com/artist/western/group'

# wt_male_txt = open('wt_male.txt', 'w+')
# wt_female_txt = open('wt_female.txt', 'w+')
# wt_group_txt = open('wt_group.txt', 'w+')

wt_male_txt = 'wt_male.txt'
wt_female_txt = 'wt_female.txt'
wt_group_txt = 'wt_group.txt'

kr_male = 'http://music.baidu.com/artist/kr/male'
kr_female = 'http://music.baidu.com/artist/kr/female'
kr_group = 'http://music.baidu.com/artist/kr/group'

# kr_male_txt = open('kr_male.txt', 'w+')
# kr_female_txt = open('kr_female.txt', 'w+')
# kr_group_txt = open('kr_group.txt', 'w+')

kr_male_txt = 'kr_male.txt'
kr_female_txt = 'kr_female.txt'
kr_group_txt = 'kr_group.txt'

jp_male = 'http://music.baidu.com/artist/jp/male'
jp_female = 'http://music.baidu.com/artist/jp/female'
jp_group = 'http://music.baidu.com/artist/jp/group'

# jp_male_txt = open('jp_male.txt', 'w+')
# jp_female_txt = open('jp_female.txt', 'w+')
# jp_group_txt = open('jp_group.txt', 'w+')

jp_male_txt = 'jp_male.txt'
jp_female_txt = 'jp_female.txt'
jp_group_txt = 'jp_group.txt'

other = 'http://music.baidu.com/artist/other'

# other_txt = open('other.txt', 'w+')
other_txt = 'other.txt'

url_file_list = [
    (cn_male, cn_male_txt), (cn_female, cn_female_txt), (cn_group, cn_group_txt),
    (wt_male, wt_male_txt), (wt_female, wt_female_txt), (wt_group, wt_group_txt),
    (kr_male, kr_male_txt), (kr_female, kr_female_txt), (kr_group, kr_group_txt),
    (jp_male, jp_male_txt), (jp_female, jp_female_txt), (jp_group, jp_group_txt),
    (other, other_txt),
]

if __name__ == '__main__':
    for url, filename in url_file_list:
        baidu = BaiduMusic(url)
        artist_list = baidu.get_artist_list()
        wr = open(filename, 'w')
        wr.write('\n'.join(artist_list))
        wr.close()
