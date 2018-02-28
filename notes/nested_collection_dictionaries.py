
teams = {
  "astros": ["Altuve", "Correa", "Bregman"],
  "angels": ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"]
}

print(teams['astros']) # => ['Altuve', 'Correa', 'Bregman']

print(teams['astros'][2]) # => Bregman

print(teams['astros'][:2]) # => ['Altuve', 'Correa']

print(teams['angels'])

print(teams['yankees'])

astros = teams['astros']
print(astros)