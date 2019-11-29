# -*- coding: utf-8 -*-
# @Time    : 19-11-27 下午10:01
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : auth.py
# @Software: PyCharm
from utils.auth import *
from .main import BaseHandler


class RegisterHander(BaseHandler):


    def get(self):
        msg = self.get_argument('msg', '')
        self.render('signup.html', next_url='/', msg=msg)

    def post(self):
        username = self.get_argument('name', '')
        password1 = self.get_argument('password1', '')
        password2 = self.get_argument('password2', '')

        ret = register(username, password1, password2)
        if ret['msg'] == 'ok':
            self.session.set('tudo_cookie', username)
            self.redirect('/')
        else:
            self.redirect('/signup?msg={}'.format(ret['msg']))





class LoginHander(BaseHandler):
    def get(self):
        msg = self.get_argument('msg', '')
        next_url = self.get_argument('next', None)
        if next_url:
            msg = 'require login for load “{}”'.format(next_url)
        else:
            next_url = '/'
        self.render('login.html', next_url=next_url, msg=msg)

    def post(self):
        username = self.get_argument('name', '')
        password = self.get_argument('password', '')

        ret = authentic(username, password)
        if ret['result']:
            self.session.set('tudo_cookie', username)
            next_url = self.get_argument('next_url', '/')
            self.redirect(next_url)
        else:
            # msg = ret['msg'] or 'username or password error'
            self.redirect('/login?msg={}'.format(ret['msg']))


class LogoutHander(BaseHandler):
    def get(self):
        self.session.delete('tudo_cookie')
        self.write('logout done')