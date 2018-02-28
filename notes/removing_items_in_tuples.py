
post = ('Python Basics', 'Intro guide to Python', 'Some python content', 'published')

# Removing elements from end
post = post[:-1]
print(post) # => ('Python Basics', 'Intro guide to Python', 'Some python content')

# Remove elements from beginning
post = post[1:]
print(post) # => ('Intro guide to Python', 'Some pyton content', 'published')

# Removing specific element ----> not recommended
# => remember 
# - tuples are immutable
# - lists are mutable
post = list(post) # => changes tuple to a list
  # can now manipulate items
post.remove('published')
post = tuple(post) # => changes the list of post back to a tuple

print(post) # => Now print the tuple post without item that was removed

