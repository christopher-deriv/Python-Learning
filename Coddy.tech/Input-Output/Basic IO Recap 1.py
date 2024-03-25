# Write a program that gets an input from the user, his age.

# The program will output (print), the number of missing years till 120 (In a specific format, shown below)

# For example, for input 25, the expected output is "95 years till 120".

age = int(input())

if age<120:
   age = 120 - age

print(f"{age} years till 120") 