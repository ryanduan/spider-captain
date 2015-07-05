# -*- coding: utf-8 -*-

"""
Description
"""

__author__ = 'T'

from bs4 import BeautifulSoup
import urllib2
import requests


of = open('proxy.txt', 'w')

for page in range(1, 10):
    body = urllib2.urlopen("http://www.kuaidaili.com/proxylist/"+str(page)).read()
    body_format = BeautifulSoup(body)
    data = body_format.find_all("td")
    ip = map(lambda x: x.text, data[::8])
    port = map(lambda x: x.text, data[1::8])
    for index, i in enumerate(ip):
        of.write('%s=%s:%s\n' % ("111", ip[index], port[index]))
        print '%s=%s:%s' % ("111", ip[index], port[index])

of.close()
