# Allows us to merge multiple lists into tuples

postitions = ['2b', '3b', 'ss', 'dh']
players = ['Altuve', 'Bregman', 'Correa', 'Gattis']

scoreboard = zip(postitions, players)

print(list(scoreboard)) # => [('2b', 'Altuve'), ('3b', 'Bregman'), ('ss', 'Correa'), ('dh', 'Gattis')] 

