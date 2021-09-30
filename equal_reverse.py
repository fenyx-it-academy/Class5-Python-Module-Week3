
# We check given list elements wheter palindrome(equal its reversed order)
   
   

def palindrome_chck():
   # Initially we ask for enter list where elements splitted by coma
   list=[n for n in input("Check list elements whether palindrome(split with comma ',')  :").split(',')]
   control=[]     #We check every each words individually by "For Loop",afterwards add results in this list.
   for i in list:
      if i==i[::-1]:    
        control.append(True)  
      else:
        control.append(False)        
   print(control)  #Results will be shown here as same order with given list due to list.append
palindrome_chck()



