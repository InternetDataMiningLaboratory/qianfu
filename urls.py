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

urls = [
    (r"/", handler.index.IndexHandler),
    (r".*", handler.base.BaseHandler),
]
