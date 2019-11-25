# -*- coding: utf-8 -*-
# @Time    : 19-11-24 下午4:58
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : db.py
# @Software: PyCharm


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'tudo'
USERNAME = 'root'
PASSWORD = 'sixqwe123'

Db_Uri = 'mysql+pymysql://{}:{}@{}/{}?charset=utf8'.format(
    USERNAME,PASSWORD,HOSTNAME,DATABASE)

engine = create_engine(Db_Uri)

Base = declarative_base(engine)

Session = sessionmaker(bind=engine)

if __name__=='__main__':
    connection = engine.connect()
    result = connection.execute('select 1')
    print(result.fetchone())
