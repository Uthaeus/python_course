tags = [
  'python',
  'development',
  'tutorials',
  'code',
  'programming'
]

print(tags[:2]) # => ['python', 'development']

slice_obj = slice(2)
print(slice_obj) # => slice(None, 2, None)

print(tags[slice_obj]) # => ['python', 'development']

# slice accepts three arguments:
# start, stop, step

slice_obj = slice(1, 4, 2)
print(tags[slice_obj]) # => ['development', 'code']

print(slice_obj.start) # => returns index of start

print(slice_obj.stop) # => index of stop

print(slice_obj.step)