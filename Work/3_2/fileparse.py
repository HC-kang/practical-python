import csv

def parse_csv(filename, select = None, types = None, has_headers = False, delimitier = ','):
    '''
    CSV 파일을 파싱해 레코드 목록 생성
    '''
    with open(filename, 'rt') as f:
        rows = csv.reader(f, delimiter = delimitier)
        
        records = []
        indices = []
        if has_headers:
            headers = next(rows)
            if select:
                indices = [headers.index(colname) for colname in select]
                headers = select
        
        for row in rows:
            if not row:
                continue
            if indices:
                row = [row[index] for index in indices]
            if types:
                row = [func(val) for func, val in zip(types, row)]
            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = row
            records.append(record)
            
    return records
