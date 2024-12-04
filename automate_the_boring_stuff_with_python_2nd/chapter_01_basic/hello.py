# This program says hello and asks for my name.
print('Hello, World!')
print('What is your name?') # ask for name
my_name = input()
print(f'It is good to met you, {my_name}')
print('The length of your name is: ')
print(len(my_name))
print('What is your age?') # ask for age
my_age = input()
print(f'You will be {str(int(my_age)+1)} in a year.')