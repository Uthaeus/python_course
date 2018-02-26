users = ['Kristine', 'Tiffany', 'Jordan', 'Leann']

print(users)

users.remove('Jordan')

print(users) # => ['Kristine', 'Tiffany', 'Leann']

popped_user = users.pop()

print(popped_user) # => Leann
print(users) # => ['Kristine', 'Tiffany']

del users[0]
print(users) # => ['Tiffany']

.remove() # - removes any value specified in your argument

.pop()

del # - when you know the index of the item you want removed