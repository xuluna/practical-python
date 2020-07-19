# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra_payment_start_month = int(input('extra_payment_start_month: '))
extra_payment_end_month = int(input('extra_payment_end_month: '))
extra_payment = int(input('extra_payment: '))

while principal > 0:
    p1 = payment
    month += 1
    if(month >= extra_payment_start_month and month <= extra_payment_end_month):
        p1 = payment+extra_payment
    principal = principal * (1+rate/12) - p1
    total_paid = total_paid + p1
    print(month, total_paid, principal)

print('Total paid', total_paid)
print('Total month', month)
