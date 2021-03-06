# How to use a tuple as a dictionary key

priority_index = {
  (1, 'premier'): [1, 34, 12],
  (1, 'mvp'): [84, 22, 24],
  (2, 'standard'): [93, 81, 3],
}
# This dictionary is using all three types

print(list(priority_index.keys())) # => [(1, 'premier'), (1, 'mvp'), (2, 'standard')]

