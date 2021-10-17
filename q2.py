# ## 2-reading_number.py
# Write a function that outputs the transcription of an input number with two digits.

# Example:
# ```
# 28---------------->Twenty Eight

reading1=['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
reading2=['Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
reading3=['Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
def reading_numb():
    x=input("A number only with two digits: ")
    if x.isdigit()==False:
        read= x
    elif int(x)<10 or int(x)>99:
        read= x
    elif 20>int(x)>=10:
        read='{}--------->{}'.format(x,reading3[int(x[1])])
        
    else:
        read='{}--------->{} {}'.format(x,reading2[int(x[0])-2],reading1[int(x[1])])
    return read
print(reading_numb())
