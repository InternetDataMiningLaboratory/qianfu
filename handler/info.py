# -*- coding: utf-8 -*-
#
# Author: jimin.huang
#
import base


class InfoHandler(base.BaseHandler):
    '''
        The handler of the info page.
    '''
    def get(self, stock_id):
        stock_item = [
            '1',
            '000001',
            u'平安银行',
            '89',
            '12.84',
            '1.17',
            '+10.03%',
            '商业银行-贸易',
            [
                [2011,2012,2013,2014,2015,2016],
                [0.0423,0.0153,-0.01678,-0.01778,-0.01892,0.0462],
                [6,13,4,4,4,3],
            ],
            [
                [2011,2012,2013,2014,2015,2016],
                [89, 78, 67, 79, 88, 91],
                [83, 79, 69, 81, 89, 90],
                [91, 73, 61, 73, 85, 89],
            ],
            [
                ['买入价', 12.72, 12.80, 12.83, 12.81, 12.80],
                ['卖出价', 13.07, 13.06, 13.03, 13.10, 12.90],
            ],
        ]

        # Render the shown page
        self.render(
            'info.html',
            page_title=u'乾阜-'+stock_item[1]+'-'+stock_item[2],
            css_file_name='info',
            stock_item=stock_item,
        )
