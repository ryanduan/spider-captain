# -*- coding: utf-8 -*-

"""
Description
"""

__author__ = 'T'
from model import session, connect, Lohas


media_list = connect.execute("select mid, serial_id, name, singer, path from media where path != ''")

for mid, serial_id, name, singer, path in media_list.fetchall():
    l = Lohas(mid=mid, serial_id=serial_id, name=name, singer=singer, path=path)
    session.add(l)
session.commit()
