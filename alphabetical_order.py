#alphabetical order 
def alphabetical():
    words=input("Enter some words and add hyphen between them: ") #I wanted to ask from user to enter some words with hyphen
    source=[n for n in words.split('-')]  #I defined a source list and it is equal all of the words with hyphen
    source.sort() #I sorted the list with an alphabetical order
    print('-'.join(source))# I wrote to the screen a print which added hyphen

alphabetical()