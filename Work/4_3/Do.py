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

