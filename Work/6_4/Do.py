a = [1,2,3,4]
b = (2*x for x in a)
c = [2*x for x in a]
b


for i in b:
    print(i, end = ' ')
b

for i in c:
    print(i, end = ' ')
c

d = sum(x*x for x in a)

d

nums = [1,2,3,4,5]
squares = (x**2 for x in nums)
squares

for n in squares:
    print(n)
    
nums = [1,2,3,4,5]
sum([x*x for x in nums])
sum(x*x for x in nums)

def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row
            
rows = []
names = []
            
rows = [row for row in rows if row['name'] in names]