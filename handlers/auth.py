# -*- coding: utf-8 -*-
# @Time    : 19-11-27 下午10:01
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : auth.py
# @Software: PyCharm
from utils.auth import register
from .main import BaseHandler


class RegisterHander(BaseHandler):


    def get(self):
        msg = self.get_argument('msg', '')
        self.render('signup.html', next_url='/', msg=msg)

    def post(self):
        username = self.get_argument('name', '')
        password1 = self.get_argument('password1', '')
        password2 = self.get_argument('password2', '')

        if username and password1 and password2:
            if password1 == password2:
                ret = register(username, password1)
                if ret:
                    self.session.set('tudo_cookie', username)
                    self.redirect('/')
                else:
                    msg = 'register fail'
            else:
                msg = 'password error'
        else:
            msg = 'username or password is empty'
        self.redirect('/signup?msg={}'.format(msg))

