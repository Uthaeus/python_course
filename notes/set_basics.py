
tags = {
  'python',
  'coding',
  'tutorials'
}
# Items in a set must be unique

print(tags) # => {'tutorials', 'python', 'coding'}

print(tags[0]) # => Will give a TypeError

query_one = 'python' in tags
print(query_one) # => True

query_two = 'ruby' in tags
print(query_two) # => False



