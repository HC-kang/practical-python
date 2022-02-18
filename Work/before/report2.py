import fileparse2 as fp2

def printReport(filePortfolio, filePrices):
    portfolio = fp2.read_portfolio(filePortfolio)
    prices = fp2.read_prices(filePrices)
    headers = ['Name', 'Shares', 'Price', 'Change']
    print()
    for h in headers:
        print(f'{h:>10s}', end =' ')
    print()
    for _ in headers:
        print('-'*10, end = ' ')
    print()
    for stock in portfolio:
        _name = stock['name']
        _shares = stock['shares']
        _price = prices[stock['name']]
        _change = (_price - stock['price']) * _shares
        print(f'{_name:>10s} {_shares:>10d} {_price:>10.2f} {_change:>10.2f}')
    
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 3:
        printReport(sys.argv[1], sys.argv[2])

