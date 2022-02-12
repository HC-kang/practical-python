# pcost.py
#
# Exercise 1.27

import sys
import csv

def portfolio_cost(filename):
    '''
    test
    '''
    tot_cost = 0
    f = open(filename, 'rt')
    rows = csv.reader(f)
    headers = next(rows)
    headers
    for rowno, row in enumerate(rows, start = 1):
        record = dict(zip(headers, row))
        record
        try:
            nshares = int(record['shares'])
            price = float(record['price'])
            tot_cost += nshares * price
        except ValueError:
            print(f"Row {rowno}: Couldn't convert: {row}")
    return tot_cost
    
    
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
    
portfolio_cost('Data/portfolio.csv')
portfolio_cost('Data/portfoliodate.csv')
portfolio_cost('Data/missing.csv')
cost = portfolio_cost(filename)
print('Total_cost : ', cost)

# data = []
# tot_cost = 0

# with open('Data/portfolio.csv', 'rt') as file:
#     for line in file:
#         data.append(line.replace('\n', '').split(','))
        
# data = data[1:]

# for i, j, k in data:
#     tot_cost += float(j) * float(k)

# print('Total cost :', tot_cost)

