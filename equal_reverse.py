def equal_reserve(x):
    if x[0:]==x[::-1]:
        return True
    else:
        return False
a =list(map(lambda x: equal_reserve(x),['madam','tacocat','utrecht']))
print(a)