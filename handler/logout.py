# -*- coding: utf-8 -*-
#
# Author: jimin.huang
#
import base


# TODO: Using modal and POST method rather than GET method to logout

class LogoutHandler(base.BaseHandler):
    '''
        The handler of logout.
    '''
    def get(self):
        self.clear_all_cookies()
        self.redirect('/')
