def reverse_ctrl():
    x = map(str, input().split(","))
    reverse_list=[]
    for i in x:
        if i == i[::-1]:
            reverse_list.append('True')
        else:
            reverse_list.append('false')
    return reverse_list
print(",".join(i for i in reverse_ctrl()))