# ## Bonus Question 1
# [HACKERRANK: FIND DIGITS](https://www.hackerrank.com/challenges/find-digits/problem)

def findDigits(n):
    n=str(n)
    l=len(n)
    summ=0
    for i in range(l):
        if int(n[i])==0:
            continue
        elif int(n)%int(n[i])==0:
            summ+=1
    return summ

# ## Bonus Question 2
# [HACKERRANK: CAPITALIZE](https://www.hackerrank.com/challenges/capitalize/problem)

def solve(s):
    s=s.split(' ')
    for i in range(len(s)):
        if s[i]=='':
            continue
        s[i]=s[i][0].capitalize()+s[i][1:]
    s=' '.join([str(item) for item in s])
    return s
solve('chris alan')