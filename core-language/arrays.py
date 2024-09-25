#arrays
#apple stock prices AAPPL
AAPPL_stock_prices = [298,305,320,301,290]
                   #day 1   2   3   4  5
                #index  0   1   2   3  4
AAPPL_stock_prices[1]

print("price on day 3")
print(AAPPL_stock_prices[2], "USD") #O(1)

print("price on day 5")
for index in range(len(AAPPL_stock_prices)):  #O(n)
    if index == 4:
        print(AAPPL_stock_prices[index])

print("on which day price was 305")      #O(n)
for index in range(len(AAPPL_stock_prices)):
   if AAPPL_stock_prices[index] == 305:
       print(index + 1)

print("All the prices")
for price in AAPPL_stock_prices:
    print(price, end=" - ")

print("insert price 500 in day 2") #O(n)
AAPPL_stock_prices.insert(1,500)
print(AAPPL_stock_prices)

print("delet prices of last day")
AAPPL_stock_prices.remove(290)
print(AAPPL_stock_prices)
print(len(AAPPL_stock_prices)-1)

print("="*7)
stock_prices = [price for price in range(1,40,10)]
print(stock_prices)
stock_names = ['APL','GOOG','AMZN','AIRBUS']

stock_data = []
for index in range(len(stock_names)):
    data = dict()
    data["ticker"] = stock_names[index]
    data["price"] = stock_prices[index]
    stock_data.append(data)
print(stock_data)