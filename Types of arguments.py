def user(name, age, sex):
    print(name, end=" ")
    print(age, end=" ")
    print(sex)
"""
# Positional Arguments

name = 'abc'
age = 20
user(name, age)
print()
user(age, name)
"""

# keyword arguments
user(age=20, sex='M', name='abc')
