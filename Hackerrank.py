### Find Digits:

n = 1012
def findDigits(n):
    n=str(n)
    len_n=len(n)
    sum = 0
    for i in range(len_n):
        if int(n[i]) == 0:
            pass
        elif int(n)%int(n[i]) == 0:
            sum+=1
    return sum
print(findDigits(n))


### Capitalize:

n = "ı guess that ıt will work ;)"
def capitalize(n):
    n_title = n.title()
    return n_title
print(capitalize(n))