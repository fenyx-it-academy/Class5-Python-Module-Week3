def alphabetical_order():
        metin=input("lütfen sıralanıcak kelimeleri arada boşluk bırakarak giriniz:")
        kelimeler=[i for i in metin.split(' ')]
        kelimeler.sort()
        return print(*kelimeler, sep='-')

alphabetical_order()