name = 'IBM'
shares = 100
price = 91.1

f'{name:>10s} {shares:>10d} {price:>10.2f}'

print(f'{name:>10s} {shares:>10d} {price:>10.2f}')


s = {
    'name': 'IBM',
    'shares': 100,
    'price': 91.1,
}

'{name:>10s} {shares:>10d} {price:>10.2f}'.format_map(s)

value = 42863.1

print(value)

print(f'{value: <16.4f}')