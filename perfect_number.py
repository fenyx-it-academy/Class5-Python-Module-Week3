#perfect numbers
from functools import reduce # I called the reduce from functools
def perfect_number(n):
    sum = 0  # I defined sum and it is equal to 0
    for x in range(1, n): #I returned the function to the number that user enter it. 
        if n % x == 0: #if the remainder of the division is equal 0
            sum += x  #add x to the sum
    return sum == n  #return it if sum equal to n which is entered by the user.
new_list=list(filter(perfect_number,range(1,1000))) #I defined a new list and it is equal to a new list which is filter by the function
sum=reduce(lambda a,b: a+b,new_list)#sum is equal to a number which is the sum of perfect numbers
print (new_list)
print(sum)