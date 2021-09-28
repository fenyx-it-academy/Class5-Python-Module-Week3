#unique list
def unique_list(*args): #I defined a function with args
    new_list=[] # I opened a new list
    for i in args: #For every lements in args
        if i not in new_list: #I wanted to search if this element is not in args
            new_list.append(i) #if the element doesn't exist in new list I add with the append properties
    return new_list # I wanted to take this new list from the function
print(unique_list(1,2,3,3,4,4,6,6,4,5,5))