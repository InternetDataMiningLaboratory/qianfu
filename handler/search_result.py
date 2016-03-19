# -*- coding: utf-8 -*-
#
# Author: jimin.huang
#
import base
import tornado.web
from csv_reader import read


class SearchResultHandler(base.BaseHandler):
    '''
        The handler of the search result page.
    '''

    load_num = 10

    def get_stock_items(self):
        datum = read('stock_items.csv')

        return datum

    def search_for_stock_items(self, search_word):
        return [
            item for item in self.get_stock_items()
            if search_word in item[1].decode('utf8')+item[2].decode('utf8')
        ]

    @tornado.web.authenticated
    def get(self):
        search_word = self.get_argument('q')
        # Render the shown page
        self.render(
            'list.html',
            page_title=u'乾阜-"{0}"搜索结果'.format(search_word),
            css_file_name='list',
            jumbotron=u'\"{0}\" 搜索得到 {1} 支相关股票'.format(
                search_word,
                len(self.search_for_stock_items(search_word)),
            ),
        )

    @tornado.web.authenticated
    def post(self):
        # Get load times from arguments
        load_times = int(self.get_argument('load_times', -1))
        search_word = self.get_argument('q')
        search_result = self.search_for_stock_items(search_word)[
            load_times*self.load_num:
            (load_times+1)*self.load_num
        ]

        # Failed to get load times
        if (
            load_times == -1 or search_word is None
            or len(search_result) == 0
            or (
                len(search_result) < self.load_num
                and load_times == 1
            )
        ):
                # Write the message that the post is failed
                self.write(str(-1))
        else:
            # Write data to response
            self.write(
                {
                    'data': search_result,
                }
            )
