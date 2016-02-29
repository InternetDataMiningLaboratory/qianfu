# -*- coding: utf-8 -*-
#
# Author: jimin.huang
#
import base
import login


class RegisterHandler(base.BaseHandler):
    '''
        The handler of the register page.
    '''

    def get(self):
        # Render the shown page
        self.render(
            'login_register.html',
            page_title=u'乾阜-登录',
            css_file_name=u'login_register',
            box_type='register',
        )
