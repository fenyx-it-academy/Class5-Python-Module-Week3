#1 
def fun_uniq(x):
    print(set(x))
unique_list= [1,2,3,3,3,3,4,5,5]
fun_uniq(unique_list)

#2
def uniq(n):
    unique= []
    for i in n:
        if i not in unique:
            unique.append(i)
    return unique
print(uniq([1,2,3,3,3,3,4,5,5]))