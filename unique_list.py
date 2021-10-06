def unique_num():
    x = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
    x_2 = []
    for i in x:
        if i in x_2:
            pass
        else: x_2.append(i)
    return x_2
print(unique_num())