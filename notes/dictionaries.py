
# Key value data store

players = {
  "ss": "Correa",
  "2b": "Altuve",
  "3b": "Bregman",
  "DH": "Gattis",
  "OF": "Springer"
}

second_base = players['2b']

print(second_base) # => Altuve

designated_hitter = players['DH'] # => Is case-sensitive

print(designated_hitter) # => Gattis
