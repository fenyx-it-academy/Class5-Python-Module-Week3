##5-equal_reverse.py

def isPalindrome(s):
    return s == s[::-1]
s = input("enter a word :")
ans = isPalindrome(s)
if ans:
    print("true")
else:
    print("false")