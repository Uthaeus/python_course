
teams = [
  {
    'astros' : {
      '2b' : "Altuve",
      'ss' : "Correa",
      '3b' : "Bregman"
    }
  },
  {
    'angels' : {
      'OF' : "Trout",
      'DH' : "Pujols"
    }
  }
]

print(teams)

print(teams[0]) # => returns the astros dictionary

angels = teams[1].get('angels', 'Team not found')
print(angels) # => returns angels dictionary

print(angels.values()) # => returns dictionary view

print(list(angels.values())[1]) # => Pujols