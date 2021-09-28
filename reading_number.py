first_digits=['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
second_digits=['','','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
specials=['Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
def read_num():
    a=input("enter a number with two digits: ")
    if a.isdigit()==False:
        result = a
    elif int(a)<10 or int(a)>99:
        result= a
    elif 20>int(a)>=10:
        result='{}--------->{}'.format(a,specials[int(a[1])])
        
    else:
        result='{}--------->{} {}'.format(a,second_digits[int(a[0])],first_digits[int(a[1])])
    return result
print(read_num())