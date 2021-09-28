def alphabetical_order():
    words=input("enter words with -:")
    words = words.split('-')
    words.sort()
    words ='-'.join(words)
    return words
print(alphabetical_order())