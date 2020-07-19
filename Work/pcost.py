# pcost.py
#
# Exercise 1.27

import gzip
cost = 0


with gzip.open('Data/portfolio.csv.gz', 'rt') as file:
    next(file)
    for line in file:
        shares = int(line.split(',')[1])
        price = float(line.split(',')[2])
        cost += shares*price

print('Total cost', cost)
