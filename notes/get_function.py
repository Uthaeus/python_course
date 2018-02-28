teams = {
  'astros': ['Altuve', 'Correa', 'Bregman'],
  'angels': ['Trout', 'Pujols'],
  'yankees': ['Judge', 'Stanton'],
  'red sox': ['Price', 'Betts']
}

featured_team = teams['astros']

featured_team = teams.get('mets', 'No featured team') # => provides an alternative if query value does not exist.
# => Considered best proctice in python


