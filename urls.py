# -*- coding: utf-8 -*-
#
# Author: jimin.huang
#
'''
Set url mapping rules as::

    ('[re_mapping]', handler)
'''
import handler.base
import handler.index
import handler.search
import handler.login
import handler.logout
import handler.info

urls = [
    (r"/", handler.index.IndexHandler),
    (r"/search", handler.search.SearchHandler),
    (r"/login", handler.login.LoginHandler),
    (r"/logout", handler.logout.LogoutHandler),
    (r"/info/(\d+)", handler.info.InfoHandler),
    (r".*", handler.base.BaseHandler),
]
