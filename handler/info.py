# -*- coding: utf-8 -*-
#
# Author: jimin.huang
#
import base
import tornado.web
from csv_reader import read


class InfoHandler(base.BaseHandler):
    '''
        The handler of the info page.
    '''
    def get_company(self):
        datum = read('company.csv')
        datum[0] = [name.strip('\n') for name in datum[0]]
        return dict(zip(datum[0], datum[1]))

    def get_executives(self):
        datum = read('executives.csv')[1:]
        for executive in datum:
            executive[3] = executive[3].decode('utf8')
            if executive[3] == u'执行董事':
                executive[1] = 1
            if executive[3] == u'非执行董事':
                executive[1] = 2
            if executive[3] == u'独立董事':
                executive[1] = 3
        return sorted(datum, key=lambda x: x[1])

    def get_transaction_history(self):
        datum = read('transaction_history.csv')[1:41]

        def new_data(data):
            data[1] = data[1].split()[0]
            return [
                data[1], data[11], data[7], data[8], data[9], data[6],
                data[15], data[13], data[14], data[3], data[2], data[16]
            ]
        return map(new_data, datum)

    def get_flow_history(self):
        datum = read('flow_history.csv')[1:41]

        def new_data(data):
            data[0] = data[0].split()[0]
            data.pop(1)
            return data
        return map(new_data, datum)

    def get_company_news(self):
        datum = read('company_news.csv')[1:31]

        return datum

    def get_research_reports(self):
        datum = read('research_reports.csv')[1:31]
        return datum

    def get_main_financial_report(self):
        datum = read('main_financial_report.csv')
        datum = [ data[1:] for data in datum ]
        return datum

    def get_debt_financial_report(self):
        datum = read('debt_financial_report.csv')
        datum = [ data[1:] for data in datum ]
        return datum

    def get_benefit_financial_report(self):
        datum = read('benefit_financial_report.csv')
        datum = [ data[1:] for data in datum ]
        return datum

    def get_cash_financial_report(self):
        datum = read('cash_financial_report.csv')
        datum = [ data[1:] for data in datum ]
        return datum

    @tornado.web.authenticated
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
                [2011, 2012, 2013, 2014, 2015, 2016],
                [0.0423, 0.0153, -0.01678, -0.01778, -0.01892, 0.0462],
                [6, 13, 4, 4, 4, 3],
            ],
            [
                [2011, 2012, 2013, 2014, 2015, 2016],
                [89, 78, 67, 79, 88, 91],
                [83, 79, 69, 81, 89, 90],
                [91, 73, 61, 73, 85, 89],
            ],
            [
                ['买入价', 12.72, 12.80, 12.83, 12.81, 12.80],
                ['卖出价', 13.07, 13.06, 13.03, 13.10, 12.90],
            ],
            self.get_company(),
            self.get_executives(),
            self.get_transaction_history(),
            self.get_flow_history(),
            self.get_company_news(),
            self.get_research_reports(),
            self.get_main_financial_report(),
            self.get_debt_financial_report(),
            self.get_benefit_financial_report(),
            self.get_cash_financial_report(),
        ]

        # Render the shown page
        self.render(
            'info.html',
            page_title=u'乾阜-'+stock_item[1]+'-'+stock_item[2],
            css_file_name='info',
            stock_item=stock_item,
        )
