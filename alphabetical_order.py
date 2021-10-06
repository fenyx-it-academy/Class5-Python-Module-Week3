def alph_order():
    word = input("Please write some words with '-'! : ")
    word = word.split("-")
    word.sort()
    word = "-".join(word)
    return word
print(alph_order())