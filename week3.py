## 1-perfect_number.py

def perfect ():
    perfectlist=[]
    for i in range (1,1000):        
        sum=0
        for j in range (1,i):
            if i%j==0:
                sum +=j  # sum all divisor
                if sum == i: # if sum of divisor equal to number it means number is perfect
                    perfectlist.append(i)
    return print(perfectlist)  
print(perfect())                


## 2-reading_number.py

def read ():
    number = int(input("please enter a number:"))
    ones=["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tens=["", "teen", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    one = number%10      # we find ones digit
    ten = number//10     #we find tens digit
    if ten == 1 and one == 1:    # for 11
        return print("eleven")
    elif ten ==1 and one == 2:  # for 12
        return print("twelve")
    elif ten ==1 and one == 3:  # for 13
        return print("thirteen")
    elif ten==1 and one != 1 and one !=2 and one != 3: #  without 10+(1, 2, 3) ; 14,15...
        return print(ones[one], "teen")
    else:
        return print(tens[ten], ones[one]) # write without {} + teen. it is 20,21,22,... 
print(read())

## 3-alphabetical_order.py

def words ():
    x, y, z, w = input("please enter four word:").split("-")
    list=[x, y, z, w]
    list.sort()
    for i in list:
        print(i,end="-")
print(words())



## 4-unique_list.py
# Write a function that filters all the unique(unrepeated) elements of a given list.
def unique_list(test_list):
    res = []
    [res.append(x) for x in test_list if x not in res]
    return res
print (unique_list([1, 1, 1, 2, 2, 3, 3]))


## 5-equal_reverse.py
def isPalindrome(s):
    return s == s[::-1]
s = input("enter a word :")
ans = isPalindrome(s)
if ans:
    print("true")
else:
    print("false")
 

