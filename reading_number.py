number = int (input("Please enter a two digit number: "))
def read_num(x):
    ones = ["", "one","two","tree","four","five","six","seven","eight","nine"]
    tens = ["", "ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]
    one = x%10
    ten = x//10 
    print(tens[ten], ones[one])
read_num(number)