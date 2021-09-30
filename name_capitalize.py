def name_check():
  nr_list=[n for n in input("Avoiding repeating(split with comma ',')  :").split(' ')]
  name=(''.join(nr_list[0])).capitalize()
  surname=(''.join(nr_list[1])).capitalize()
  print(name,surname)

name_check()