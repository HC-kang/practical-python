from cgi import test
from email import header


f = open('./Data/portfolio.csv', 'rt')
data = f.read()
g = open('test.txt', 'wt')
g.write(data)

print(data)

f.close()
g.close()

with open('test.txt', 'rt') as file:
    data = file.read()
    
print(data)

with open('test.txt', 'rt') as f:
    for i, line in enumerate(f):
        print(str(i).zfill(3), end = ' ')
        print(line)
        
        
with open('test_log.txt', 'wt') as logs:
    logs.write('This is Test1111')
    
    
with open('tst.txt', 'wt') as out2:
    print('hello', file = out2)
    print('hello', file = out2)
    

with open('Data/portfolio.csv', 'rt') as f:
    data = f.read()

data = data.split(',')
data = data.split('\n')
data

for i in range(len(data)):
    data[i] = (data[i].split(','))
    
data

data2 = []
for i in range(len(data)):
    for j in data[i]:
        data2.append(j)
        
data2

f = open('Data/portfolio.csv', 'rt')
headers = next(f)
headers
for line in f:
    print(line, end = '')
    
f.close()


import gzip

with gzip.open('Data/portfolio.csv.gz', 'rt') as f:
    for line in f:
        print(line, end ='')