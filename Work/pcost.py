# pcost.py
#
# Exercise 1.27

import sys

def portfolio_cost(filename):
    '''
    test
    '''
    tot_cost = 0
    data = open(filename, 'rt')
    headers = next(data)
    headers
    for line in data:
        _, i, j = line.split(',')
        tot_cost += float(i) * float(j)
    return tot_cost
    
    
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
    
portfolio_cost('Data/portfolio.csv')
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

