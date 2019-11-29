# -*- coding: utf-8 -*-
# @Time    : 19-11-23 下午11:22
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : main.py
# @Software: PyCharm
import tornado.web
from PIL import Image
from pycket.session import SessionMixin

from utils.auth import add_post, get_all_posts, get_post


class BaseHandler(tornado.web.RequestHandler, SessionMixin):
    def get_current_user(self):
        return self.session.get("tudo_cookie")


class IndexHandler(BaseHandler):
    '''
    首页 用户上传图片的展示
    '''

    @tornado.web.authenticated
    def get(self):
        posts = get_all_posts()
        self.render('index.html', img_list=posts)


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
        self.render('explore.html', img_list=[])


class UploadHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        return self.render('upload.html')

    def post(self):
        post_id = None
        file_list = self.request.files.get('picture', [])
        for img_dict in file_list:  # {"filename":..., "content_type":..., "body":...}
            filename = img_dict['filename']
            print(filename)
            print(img_dict['content_type'])
            save_path = 'static/images/{}'.format(filename)
            with open(save_path, 'wb') as f:
                f.write(img_dict['body'])

            # 把图片变成缩略图
            img = Image.open(save_path)
            img.thumbnail((200, 200))
            img.save('static/images/thum_{}'.format(filename), 'JPEG')

            post_id = add_post('images/{}'.format(filename), self.current_user)
        if post_id:
            self.redirect('/post/{}'.format(str(post_id)))
        else:
            self.write('upload error')
