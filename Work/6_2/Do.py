for x in countdown(10):
    print(x, end = ' ')
    
    
def countdown(n):
    while n > 0:
        yield n
        n-=1
        
        
x = countdown(10)

x
print(x)

x.__next__()

next(x)

def filematch(filename, substr):
    with open(filename, 'r') as f:
        for line in f:
            if substr in line:
                yield line
                
for line in open('../Data/portfolio.csv'):
    print(line, end = '')
    
for line in filematch('../Data/portfolio.csv', 'IBM'):
    print(line, end = '')