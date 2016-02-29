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
            page_title=u'乾阜-注册',
            css_file_name=u'login_register',
            box_type='register',
        )
    
    def post(self):
        # Get parameters
        username = self.get_argument("username", None)
        password = self.get_argument("password", None)
        mail = self.get_argument("mail", None)

        # Check parameters
        if username not in login.LoginHandler.temp_user_list:
            # Register user
            login.LoginHandler.temp_user_list[username] = password
            self.redirect('/login')
        else:
            self.redirect('/register')
