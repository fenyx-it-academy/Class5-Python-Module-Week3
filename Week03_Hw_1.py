##Write a function that finds perfect numbers between `1` and `1000`.
##Check perfect numbers between `1` and `1000` and find the sum of the perfect numbers using reduce and filter functions. 

def perfect(x): 
    return [y for y in range(1, int(x / 2) + 1) if x % y == 0] 

def perfect_numbers_in_range(a,b): 
    return [x for x in range(a,b+1) if sum(perfect(x)) == x] 

print(perfect_numbers_in_range(1, 10000))
