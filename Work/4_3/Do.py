from datetime import date

from numpy import NaN

d = date(2012, 12, 21)

print(d)

d

str(d)

repr(d)

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        
    def __str__(self):
        return f'{self.year}-{self.month}-{self.day}'
    
    def __repr__(self):
        return f'Date({self.year}, {self.month}, {self.day})'
    

import stock

s = stock.Stock('GOOG', 100, 490.1)
s
s.cost()
c = s.cost

s.cost
c
s == None
ss = stock.Stock(None, 100, 100)

getattr(s, 'name')

k = getattr(ss, 'name', None)
k

hasattr(ss, 'name')
a = getattr(ss, 'name')
a == None
a = getattr(s, 'name')
a == None

import stock
goog = stock.Stock('GOOG', 100, 490.1)
goog

import report

portfolio = report.read_portfolio('../Data/portfolio.csv')
portfolio

import stock
s = stock.Stock('GOOG', 100, 490.1)
columns = ['name', 'shares']
for colname in columns:
    print(colname, '=', getattr(s, colname))


import report
report.portfolio_report('../Data/portfolio.csv', '../Data/prices.csv', 'txt')

portfolio = report.read_portfolio('../Data/portfolio.csv')
from tableformat import create_formatter, print_table

formatter = create_formatter('txt')
print_table(portfolio, ['name', 'shares'], formatter)

from tableformat import create_formatter

formatter = create_formatter('xls')