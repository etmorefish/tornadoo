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


def register(username, password1, password2):
    ret = {
        'msg':'other error',
        'user_id': None
    }
    if username and password1 and password2:
        if password1 == password2:
            session = Session()
            user = session.query(User).filter_by(username=username).all()
            if user:
                msg = 'username is exists'
            else:
                new_user = User(username=username, password=hash(password1))
                session.add(new_user)
                session.commit()
                ret['user_id'] = new_user.id
                session.close()
                msg = 'ok'
        else:
            msg = 'password1 != password2'
    else:
        msg = 'username or password is empty'
    ret['msg'] = msg
    return ret




def authentic(username, password):
    if username and password:
        result = User.is_exists(username, hash(password))
        if result:
            msg = 'ok'
        else:
            msg = 'username / password not match'
    else:
        result = False
        msg = 'empty username or password'
    ret = {
        'msg':msg,
        'result':result,
    }
    return ret