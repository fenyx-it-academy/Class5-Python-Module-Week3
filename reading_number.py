def yazi(a):
    birler=["","bir","iki","uc","dort","bes","alti","yedi","sekiz","dokuz"]
    onlar=["","on","yirmi","otuz","kirk","elli","altmis","yetmis","seksen","doksan"]
    bir=a%10
    on=a//10
    print(onlar[on],birler[bir])

sayi=int(input("iki basamakli bir sayi giriniz"))
yazi(sayi)