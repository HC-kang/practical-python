import csv

def read_portfolio(filename):
    '''
    read portfolio file
    '''
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        
        for row in rows:
            record = dict(zip(headers, row))
            stock = {
                'name' : record['name'],
                'shares': int(record['shares']),
                'price': float(record['price'])
            }
            portfolio.append(stock)
    
    return portfolio

def read_price(filename):
    '''
    read Price csv
    '''
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
    
    return prices

def make_report_data(portfolio, prices):
    '''
    make report data
    '''
    
    rows = []
    for stock in portfolio:
        current_price = prices[stock['name']]
        change = current_price - stock['price']
        summary = (stock['name'], stock['shares'], current_price, change)
        rows.append(summary)
    return rows

def print_report(reportdata):
    '''
    print report
    '''
    
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for row in reportdata:
        print('%10s %10d %10.2f %10.2f' % row)
        
def portfolio_report(portfoliofile, pricefile):
    '''
    test
    '''
    portfolio = read_portfolio(portfoliofile)
    prices = read_price(pricefile)
    
    report = make_report_data(portfolio, prices)
    
    print_report(report)
    
portfolio_report('../Data/portfolio.csv',
                 '../Data/prices.csv')