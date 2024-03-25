# Write a program that gets one input, a number. The input number indicates how many times to execute the below function. 
# Create a function that calculates the sum of all of the numbers between 1 and 10000 (including) and prints it, name the function however you like.

# When defining a function you essentially have to treat it as it's own separate code block including all the variables
# you would normally include in a longer piece of code in that initial function.
def sum_number():
    base = 0
    for sumthis in range(1,10001):
        base += sumthis
    #You want to print base as it is the one that's having the initial number (0) and is the one that will have
    # the range of numbers added to it when the loop initiates.
    # sumthis will just tell you the final number in the range(1,10001) which is 10000
    print(base)
    
dynamic_input = int(input())

for recursive in range(dynamic_input):
    sum_number()
