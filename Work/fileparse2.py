import csv
import enum

def read_portfolio(filename):
    '''
    portfolio 파일을 읽어 Dict들의 List로 반환합니다.
    '''
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        portfolio = []
        for rowNo, row in enumerate(rows):
            try:
                row = [row[0], int(row[1]), float(row[2])]
                portfolio.append(dict(zip(headers, row)))
            except ValueError:
                throwValueErrorFromRow(rowNo)
            
    return portfolio
        
def read_prices(filename):
    '''
    prices 파일을 읽어 Dict들의 List로 반환합니다.
    '''
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        prices = {}
        for rowNo, row in enumerate(rows):
            try:
                row = [row[0], float(row[1])]
                prices[row[0]] = row[1]
            except IndexError:
                # throwIndexErrorFromRow(rowNo)
                pass
    return prices

def throwIndexErrorFromRow(rowNo):
    raise IndexError(f"Row {rowNo} : Can't read this Row.")

def throwValueErrorFromRow(rowNo):
    raise ValueError(f"Row {rowNo} : Can't read this Row.")
            
