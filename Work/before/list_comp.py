a = [1,2,3,4,5]
b = [2*x for x in a]

b

names = ['Elwood', 'Jake']
a = [name.lower() for name in names]
a

a = [1, -5, 4, 2, -2, 10]
b = [2*x for x in a if x>0]
b

stockname = [s['name'] for s in stocks]

a = [s for s in stock if s['price'] > 100 and s['share'] > 50]

cost = sum([s['shares']*s['price'] for s in stocks])


nums = [1,2,3,4]
squares = [x**2 for x in nums]
squares

twice = [2*x for x in nums if x>2]

twice

from report import read_portfolio

portfolio = read_portfolio('Data/portfolio.csv')
portfolio

cost = sum([stock[1] * stock[2] for stock in portfolio])
cost


import csv
portfolio = []
data = open('Data/portfolio.csv', 'rt')
rows = csv.reader(data)
headers = next(rows)
headers
for row in rows:
    portfolio.append({'name': row[0], 'shares': int(row[1]), 'price': float(row[2])})

portfolio

from collections import Counter
holdings = Counter()

for s in portfolio:
    holdings[s['name']] += s['shares']
    
holdings

more100 = [s for s in portfolio if s['shares'] > 100]
more100

msftibm = [s for s in portfolio if s['name'] in {'MSFT', 'IBM'}]
msftibm

cost10k = [s for s in portfolio if s['shares'] * s['price'] > 10000]
cost10k

name_shares = [(s['name'], s['shares']) for s in portfolio]
name_shares

names = {s['name'] for s in portfolio}
names

holdings = {name: 0 for name in names}

holdings

for s in portfolio:
    holdings[s['name']] += s['shares']

holdings

data = open('Data/prices.csv')
prices = {}
rows = csv.reader(data)
for row in rows:
    try:
        prices[row[0]] = row[1]
    except IndexError:
        pass
prices

portfolio_prices = {name: prices[name] for name in names}
portfolio_prices

import csv

f = open('Data/portfoliodate.csv')
rows = csv.reader(f)
headers = next(rows)
headers

select = ['name', 'shares', 'price']

indices = [headers.index(colname) for colname in select]
indices

row = next(rows)
record = {colname: row[index] for colname, index in zip(select, indices)}

record

portfolio = [{colname: row[index] for colname, index in zip(select, indices)} for row in rows]

portfolio