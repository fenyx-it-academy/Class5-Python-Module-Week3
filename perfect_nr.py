
"""Perfect number: Perfect number is a positive integer that is equal to the sum of its proper divisors.
The smallest perfect number is 6, which is the sum of 1, 2, and 3.
Some other perfect numbers are 28(1+2+4+7+14=28).
This function finds perfect numbers between 1 and 1000.
And find the sum of these perfect numbers using reduce and filter functions additionally."""


from functools import reduce
def perfect_nr(n):
    sum = 0 
    for x in range(1, n):
        if n % x == 0:  #checking positive divisors whether remainder is zero
            sum += x    #adding every each divisors  
    return sum == n     #If given number is a perfect ,then this will be True
                        #filter function gathers perfect numbers(which return True)
print("Perfect numbers lower than 1000  :",list(filter(perfect_nr,range(2,1001))))

print("Sum of perfect numbers lower than 1000  :",reduce(lambda x,y: x+y,list(filter(perfect_nr,range(2,1001)))))
# use  reduce function to adding all perfect numbers lower than 1000.