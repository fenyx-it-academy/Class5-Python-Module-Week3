"""This function takes an input of different words with hyphen (-) in between them and then:
sorts the words in alphabetical order,adds hyphen icon (-) between them,
gives the output of the sorted words."""


def sorter():
  elements=[n for n in input("Enter words which you want to sort(split with hyphen '-')  :").split('-')]
  #inputs will be in elements list,afterwards we use sort() for sorting list
  elements.sort()
  print('-'.join(elements)) #join() method separates with '-' 
sorter()