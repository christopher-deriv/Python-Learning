# here we only need to define a function but not actually run it

# n will represent an input gathered from another source
def sigma(n):
    # total sits as a variable to store the summation as it loops through
    total = 0
    # The loop iterates through the numbers from 1 to n (inclusive)
    for numbers in range(1,n+1):
        # Each number will then be added into the variable total until it goes through the range
        total += numbers
    # it will then return the total so it can update the variable
    return(total)
