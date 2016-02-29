# -*- coding: utf-8 -*-
#
# Author: jimin.huang
#
import base


class InfoHandler(base.BaseHandler):
    '''
        The handler of the info page.
    '''
    def get(self):
        stock_item = ['1', '000001', '平安银行', '89']

        # Render the shown page
        self.render(
            'info.html',
            page_title=u'乾阜-'+stock_item[1]+'-'+stock_items[2],
            css_file_name='info',
            stock_item=stock_item,
        )
