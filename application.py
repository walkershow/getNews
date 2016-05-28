#-*- coding: utf-8 -*
__author__ = 'Howie'
import tornado.web
import os
from handlers.index import IndexHandler
from handlers.admin import AdminHandler
from handlers.newsManage import NewsManage
from handlers.userManage import UserManage
from handlers.changePass import ChangePass
from handlers.dataOperator import DataOperator

url = [
    (r'/', IndexHandler),
    (r'/admin',AdminHandler),
    (r'/newsManage',NewsManage),
    (r'/userManage',UserManage),
    (r'/changePass',ChangePass),
    (r'/dataOperator',DataOperator),
]

setting = dict(
    template_path = os.path.join(os.path.dirname(__file__), "templates"),
    static_path = os.path.join(os.path.dirname(__file__), "static"),
    cookie_secret = "XQ5rhITaQ1m7HoN40CcggWPCvR2jqUn1tY9E3kWU+yc=",
    #xsrf_cookies = True,
    debug = True,
    login_url = '/',
)

application = tornado.web.Application(
    handlers = url,
    **setting
)