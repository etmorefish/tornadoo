# -*- coding: utf-8 -*-
# @Time    : 19-11-30 下午9:52
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : photo.py
# @Software: PyCharm

import  uuid
import os

class UploadImage(object):
    '''
    辅助保护用户上传的图片，记录图片相关的url 用来保存到数据库
    '''
    upload_dir = 'uploads'

    def __init__(self, ext, static_path):
        self.ext = ext
        self.new_name = self.gen_new_name()
        self.static_path = static_path

    def gen_new_name(self):
        # return '.'.join([uuid.uuid4().hex, self.ext])
        return uuid.uuid4().hex + self.ext

    @property
    def image_url(self):
        return os.path.join(self.upload_dir, self.new_name)

    @property
    def save_to(self):
        return os.path.join(self.static_path, self.image_url)

    def save_content(self, content):
        with open(self.save_to, 'wb') as f:
            f.write(content)

