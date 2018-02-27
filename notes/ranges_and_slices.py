tags = [
  'python',
  'development',
  'tutorials',
  'code',
  'programming',
  'computer science'
]

tag_range = tags[1:-1]
print(tag_range) # => ['development', 'tutorials', 'code', 'programming']

tag_range = tags[:-1:2]
print(tag_range) # => ['python', 'tutorials', 'programming']

tag_range = tags[::-1] # => reverses list by index
print(tag_range) # => ['computer science', 'programming', 'code', 'tutorials', 'development', 'python']

tags.sort(reverse=True)
print(tags) # => ['tutorials', 'python', 'programming', 'development', 'computer science', 'code']

sorted_tags = tags.sort(reverse=True)
print(sorted_tags) # => returns none
# sort does not actually return anything

