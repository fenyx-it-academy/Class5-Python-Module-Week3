#reading numbers
def reading_numbers(): # I defined a fuction
    x=int(input("Please a number with two digits: ")) #I wanted to ask from user to enter a number with two digits
    list=["ten","eleven","twalf","thirteen","fourteen","fifteen","sixteen","seventeen","ëighteen","nineteen"] # I defined three lists
    first_digit=["","one","two","three","four","five","six","seven","eight","nine"]
    second_digit=["","","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]
    first=x%10 #I defined first is equal the first digit of the number
    second=x//10 # I defined second is equal to the second digit of the number
    if 10<=x<20: # if the number equal to ten or small than twenty 
        print(list[first]) # I wanted to print to the elememt of the list which is order in the first position
    else:
        print(second_digit[second],first_digit[first])# if it is others the reading of the number equal to second postion of the secondigit list
reading_numbers()                                     #and first position of the firstdigit list