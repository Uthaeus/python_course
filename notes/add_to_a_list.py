
tags = ['python', 'development', 'tutorials', 'code']

#Nope
tags[-1] = 'programming'

tags.extend('programming') # => adds each character seperately to the list

tags.extend(['programming']) # => appends 'programming' to the end of the list




new_tags = tags + ['programming'] # => creates new variable containing item appended to the end
