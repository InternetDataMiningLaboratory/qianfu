# -*- coding: utf-8 -*-
#
# Author: jimin.huang
#
import base


class IndexHandler(base.BaseHandler):
    '''
        The handler of the index page.
    '''
    def get(self):
        # Render the shown page
        self.render(
            'index.html',
            page_title=u'乾阜',
        )
