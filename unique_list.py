## 4-unique_list.py
# Write a function that filters all the unique(unrepeated) elements of a given list.
def unique_list(test_list):
    res = []
    [res.append(x) for x in test_list if x not in res]
    return res
print (unique_list([1, 1, 1, 2, 2, 3, 3]))
