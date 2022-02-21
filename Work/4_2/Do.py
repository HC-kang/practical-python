class Parent:
    def __init__(self):
        return 0
    
class Child(Parent):
    def __init__(self):
        return 0
    

from stock import MyStock, Stock

s = MyStock('GooG', 100, 490.1)
ss = Stock('GooG', 100, 490.1)

s.sell(25)

s.shares

s.panic()
s.shares


s.cost()
ss.cost()

s.cost2()

s = MyStock('GooG', 100, 490.1, 1)


s = MyStock('GooG', 100, 1)

import report

report.portfolio_report('../Data/portfolio.csv', '../Data/prices.csv', 'csv')

a = 'port.csv'
a.split('.')[1]