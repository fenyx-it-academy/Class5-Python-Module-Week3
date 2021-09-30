
## 4-unique_list.py
##Write a function that filters all the unique(unrepeated) elements of a given list.



def unique(list):

    unique_list = []

    for x in list:
        
        if x not in unique_list:
            unique_list.append(x)
    
    for x in unique_list:
        print(x)

list = [1,2,3,3,3,3,4,5,5]

print(unique(list))


