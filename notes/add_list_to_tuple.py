
post = ('Python Basics', 'Intro guide to Python', 'Some python content')

tags = ['python', 'coding', 'tutorial']

post += (tags,) # remember that the comma indicates this is intended to be a tuple
  # => This will add the list tags to the end of the tuple post

print(post) # => ('Python Basics', 'Intro guide to Python', 'Some python content', ['python', 'coding', 'tutorial'])

print(post[-1]) # => ['python', 'coding', 'tutorial']

print(post[-1][1]) # => coding