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
        stock_items = [['1', '000001', '平安银行', '89'] for index in xrange(10)]

        # Render the shown page
        self.render(
            'list.html',
            page_title=u'乾阜',
            css_file_name='list',
            jumbotron=u'今日推荐',
            stock_items=stock_items,
        )
