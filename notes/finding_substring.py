
sentence = 'The quick brown fox jumped over the lazy dog.'

query = sentence.find('quick')
print(query)
# => 4 -- it begins at the fourth index of the string

query = sentence.index('quick')
# index will throw an error if it does not find a match
# find will return a -1

query = 'fox' in sentence
print(query)
# will return true or false

if 'fox' in sentence:
  ...