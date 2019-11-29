# -*- coding: utf-8 -*-
# @Time    : 19-11-23 下午11:22
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : main.py
# @Software: PyCharm
import tornado.web

from pycket.session import SessionMixin


class BaseHandler(tornado.web.RequestHandler, SessionMixin):
    def get_current_user(self):
        return self.session.get("tudo_cookie")


class IndexHandler(BaseHandler):
    '''
    首页 用户上传图片的展示
    '''
    @tornado.web.authenticated
    def get(self):
        self.render('index.html', img_list=[])


class PostHandler(BaseHandler):
    '''
    单个图片的详情页
    '''
    @tornado.web.authenticated
    def get(self, post_id):
        self.render('post.html', post_id=post_id)


class ExploreHandler(BaseHandler):
    '''
    最近上传的缩略图页面
    '''
    def get(self):
        self.render('explore.html', img_list=[])



