# => Dictionary View Objects
# provides a dynamic view.

players = {
  "ss": "Correa",
  "2b": "Altuve",
  "3b": "Bregman",
  "DH": "Gattis",
  "OF": "Springer"
}

print(players.keys()) # => These return dict objects
print(players.values())
print(players.items())

print(list(players.values())[1]) # => Altuve

player_names = list(players.copy().values()) # => Will copy all values into a new list
print(player_names)

teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels" : ["Trout", "Pujols"],
  "yankees" : ["Judge", "Stanton"],
  "red sox" : ["Price", "Betts"]
}


team_groupings = teams.items()

print(len(team_groupings)) # => 4

print(list(team_groupings))

"""
[
  ('astros', ['Altuve', 'Correa', 'Bregman']),
  ('angels', ['Trout', 'Pujols']),
  ('yankees', ['Judge', 'Stanton']),
  ('red sox', ['Price', 'Betts'])
]
"""

print(list(team_groupings)[1]) # => ('angels', ['Trout', 'Pujols'])

print(list(team_groupings)[1][1]) # ['Trout', 'Pujols']

print(list(team_groupings)[1][1][0]) # => Trout








