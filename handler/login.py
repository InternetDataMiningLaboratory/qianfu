# -*- coding: utf-8 -*-
#
# Author: jimin.huang
#
import base


class LoginHandler(base.BaseHandler):
    '''
        The handler of the login page.
    '''
    # temp user list
    temp_user_list = {
        'admin':'admin',
    }

    def get(self):
        # Render the shown page
        self.render(
            'login_register.html',
            page_title=u'乾阜-登录',
            css_file_name=u'login_register',
            box_type='login',
        )
    
    def post(self):
        # Check username and password
        username = self.get_argument('username', None)
        password = self.get_argument('password', None)

        # If username and password is right
        if username and password\
            and password == self.temp_user_list.get(username):
            # Write username to cookie so we can check it
            self.set_secure_cookie('username', username)
            # next is a parameter which points to the formal page
            self.redirect(self.get_argument('next', '/'))
