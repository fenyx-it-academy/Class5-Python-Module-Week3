## 1-perfect_number.py
from functools import reduce
def perfect_number(x):
    sum = 0
    for i in range(1,x):
        if x%i == 0:
            sum+=i
    if sum ==x:
        return True
perfect_list=list(filter(lambda x: perfect_number(x),range(1,1000)))
print(perfect_list)
final_result =reduce(lambda a,b:a+b,list(filter(lambda x: perfect_number(x),range(1,1000))))
print(final_result)