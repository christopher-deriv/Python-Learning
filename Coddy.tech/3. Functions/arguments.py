# Write a program that gets two inputs, numbers. The input numbers are the arguments of the below function. 
# Create a function that gets two arguments, calculates the product of them and prints it, name the function however you like.

#Again think of it as if you needed to create the code for your script to do something all of it must be defined in the function first (input, calculation/what you want it to do, and it must update itself with (this is why you need return product))
def multiply():
    number1 = int(input())
    number2 = int(input())    
    product = number1 * number2
    return product

total = multiply()
print(total)