import sys

key = sys.argv[1:]
if key:
    with open('bakery.csv', encoding='utf-8') as f:
        sales = [line.strip() for line in f.readlines()]
    if len(key) == 1:
        sale = sales[int(key[0]):]
        print('\n'.join(sale))
    elif len(key) == 2:
        sale = sales[int(key[0]):int(key[1]) + 1]
        print('\n'.join(sale))

with open('bakery.csv', encoding='utf-8') as f:
    sales = [line.strip() for line in f.readlines()]
    print(sales[1:])
