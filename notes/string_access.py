# The quick brown fox jumped
# T => 0
# h => 1
# e => 2
# ' ' => 3

starter_sentence = 'The quick brown fox jumped'
print(starter_sentence[0])
# => 'T'
# => Strings are immutable in Python

# Ranges

starter_sentence = 'The quick brown fox jumped'
first_word = starter_sentence[0:3]
new_sentence = first_word
print(new_sentence)
# => The

starter_sentence = 'The quick brown fox jumped'

new_sentence = 'Thy' + starter_sentence[3:]
print(new_sentence)
# => Thy quick brown fox jumped

