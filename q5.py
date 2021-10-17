# ## 5-equal_reverse.py
# Write a function that controls the given inputs whether they are equal to their reversed order or not.

# Example:
# ```
# Input  >>> madam, tacocat, utrecht 
# Output >>> True, True, False
# ```
def reserved(x):
    if x==x[::-1]:
        return True
    else:
        return False
print(list(map(lambda x: reserved(x),['madam','tacocat','utrecht'])))