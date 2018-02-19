
name = 'Kristine'
age = 12
product = 'Python eLearning course'
from_account = 'Steve'

greeting = "Hi {0}, you are listed as {1} years old and you have purchased: {2}... From {3}".format(name, age, product, 'Steve')
# Format Method

print(greeting)

greeting = f"Hi {name}, you are listed as {age} years old and you have purchased: {product}... From {from_account}"
#f is short for format

print(greeting)