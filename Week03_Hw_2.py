
#write a function that outputs the transcription of an input number with two digits.


def transcription(n):

    units_digits=['','one','two','tree','four','five','six','seven','eight','nine']
    tens_digits=['','','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety']
    units=n%10
    tens=n//10
    print(tens_digits[tens],units_digits[units])

number=int(input("enter number with two digits : "))
transcription(number)

