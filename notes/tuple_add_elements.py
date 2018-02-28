
post = ('Python Basics', 'Intro guide to python', 'Some python content')

print(id(post)) # => Each object has a unique id in memory

post = post + ('published',) # => the comma indicates that we want this treated as a tuple

# title, sub_heading, content, status = post

# print(title)
# print(sub_heading)
# print(content)
# print(status)

