from functools import reduce
def fun(a):
    global list1
    list1=[]
    for i in range(1,a):
        toplama= 0
        for j in range(1,i):
            if i%j==0:
                toplama+=j
        if toplama == i:
            list1.append(toplama)
    return list1
print(fun(10000))
print(reduce(lambda x,y:x+y,list1))
