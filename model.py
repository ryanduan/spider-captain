# -*- coding: utf-8 -*-

"""
Description
"""

__author__ = 'T'

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import time

Base = declarative_base()

db_type = 'mysql'
db_user = 'root'
db_host = '127.0.0.1'
db_password = ''
db_name = 'yqc_media'
media = 'media'

db_uri = '{}://{}:{}@{}/{}?charset=utf8'.format(
    db_type, db_user, db_password, db_host, db_name)
media_uri = '{}://{}:{}@{}/{}?charset=utf8'.format(
    db_type, db_user, db_password, db_host, media)
media_engine = create_engine(media_uri, encoding='utf8')
connect = media_engine.connect()
engine = create_engine(db_uri, encoding='utf8')
session = Session(bind=engine)


class Baidu(Base):
    __tablename__ = 'baidu_music_new'

    bid = Column(Integer, primary_key=True)
    name = Column(String(200))
    singer = Column(String(100))
    url = Column(String(300))
    lrc = Column(String(300))
    create_at = Column(Integer, default=lambda: int(time.time()))


class BaiduBakup(Base):
    __tablename__ = 'baidu_music'

    bid = Column(Integer, primary_key=True)
    name = Column(String(200))
    singer = Column(String(100))
    url = Column(String(300))
    lrc = Column(String(300))
    create_at = Column(Integer, default=lambda: int(time.time()))


class Tencent(Base):
    __tablename__ = 'qq_music'

    tid = Column(Integer, primary_key=True)
    name = Column(String(200))
    singer = Column(String(100))
    url = Column(String(300))
    lrc = Column(String(300))
    create_at = Column(Integer, default=lambda: int(time.time()))


class Lohas(Base):
    __tablename__ = 'lohas_music'

    mid = Column(Integer, primary_key=True)
    serial_id = Column(Integer)
    name = Column(String(200))
    singer = Column(String(100))
    path = Column(String(50))


class Want(Base):
    __tablename__ = 'want_music'

    id = Column(Integer, primary_key=True)
    sub_id = Column(Integer)
    name = Column(String(200))
    singer = Column(String(100))
    url = Column(String(300))
    lrc = Column(String(300))
    create_at = Column(Integer, default=lambda: int(time.time()))


class Download(Base):
    __tablename__ = 'download_music'

    id = Column(Integer, primary_key=True)
    sub_id = Column(Integer)
    name = Column(String(200))
    singer = Column(String(100))
    url = Column(String(300))
    lrc = Column(String(300))
    create_at = Column(Integer, default=lambda: int(time.time()))


def init_schema():
    Base.metadata.create_all(bind=engine)
