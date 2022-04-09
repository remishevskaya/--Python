prices = [32.02, 46.51, 23, 23.12, 21.10, 45, 56.34, 22.1, 56, 98.23]
for price in prices:
    prices[prices.index(price)] = f'{int(price)} руб. {str(int((price - int(price)) * 100)).zfill(2)} коп.'
print(', '.join(prices))
print(id(prices))
prices.sort()
print(', '.join(prices))
print(id(prices))
prices_sort = sorted(prices, reverse=True)
print(', '.join(prices_sort))
print(id(prices_sort))
print(', '.join(prices_sort[:5]))
