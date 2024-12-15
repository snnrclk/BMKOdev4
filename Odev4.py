#1- Kendisine gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız.

def gönderilen(kelime, tekrar_sayisi):
    for i in range(tekrar_sayisi):
        print(kelime)

gönderilen("Hoş geldiniz", 2)

#2- Dikdörtgenin alan ve çevresini hesaplayan fonksiyonu yazınız.

def dikdortgen(a, b):
    alan=a*b
    cevre=2*(a+b)
    return alan, cevre

print(dikdortgen(30, 2))

#3- Yazı tura uygulamasını fonksiyon kullanarak yapınız. (Random modülü)

import random
def yazı_tura():
    sonuc=["yazı","tura"]
    secim=random.choice(sonuc)
    return secim
print(yazı_tura())

#4- Kendisine gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyonu yazınız.

def asal_sayilar(ilk, son):
    asal_sayilar=[]

    for sayi in range(ilk, son+1):
        if sayi>1:
            for x in range(2, int(sayi**0.5)+1):
                if (sayi % x == 0):
                    break
            else:
                asal_sayilar.append(sayi)
    return asal_sayilar           

ilk=int(input('ilk: '))
son=int(input('son: '))
print(f"{ilk} ve {son} arasındaki asal sayılar: {asal_sayilar(ilk, son)}")

#5- Kendisine gönderilen bir sayının tam bölemlerini bir liste şeklinde döndüren fonksiyonu yazınız. 

def tam_bolenler(sayi):
    tam_bolenler=[]

    for x in range(1, int(sayi)+1):
        if sayi % x == 0:
            tam_bolenler.append(x)

    return tam_bolenler

sayi=int(input('sayi: '))

print(f"{sayi} sayısını tam bölenleri: {tam_bolenler(sayi)}")




