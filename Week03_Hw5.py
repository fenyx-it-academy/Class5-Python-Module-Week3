
# function which return reverse of a string

def return_reserve(x):
    return x == x[::-1]

x = input("check your word reserve or not, please enter your word : ")
y = return_reserve(x)

if y:
    print("Yes")
else:
    print("No")
