# Create a function that will merge two lists together. You need to include 2 arguements for the fucntion to be able to accept
def merge(lst1, lst2):
    # Now you need to loop through each item in the second list
    for item in lst2:
        # Then it needs to be appended to the first list. If you try to append the whole list to the first one it will nest it instead of actually adding the individual item
        lst1.append(item)
    # Then sort the list
    lst1.sort()
    #print the list once merged and sorted
    print(lst1)