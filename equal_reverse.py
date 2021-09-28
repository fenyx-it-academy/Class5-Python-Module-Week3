#equal deverse
def equal_devers(*args): #I defined a function with args
    words=[] #I opened a new empty list
    for i in args: #I wanted to look all elements 
        if i==i[::-1]: #If their reverse is equal to them
            words.append(True) #If it is equal I added True to the words list
        else:
            words.append(False) # If it is not equal I added False to the words list
    return words #I wanted to return words list from the function
print(equal_devers("madam","tacocat","utrecht"))