# Define a function that accepts 3 arguments in this case it's a list, the index of the list, and a new element to replace the index you selected
def change_element(lst, index, new_element):
    # now overwrite the selected item in the list with the new elemtn
    lst[index] = new_element
    # print out the new list, needs to be in this location as if you move it back it will print the previous list and not "learn" the new list
    print(lst)