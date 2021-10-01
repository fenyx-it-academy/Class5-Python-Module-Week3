##2-reading_number.py

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