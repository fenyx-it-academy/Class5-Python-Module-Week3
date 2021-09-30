#Write a function that outputs the transcription of an input number with two digits.


def nr_reader():
   nr_list = list(input("Enter a double digits number : "))#we convert to list for indexing given number
  
   x=int(nr_list[0])    #indexed units converted to integer,we will use as keys to call assigned values in dictionary
   y=int(nr_list[1])    
   #we need dictionaries to asiggn indexed keys to their string values
   onluk={1:"on",2:"Yirmi",3:"Otuz",4:"Kirk",5:"Elli",6:"Altmis",7:"Yetmis",8:"Seksen",9:"Doksan"}
   birlik={0:"",1:"bir",2:"iki",3:"uc",4:"dort",5:"bes",6:"alti",7:"yedi",8:"sekiz",9:"dokuz"}
   #We use Turkish to make it clear :D
   sayiyazi=onluk[x]+birlik[y] #calling values for each digit to print,adjacent values due to sum str
   return(sayiyazi) 
print(nr_reader())