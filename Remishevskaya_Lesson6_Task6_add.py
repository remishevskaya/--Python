import sys

with open('bakery.csv', 'a', encoding='utf-8') as bakery_sales:
    bakery_sales.write(sys.argv[1] + '\n')
