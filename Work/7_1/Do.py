def avg(x, *more):
    return float(x + sum(more)) / (1+len(more))

avg(10, 11)

avg(3,4,5)

data = ('GooG', 100, 490.1)

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
        
s = Stock(data)
s = Stock(*data)
s

data = {'name': 'GooG', 'shares': 100, 'price': 490.1}

s = Stock(data)
s = Stock(*data)
s = Stock(**data)
s.__dict__


import report

port = report.read_portfolio('../Data/missing.csv')
port = report.read_portfolio('../Data/missing.csv', silence_errors = True)
