def filematch(lines, substr):
    for line in lines:
        if substr in line:
            yield line


from matplotlib import ticker
import follow

lines = follow.follow('../Data/stocklog.csv')
ibm = filematch(lines, 'IBM')
for line in ibm:
    print(line)
    

from follow import follow
import csv

lines = follow('../Data/stocklog.csv')
rows = csv.reader(lines)
for row in rows:
    print(row)
    
from follow import follow
import csv

lines = follow('../Data/stocklog.csv')
rows = csv.reader(lines)
for row in rows:
    for split in row:
        print(split)
        

import report
import ticker
import follow
import csv

def ticker(portfoliofile, logfile):
    portfolio = report.read_portfolio(portfoliofile)
    rows = parse_stock_data(follow.follow(logfile))
    rows = filter_symbols(rows, portfolio)
    headers = ['Name', 'Price', 'Change']
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s}')
    print(('-'*10+' ')*len(headers))
    for row in rows:
        print(f'{row["name"]:>10s} {row["price"]:>10.2f} {row["change"]:>10.2f}')
        # print(row)
        # print(f'{row[0]:>10s} {row[1]:>10.2f} {row[2]:>10.2f}')
        
ticker('../Data/portfolio.csv', '../Data/stocklog.csv')


def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows

def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]
        
def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]        
        
def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))
        
def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row
