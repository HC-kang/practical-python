# import csv

# def read_portfolio(filename):
#     portfolio = []
#     data = open(filename, 'rt')
#     rows = csv.reader(data)
#     headers = next(data)
#     for row in rows:
#         try:
#             portfolio.append((row[0], int(row[1]), float(row[2])))
#         except ValueError:
#             print('ValueError')
#     return portfolio

# def read_prices(filename):
#     prices = {}
#     data = open(filename, 'rt')
#     rows = csv.reader(data)
#     for row in rows:
#         try:
#             prices[row[0]] = float(row[1])
#         except IndexError:
#             print('Not Enough Data')
#     return prices
        
# def make_report(portfolio, prices):
#     report = []
#     headers = ('Name', 'Shares', 'Price', 'Change')
#     for row in portfolio:
#         try:
#             report.append((row[0], row[1], prices[row[0]], round(prices[row[0]]-row[2], 2)))
#         except IndexError:
#             print('NO stock available')
    
#     for header in headers:
#         print(f'{header:>10s}', end=' ')
#     print()
#     for header in headers:
#         print('-'*10, end = ' ')
#     print() 
#     for r in report:
#         print(f'{r[0]:>10s} {r[1]:>10d} {"$"+str(r[2]):>10s} {r[3]:>10.2f}')
    
#     return report


# if __name__ == '__main__':
#     portfolio = read_portfolio('Data/portfolio.csv')
#     prices = read_prices('Data/prices.csv')
#     make_report(portfolio, prices)


# # report.py
# #
# # Exercise 2.4

# import csv
# from pprint import pprint

# # def portfolio_cost(filename):
# #     '''
# #     test
# #     '''
# #     tot_cost = 0
# #     with open(filename, 'rt') as file:
# #         rows = csv.reader(file)
# #         headers = next(rows)
# #         for _, nShares, price in rows:
# #             tot_cost += int(nShares) * float(price)
    
# #     return tot_cost

# def portfolio_cost(filename):
#     '''
#     test
#     '''
#     portfolio = []
#     with open(filename, 'rt') as file:
#         rows = csv.reader(file)
#         headers = next(rows)
#         for name, nShares, price in rows:
#             holdings = (name, int(nShares), float(price))
#             portfolio.append(holdings)
    
#     return portfolio

# # portfolio_cost('Data/portfolio.csv')

# def read_portfolio(filename):
#     portfolio = []
#     with open(filename, 'rt') as file:
#         rows = csv.reader(file)
#         headers = next(rows)
#         for name, share, price in rows:
#             portfolio.append({'name': name, 'share': share, 'price': price})
#     pprint(portfolio)
#     # return portfolio
            
# # read_portfolio('Data/portfolio.csv')


# import csv

# def read_csv(filename):
#     prices = {}
#     NAcnt = 0
#     f = open(filename, 'rt')
#     rows = csv.reader(f)
#     headers = next(rows)
#     for row in rows:
#         try:
#             prices[row[0]] = float(row[1])
#         except IndexError:
#             NAcnt += 1
#             print('Not Available: ', NAcnt)
        
#     return prices
        
# # read_csv('Data/prices.csv')



# def question():
#     portfolio = portfolio_cost('Data/portfolio.csv')
#     prices = read_csv('Data/prices.csv')
#     profit = 0
#     for stock in portfolio:
#         try:
#             profit += prices[stock[0]] * stock[1]
#             profit -= stock[2] * stock[1]
#         except KeyError:
#             print('Deleted')
        
#     return profit

# # question()

# if __name__ == '__main__':
#     print(question())


# headers = ['Name', 'Shares', 'Price', 'Change']
# print('%10s %10s %10s %10s' % headers)
# print(('-' * 10 + ' ') * len(headers))
# for row in report:
#     print('%10s %10d %10.2f %10.2f' % row)


import csv
def read_portfolio(filename):
    '''
    주식 포트폴리오 파일 읽어, 딕셔너리로 구성된 리스트 생성.
    keys: name, shares, price
    '''
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        
        for row in rows:
            record = dict(zip(headers, row))
            stock = {
                'name': record['name'],
                'shares': int(record['shares']),
                'price': float(record['price'])
            }
            portfolio.append(stock)
    print('read portfolio complete')
    return portfolio

def read_prices(filename):
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        
        for rowno, row in enumerate(rows):
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                print(f'Row {rowno}: Cant do this. skipping...')
    
    print('read prices complete')
    return prices

def make_portfolio_report(portfolioFilename, pricesFilename):
    report = read_portfolio(portfolioFilename)
    prices = read_prices(pricesFilename)
    headers = ['Name', 'Shares', 'Price' ,'Change']
    print()
    print(f'{headers[0]:>10} {headers[1]:>10} {headers[2]:>10} {headers[3]:>10}')
    print(('-'*10 + ' ') * len(headers))
    for stockno, stock in enumerate(report):
        try:
            print(f'{stock["name"]:>10s} {stock["shares"]:>10d} {prices[stock["name"]]:>10.2f} {prices[stock["name"]]-stock["price"]:>10.2f} ')
        except KeyError:
            # print(f'Row {stockno}: Cant find this. skipping...')
            pass



make_portfolio_report('Data/portfolio.csv', 'Data/prices.csv')


    
