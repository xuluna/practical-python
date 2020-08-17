# report.py
#
# Exercise 2.4

# pcost.py
#
# Exercise 1.27

import csv
from pprint import pprint


def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        headers = next(rows)
        for line in rows:
            holding = {}
            try:
                holding['name'] = line[0]
                holding['shares'] = int(line[1])
                holding['price'] = float(line[2])
                portfolio.append(holding)
            except ValueError:
                print("invalid row: ", line)

    return portfolio


def read_prices(filename):
    prices = {}
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        for row in rows:
            if len(row) < 2:
                continue
            prices[row[0]] = float(row[1])
    return prices


def make_report(portfolio, prices):
    report = []
    for f in portfolio:
        name = f['name']
        share = f['shares']
        price = prices[name]
        change = price-f['price']
        report.append((name, share, price, change))
    return report


prices = read_prices('Data/prices.csv')
portfolio = read_portfolio('Data/portfolio.csv')
report = make_report(portfolio, prices)
headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)
print(('-'*10+' ')*4)
for name, share, price, change in report:
    price = "${:.2f}".format(price)
    print(f'{name:>10s} {share:>10d} {price:>10s} {change:>10.2f}')
