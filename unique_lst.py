#We prevent user from repeating.Repeated elements in given list will be expelled.


def unique_list():
   elements=[n for n in input("Avoiding repeating(split with comma ',')  :").split(',')]
   # Initially we ask for enter list where elements splitted by coma
   elements=set(elements) #Due to set property ,repeated element will be expelled.
   elements=list(elements) #We revert set to list for print as a list.
   print(elements)
unique_list()
