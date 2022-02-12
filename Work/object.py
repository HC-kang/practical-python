a = [1,2,3]
b = a
c = [a,b]


a
b
c

a.append(999)

a = [1,2,3]
b = a
a is b
b = [1,2,3]

a == b
a is b

a = [2,3, [100, 101], 4]
b = list(a)
a is b

a[2].append(102)
b[2]

a = [2,3,[100, 101], 4]
import copy
b = copy.deepcopy(a)
a[2].append(102)
b[2]

if isinstance(a, list):
    print('a is a list')
    
if isinstance(a, (list, tuple)):
    print('a is a list or tuple')
    
import math
items = [abs, math, ValueError]
items

items[0](-45)

items[1].sqrt(2)

try:
    x = int('not a number')
except items[2]:
    print('Failed')
    

types = [str, int, float]

import csv
f = open('Data/portfolio.csv', 'rt')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)
row

row[1] * row[2]

types[1](row[1])

types[2](row[2])

types[0](row[0])


types[1](row[1])*types[2](row[2])

r = list(zip(types, row))
r

converted = []
for func, val in zip(types, row):
    converted.append(func(val))
    
converted

converted = [func(val) for func, val in zip(types, row)]


f = open('Data/dowstocks.csv', 'rt')
rows = csv.reader(f)
headers = next(rows)
headers
row = next(rows)
row

types = [str, float, str, str, float, float, float, float, int]
converted = [func(val) for func, val in zip(types, row)]
record = dict(zip(headers, converted))

record


s = '6/11/2007'
ss = tuple(s.split('/'))
ss