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
        ]

        # Render the shown page
        self.render(
            'info.html',
            page_title=u'乾阜-'+stock_item[1]+'-'+stock_item[2],
            css_file_name='info',
            stock_item=stock_item,
        )
