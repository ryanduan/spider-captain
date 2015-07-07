#!/usr/bin/python

lyric = open('download_lrc.txt', 'r').readlines()
song_list = open('download_song.txt', 'r').readlines()
match_list = open('want.txt', 'r').readlines()

total = len(song_list)
print total

count = 10000

filenum = total / count + 1
print filenum


for i in range(filenum):
    song = open('song-{}.txt'.format(i), 'a+')
    lrc = open('lyric-{}.txt'.format(i), 'a+')
    match = open('match-{}.txt'.format(i), 'a+')
    start = count * i
    stop = start + count
    song.write(''.join(song_list[start:stop]))
    lrc.write(''.join(lyric[start:stop]))
    match.write(''.join(match_list[start:stop]))
    song.close()
    lrc.close()
    match.close()
    print 'segmentation {} done'.format(i)
