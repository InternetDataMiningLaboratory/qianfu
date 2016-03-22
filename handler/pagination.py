# -*- coding: utf-8 -*-
#
# Author: jimin.huang
#
import base
import tornado.web
from csv_reader import read


class PaginationHandler(base.BaseHandler):
    '''
        The handler of the pagination module.
    '''
    @tornado.web.authenticated
    def post(self, name):
        call_function = None
        try:
            call_function = getattr(self, name)
        except AttributeError:
            self.write("failed")
            return
        else:
            self.write(call_function(self.get_argument('index', None)))

    def news(self, index):
        page_size = 10
        index = int(index)
        datum = read('company_news.csv')
        data = [
            self.render_string("news_item.html", news=news)
            for news in datum[index*page_size: (index+1)*page_size]
        ]
        page_num = len(datum)/page_size - 1
        page_num += 0 if len(datum)%page_size==0 else 1
        return {
                'data': data,
            'page_num': page_num,
        }
