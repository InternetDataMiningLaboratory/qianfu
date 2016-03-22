# -*- coding: utf-8 -*-
#
# Author: jimin.huang
#
import base
import logging
from csv_reader import read


class IndexHandler(base.BaseHandler):
    '''
        The handler of the index page.
    '''

    load_num = 10

    def get_stock_items(self):
        datum = read('stock_items.csv')

        return datum

    def get(self):
        # Render the shown page
        self.render(
            'list.html',
            page_title=u'乾阜',
            css_file_name='list',
            jumbotron=u'今日推荐',
        )

    def post(self):
        # Get load times from arguments
        load_times = int(self.get_argument('load_times', -1))

        # Failed to get load times
        if load_times == -1:
            # Write the message that the post is failed
            self.write(str(load_times))
        else:
            # Write data to response
            self.write(
                {
                    'data':
                        self.get_stock_items()[
                            load_times*self.load_num:
                            (load_times+1)*self.load_num
                        ],
                }
            )
