#find digits
def findDigits(n):
    n=str(n)
    l=len(n)
    count =0
    for i in range(l):
        if int(n[i])==0:
            continue
        elif int(n)%int(n[i])==0:
            count+=1
    return count

#capitalize
def solve(s):
    s=s.split(' ')
    for i in range(len(s)):
        if s[i]=='':
            continue
        s[i]=s[i][0].capitalize()+s[i][1:]
    s=' '.join([str(words) for words in s])
    return s
