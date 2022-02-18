portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.1),
    ('CAT', 150, 83.44),
    ('IBM', 100, 45.23),
    ('GOOG', 75, 572.45),
    ('AA', 50, 23.15),
]

from collections import Counter
total_shares = Counter()
for name, shares, price in portfolio:
    total_shares[name] += shares
    
total_shares['IBM']

from collections import defaultdict

holdings = defaultdict(list)
for name, shares, price in portfolio:
    holdings[name].append((shares, price))
holdings['IBM']

holdings

from collections import deque

history = deque(maxlen = N)
with open(filename) as f:
    for line in f:
        history.append(line)
        
        
