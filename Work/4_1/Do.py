from cv2 import line
from soupsieve import select
import stock

a = stock.Stock('GooG', 100, 490.1)

a

a.name
a.shares

a.cost()
a.sell(25)
a.cost()

import fileparse

with open('../Data/portfolio.csv') as lines:
    portdicts = fileparse.parse_csv(lines, select = ['name', 'shares', 'price'], types = [str, int, float])
    
portfolio = [stock.Stock(d['name'], d['shares'], d['price']) for d in portdicts]

portfolio

sum([s.cost() for s in portfolio])

import pcost
pcost.portfolio_cost('../Data/portfolio.csv')

import report
report.portfolio_report('../Data/portfolio.csv', '../Data/prices.csv')