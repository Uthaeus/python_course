
tags = ['python', 'development', 'tutorials', 'code']

tag_range = tags[1:2]

print(tag_range) # => development

tag_range = tags[1:3]
print(tag_range) # => development, tutorials

tag_range = tags[1:]
print(tag_range) # => development, tutorials, code

tag_range = tags[:3]
print(tag_range) # => python, development, tutorials

tag_range = tags[:-1]
print(tag_range) # => lists all except last item

tag_range = tags[:]
print(tag_range) # => prints entire list

