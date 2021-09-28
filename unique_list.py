def unique_list(list):
    new_list=[]
    for i in list:
        if i in new_list:
            continue
        else:
            new_list.append(i)
    return new_list
unique_list([1,2,3,3,3,3,4,5,5])