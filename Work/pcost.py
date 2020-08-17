# pcost.py
#
# Exercise 1.27

import gzip
import csv
import sys


def portfolio_cost(filename):
    cost = 0

    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        headers = next(rows)
        for line in rows:
            try:
                shares = int(line[1])
                price = float(line[2])
                cost += shares*price
            except ValueError:
                print("invalid row: ", line)

    return cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost', cost)
