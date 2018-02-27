import math

"""
Tools:
-math library
-sorted function
-list slicing
-computations
"""

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

sorted_list = sorted(sale_prices)
num_of_sales = len(sorted_list)

first_sale_items = sorted_list[:math.floor(num_of_sales/2)]
last_sale_items = sorted_list[-(math.floor(num_of_sales/2)):]
median = sorted_list[math.floor(num_of_sales/2):(math.floor(num_of_sales/2) + 1)]

half_slice = math.floor(num_of_sales/2)

median = sorted_list[half_slice:(half_slice + 1)]


