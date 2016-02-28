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

urls = [
    (r"/", handler.index.IndexHandler),
    (r"/search", handler.search.SearchHandler),
    (r".*", handler.base.BaseHandler),
]
