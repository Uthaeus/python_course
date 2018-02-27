sale_prices = [
  100,
  83,
  220,
  40,
  100,
  400,
  10,
  1,
  3
]

sale_prices.sort()
print(sale_prices)
# By calling sort you have changed the list

sorted_list = sale_prices.sort()
print(sorted_list) # => returns none

sorted_list = sorted(sale_prices)
print(sorted_list) # prints out the sorted sale_prices list

sorted_list = sorted(sale_prices, reverse=True)
print(sorted_list) # prints out a reverse-ordered sale_prices list
