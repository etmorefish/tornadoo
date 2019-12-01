# -*- coding: utf-8 -*-
# @Time    : 19-11-27 下午10:27
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : auth.py
# @Software: PyCharm
from hashlib import md5
from models.auth import User, Post
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

def add_post(img_url, thumb_url, username):
    session = Session()
    user = session.query(User).filter_by(username=username).first()
    post = Post(image_url=img_url, thumb_url=thumb_url, user_id=user.id)
    session.add(post)
    session.commit()
    post_id = post.id
    session.close()
    return post_id

def get_all_posts(username=None):
    '''
    查询获取所有图片或者是特定的用户
    :param username:如果没做，就是获取全部图片
    :return:
    '''
    session = Session()
    if username:
        user = session.query(User).filter_by(username=username).first()
        posts = session.query(Post).filter_by(user=user).all()

    else:
        posts = session.query(Post).all()
    if posts:
        return posts
    else:
        return []

def get_post(post_id):
    session = Session()
    post = session.query(Post).filter_by(id=post_id).scalar()
    return post

