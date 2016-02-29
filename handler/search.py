# -*- coding: utf-8 -*-
#
# Author: jimin.huang
#
import base
import tornado.web


class SearchHandler(base.BaseHandler):
    '''
        The handler of the search page.
    '''
    @tornado.web.authenticated
    def post(self):
        search_word = self.get_argument('search_word', 'XXX')
        stock_items = [['1', '000001', '平安银行', '89'] for index in xrange(10)]

        # Render the shown page
        self.render(
            'list.html',
            page_title=u'乾阜-{0}搜索结果'.format(search_word),
            css_file_name='list',
            jumbotron=u'\"{0}\" 搜索得到10条结果'.format(search_word),
            stock_items=stock_items,
        )
