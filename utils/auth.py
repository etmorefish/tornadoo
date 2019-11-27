# -*- coding: utf-8 -*-
# @Time    : 19-11-27 下午10:27
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : auth.py
# @Software: PyCharm
from hashlib import md5
from models.auth import User
from models.db import  Session

SALT = 'lilei'
def hash(text):
    return md5('{}{}'.format(text, SALT).encode()).hexdigest()


def register(username, password):
    ret = {}
    new_user = User(username=username, password=hash(password))
    session = Session()
    session.add(new_user)
    session.commit()
    session.close()
    ret['user'] = 'ok'

    return ret