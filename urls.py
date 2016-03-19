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
import handler.search_result
import handler.login
import handler.register
import handler.logout
import handler.info

urls = [
    (r"/", handler.index.IndexHandler),
    (r"/search", handler.search.SearchHandler),
    (r"/login", handler.login.LoginHandler),
    (r"/logout", handler.logout.LogoutHandler),
    (r"/info/(\d+)", handler.info.InfoHandler),
    (r"/search_result", handler.search_result.SearchResultHandler),
    (r"/register", handler.register.RegisterHandler),
    (r".*", handler.base.BaseHandler),
]
