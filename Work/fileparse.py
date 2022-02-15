# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename, select = None, types = None):
    '''
    CSV파일을 파싱해 레코드의 목록 생성
    '''
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        
        if select:
            indices = [headers.index(s) for s in select]
            headers = select
        else:
            indices = []    
        
        records = []
        for row in rows:
            if not row:
                continue
            if types:
                row = [func(val) for func, val in zip(types, row)]
                
            if indices:
                row = [row[index] for index in indices]
            records.append(dict(zip(headers, row)))
    return records


parse_csv('Data/portfolio.csv', ['price', 'name'], [str, int, float])

def parse_csv2(filename, types = None, has_headers = False):
    '''
    CSV Price 파싱 함수
    '''
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        if has_headers:
            headers = next(rows)
        
        prices = []
        for row in rows:
            if not row:
                continue
            if types:
                row = [func(val) for func, val in zip(types, row)]
            prices.append((row[0], row[1]))
    return prices


parse_csv2('Data/prices.csv', [str, float], True)


def parse_csv3(filename, select = None, types = None, delimiter = ','):
    '''
    CSV파일을 파싱해 레코드의 목록 생성
    '''
    with open(filename) as f:
        rows = csv.reader(f, delimiter = delimiter)
        headers = next(rows)
        
        if select:
            indices = [headers.index(s) for s in select]
            headers = select
        else:
            indices = []    
        
        records = []
        for row in rows:
            if not row:
                continue
            if types:
                row = [func(val) for func, val in zip(types, row)]
                
            if indices:
                row = [row[index] for index in indices]
            records.append(dict(zip(headers, row)))
    return records


parse_csv3('Data/portfolio.dat', ['price', 'name'], [str, int, float], delimiter=' ')


def parse_csv4(filename, select=None, types = None, has_headers = False):
    '''
    CSV Price 파싱 함수
    '''
    if not has_headers and select:
        raise RuntimeError('select argumnet requires column headers')
    
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        if has_headers:
            headers = next(rows)
        
        if select:
            indices = [headers.index(s) for s in select]
            headers = select
        else:
            indices = []
        
        prices = []
        for row in rows:
            if not row:
                continue
            if types:
                row = [func(val) for func, val in zip(types, row)]
            if indices:
                row = [row[index] for index in indices]
            prices.append((row[0], row[1]))
    return prices

parse_csv4('Data/prices.csv',select=['Name', 'price'], types = [str, float], has_headers = False)


def parse_csv5(filename, select = None, types = None, delimiter = ','):
    '''
    CSV파일을 파싱해 레코드의 목록 생성
    '''
    with open(filename) as f:
        rows = csv.reader(f, delimiter = delimiter)
        headers = next(rows)
        
        if select:
            indices = [headers.index(s) for s in select]
            headers = select
        else:
            indices = []    
        
        records = []
        for row in rows:
            if not row:
                continue
            if types:
                row = [func(val) for func, val in zip(types, row)]
                
            if indices:
                row = [row[index] for index in indices]
            records.append(dict(zip(headers, row)))
    return records


parse_csv5('Data/missing.csv', types = [str, int, float])