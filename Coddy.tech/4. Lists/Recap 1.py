# Easy part, need a function that takes a list as an input (in this case lst is our variable name which the actual list will be pssed into)
def prod(lst):
    # need to initize total at 1 because you will be doing multilplication and doing 0 will just have it all equal 0
    total = 1
    # Time for the loop, iterate over each number in the list
    for numbers in lst:
        # Multiply the current number with the total (in this case it's the current number of that loop)
        total *= numbers
    # returns the sum
    return total