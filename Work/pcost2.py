import csv

def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        tot_cost = 0
        for row in rows:
            tot_cost += int(row[1]) * float(row[2])
    print('Total Cost:', tot_cost)


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        portfolio_cost(sys.argv[1])