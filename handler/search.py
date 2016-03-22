# -*- coding: utf-8 -*-
#
# Author: jimin.huang
#
import base
import tornado.web


class SearchHandler(base.BaseHandler):
    '''
        The handler of the search page.
    '''
    @tornado.web.authenticated
    def post(self):
        search_word = self.get_argument('search_word', '')

        self.redirect('/search_result?q='+search_word)
