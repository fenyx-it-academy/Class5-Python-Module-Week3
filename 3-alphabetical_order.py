def sirala():
    list1 = map(str, input().split('-'))
    print("-".join(i for i in sorted(list1)))
sirala()