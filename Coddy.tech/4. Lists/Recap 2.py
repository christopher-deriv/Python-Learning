def reverse(lst):
    new_list = []
    for numbers in range(len(lst -1, -1, -1)):
        numbers.append(new_list)
    return(new_list)
# Function that accepts a list as arguement
def reverse(lst):
  # Empty list to append the list in the reverse order
  reversed_list = []
  # Used to get the range of numbers needed for the loop from the list given
  n = len(lst)
  # The loop itself with the range(0,n) letting you know how many times to loop and to also include the first number in the list.
  # In this i represents the loop index which starts at 0
  for i in range(0, n):
    # Now you are going to append each number in the list to the new list reversed_list
    reversed_list.append(lst[n - i - 1])
  # Returns the new list
  return reversed_list