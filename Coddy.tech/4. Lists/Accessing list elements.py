# This one was pretty straight forward but when reading the prompt I thought we still had to account for user input or calling upon the function later on. 
# It just wants you to create the function nothing else

# Here you define the new function but also tell it what to accept as an arguement when calling it
def values(my_list):
  # Loop to iterate over each iteam in the list across the range which is the length of the list given
  for i in range(len(my_list)):
    # this just prints out each item individually as it goes through the loop
    print(my_list[i])

