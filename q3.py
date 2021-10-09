# ## 3-alphabetical_order.py
# Write a function that takes an input of different words with hyphen (-) in between them and then:<br />
# * sorts the words in alphabetical order,
# * adds hyphen icon (-) between them, 
# * gives the output of the sorted words.

# Example:
# ```
# Input  >>> green-red-yellow-black-white
# Output >>> black-green-red-white-yellow 
# ```

def alphabetical_order():
    words=input("Words with -  : ")
    words=words.split('-')
    words.sort()
    words='-'.join(words)
    return words
print(alphabetical_order())