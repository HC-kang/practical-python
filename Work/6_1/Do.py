a = 'hello'

for c in a:
    print(c)
    
b = {'name': 'Dave', 'password': '123'}

for k in b:
    print(b[k])

    
    
a

_iter = a.__iter__()

while True:
    try:
        print(_iter.__next__())
    except StopIteration:
        break
    
    
    
x = [1,2,3,4,5,6,7,8,9,0]

it = x.__iter__()
it

it.__next__()

a
i = a.__iter__()

i.__next__()

i = x.__iter__()
next(i())

i.__next__()

i  = x.__iter__

j = i()

j.__next__()

i = x.__iter__()

next(i)


import report
report.portfolio_report('../Data/portfolio.csv', '../Data/prices.csv')

import report

portfolio = report.read_portfolio('../Data/portfolio.csv')
len(portfolio)
portfolio[0]

portfolio.__dict__
'IBM' in portfolio