zero_19 = {0:"zero ", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven",
                8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen",
                14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen" };
twinty_100 = {2:"twenty", 3:"thirty", 4:"forty", 5:"fifty", 6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety",}

def change(x=int(input('bir sayi girin:'))):
    y=list(map(int, str(x)))
    if 0<=x<20:
        print(zero_19[x])
    elif 20<=x<100 and x%10!=0:
        y=list(map(int, str(x)))
        print(twinty_100[y[0]],zero_19[y[1]],sep=' ')
    else:
        print(twinty_100[y[0]])
change()