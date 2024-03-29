# -*- coding: utf-8 -*-
# @Time    : 19-10-10 下午1:55
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : app.py
# @Software: PyCharm


import tornado.ioloop
import tornado.web
import tornado.options
from tornado.options import define, options
from tornado.web import URLSpec
from handlers import main, auth


define('port', default='8001', help='Listening port', type=int)


class Application(tornado.web.Application):
    def __init__(self):
        self.SESSION_NAME = 'tudo_cookie'
        handlers = [
            (r"/", main.IndexHandler),
            (r"/explore", main.ExploreHandler),
            URLSpec(r"/post/(?P<post_id>[0-9]+)", main.PostHandler, name='post'),
            (r"/upload", main.UploadHandler),
            (r"/signup", auth.RegisterHander),
            (r"/login", auth.LoginHander),
            (r"/logout", auth.LogoutHander),

        ]
        settings = dict(
            debug=True,
            static_path='static',
            template_path='templates',
            cookie_secret="asdfghjkjjrtetiiu",
            # xsrf_cookies=True,
            login_url = '/login',
            pycket={
                'engine': 'redis',
                'storage': {
                    'host': '127.0.0.1',
                    'port': 6379,
                    # 'password': '',
                    'db_sessions': 5,  # redis db index
                    # 'db_notifications': 11,
                    'max_connections': 2 ** 30,
                },
                'cookies': {
                    'expires_days': 30,
                },
            }
        )

        super().__init__(handlers, **settings)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = Application()
    app.listen(options.port)
    print('Server start on http://127.0.0.1:{}'.format(str(options.port)))
    tornado.ioloop.IOLoop.current().start()
