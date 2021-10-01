##3-alphabetical_order.py

def words ():
    x, y, z, w = input("please enter four word:").split("-")
    list=[x, y, z, w]
    list.sort()
    for i in list:
        print(i,end="-")
print(words())