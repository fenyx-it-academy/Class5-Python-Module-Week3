# ## 1-perfect_number.py
# Perfect number: Perfect number is a positive integer that is equal to the sum of its proper divisors.

# The smallest perfect number is `6`, which is the sum of `1`, `2`, and `3`. 

# Some other perfect numbers are `28(1+2+4+7+14=28)`, `496` and `8128`.

# Write a function that finds perfect numbers between `1` and `1000`.
# Check perfect numbers between `1` and `1000` and find the sum of the perfect numbers using reduce and filter functions. <br />

def perfect_number(x):
    summ=0
    for i in range(1,x):
        if x%i==0:
            summ+=i
    if summ==x:
        return True
from functools import reduce
print(reduce(lambda a,b:a+b,(list(filter(lambda x: perfect_number(x),range(1,1000))))))