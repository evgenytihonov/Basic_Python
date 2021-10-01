import sys

key = sys.argv[1:]
if key:
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        f.write(f'\n{key[0]}')