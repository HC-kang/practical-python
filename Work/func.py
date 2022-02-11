def sumcount(n):
    total = 0
    while n > 0:
        total += n
        n -= 1
        return total
    

import math

x = math.sqrt(10)
x

import urllib.request
u = urllib.request.urlopen('http://www.python.org/')
data = u.read()

lists = [['Ford', 'John', 'Sherry']]

for i in lists:
    try:
        print(i.index('Mark'))
    except ValueError:
        print("Can't find Mark")


for i in lists:
    try:
        raise RuntimeError('hhh')
    except ValueError:
        print("Can't find Mark")


def greeting(name):
    'Issues a greeting'
    print('Hello', name)
    
    
def check():
    '''
    ㅎㅎㅎㅎ 확인 해 봅시당
    '''
    for i in range(10):
        print('이것도 나오나?',i)
    print('hello')

check()

    
greeting('Ho')

help(greeting)


def portfolio_cost(filename):
    '''
    테스트용입니다.
    '''
    tot_cost = 0
    filepath = 'Data/'+filename
    data = []
    try:
        with open(filepath, 'rt') as file:
            for line in file:
                data.append(line.replace('\n', '').split(','))
            data = data[1:]
    except FileNotFoundError:
        print("Can't find that File")
        return -1

    for _, i, j in data:
        tot_cost += float(i) * float(j)
    
    return tot_cost
    
portfolio_cost('portfol')


import csv
f = open('Data/portfolio.csv')
rows = csv.reader(f)
headers = next(rows)
headers

for row in rows:
    print(row)
f.close()