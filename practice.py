items = ['towel','pb','tp','gum','shirt']
prices = [3.4,5,3,6,8]
#print statement for each item

for index in range(len(items)):
    print(f'I bought {items[index]} for ${prices[index]}')

sum = 0

for price in prices:
    sum += price
print(f'I paid ${sum} for everything!')

maxPrice = max(prices)

removePrice = prices.index()
del items