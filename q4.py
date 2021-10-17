# ## 4-unique_list.py
# Write a function that filters all the unique(unrepeated) elements of a given list.

# Example:
# ```
# Function call: unique_list([1,2,3,3,3,3,4,5,5])
# Output       : [1, 2, 3, 4, 5]
# ```

def unique_list(list):
    new_list=[]
    for i in list:
        if i in new_list:
            continue
        else:
            new_list.append(i)
    return new_list
unique_list([1,2,3,3,3,3,4,5,5])