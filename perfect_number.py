##1-perfect_number.py

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