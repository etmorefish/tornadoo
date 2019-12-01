# -*- coding: utf-8 -*-
# @Time    : 19-11-23 下午11:22
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : main.py
# @Software: PyCharm
import tornado.web
import os
from PIL import Image
from pycket.session import SessionMixin

from utils.auth import add_post, get_all_posts, get_post
from utils.photo import *

SESSION_NAME = 'tudo_cookie'

class BaseHandler(tornado.web.RequestHandler, SessionMixin):
    def get_current_user(self):
        return self.session.get(SESSION_NAME)


class IndexHandler(BaseHandler):
    '''
    首页 用户上传图片的展示
    '''

    @tornado.web.authenticated
    def get(self):
        posts = get_all_posts(self.current_user)
        self.render('index.html', posts=posts)


class PostHandler(BaseHandler):
    '''
    单个图片的详情页
    '''

    @tornado.web.authenticated
    def get(self, post_id):
        post = get_post(int(post_id))
        if post:
            self.render('post.html', post=post)
        else:
            self.send_error(404)


class ExploreHandler(BaseHandler):
    '''
    最近上传的缩略图页面
    '''

    def get(self):
        posts = get_all_posts()

        self.render('explore.html', posts=posts)


class UploadHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        return self.render('upload.html')

    @tornado.web.authenticated
    def post(self):
        post_id = None
        file_list = self.request.files.get('picture', [])

        for img_dict in file_list:  # {"filename":..., "content_type":..., "body":...}
            filename = img_dict['filename']
            print(filename, self.application.settings['static_path'])
            print(img_dict['content_type'])

            _, ext = os.path.splitext(filename)
            # ext = filename.split('.')[-1]
            # print(ext, "-"*20)
            up_im = UploadImage(ext, self.application.settings['static_path'])
            up_im.save_content(img_dict['body'])
            up_im.make_thumb()

            print(up_im.static_path,'\n',up_im.thumb_url)
            post_id = add_post(up_im.image_url, up_im.thumb_url, self.current_user)

            # self.write('upload done')
        if post_id:
            self.redirect('/post/{}'.format(str(post_id)))
        else:
            self.write('upload error')
            # save_path = 'static/images/{}'.format(filename)
            # with open(save_path, 'wb') as f:
            #     f.write(img_dict['body'])

            # 把图片变成缩略图
        #     img = Image.open(up_im.save_to)
        #     img.thumbnail((200, 200))
        #     img.save('static/images/thum_{}'.format(filename), 'JPEG')
        #
        #     post_id = add_post('images/{}'.format(filename), self.current_user)
        # if post_id:
        #     self.redirect('/post/{}'.format(str(post_id)))
        # else:
        #     self.write('upload error')
