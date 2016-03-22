# -*- coding: utf-8 -*-
#
# Author: jimin.huang
#
# -*- coding: utf-8 -*-
#
# Author: jimin.huang
#
'''
    The test module for the test of modules
'''
import tornado.web


class PaginationModule(tornado.web.UIModule):

    def render(self, pagination_source):
        return self.render_string(
            "module/pagination.html",
            pagination_source=pagination_source, 
        )

    def javascript_files(self):
        return '/static/js/pagination.js'
