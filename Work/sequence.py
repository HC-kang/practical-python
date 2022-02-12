# a = 'Hello'
# b = [1,4,5]
# c = ('GOOG', 100, 490.1)

# a[0]
# b[-1]
# c[1]

# len(a)
# len(b)
# len(c)

# a * 3

# b * 2

# a = (1,2,3)
# b = (4,5)

# a+b

# c = [1,4]
# a + c

# a = [0,1,2,3,4,5,6,7,8]

# a[2:5]

# a[-5:]

# a[:3]

# a

# a[2:4] = [123,234,345,456,567]
# a

# del a[2:6]
# a

# s = [1,2,3,4]
# sum(s)
# min(s)
# max(s)

# t = ['Hello', 'World']
# max(t)

# import time

# def printer1():
#     start = time.time()
#     for i, j in enumerate(range(20000)):
#         print(i, j)
#     end = time.time()
#     print('time', round(end - start, 2), 'sec')

# def printer2():
#     start = time.time()
#     j = 0
#     for i in range(20000):
#         j += 1
#         print(i, j)
#     end = time.time()
#     print('time', round(end - start, 2), 'sec')
    
# printer1()
# printer2()

# columns = ['name', 'shares', 'price']
# values = ['GOOG', 100, 490.1]
# pairs = zip(columns, values)

# for column, value in pairs:
#     print(column, value)
    
# d = dict(pairs)
# d

# for n in range(10):
#     print(n, end = ' ')
    
# for n in range(10, 0, -1):
#     print(n, end = ' ' )
    
# for n in range(0, 10, 2):
#     print(n, end = ' ')
    
    
import csv

def portfolio_cost(filename):
    data = open(filename, 'rt')
    rows = csv.reader(data)
    headers = next(rows)
    print(headers)
    print('----------')
    for rowno, row in enumerate(rows, start = 1):
        try:
            print(list((row[0], row[1], row[2])))
        except IndexError:
            print(f"Row {rowno}: Couldn't convert")

portfolio_cost('Data/missing.csv')


prices = {
    'GOOG': 490.1,
    'AA': 23.45,
    'IBM': 91.1,
    'MSFT': 34.23,
}

prices.items()

pricelist = list(zip(prices.values(), prices.keys()))
pricelist

a = [1,2,3,4]
b = ['w', 'x', 'y','z']
c = [0.2, 0.4, 0.6, 0.8]

list(zip(a,b,c))

a = [1,2,3,4,5,6]
b = ['x', 'y', 'z']

list(zip(a,b))