import random
from asyncio.windows_events import NULL
import os
import time 

ysr=NULL
kullanici=NULL
toplam = 0
i=0
kullanicibakiye=10000

def zarGorsellestir(zar):
    zar1 = """------------------
|                |
|                |
|       1        |
|                |
|                |
------------------"""

    zar2 = """------------------
|                |
|  2             |
|                |
|            2   |
|                |
------------------"""

    zar3 = """------------------
| 3              |
|                |
|       3        |
|                |
|             3  |
------------------"""

    zar4 = """------------------
|  4          4  |
|                |
|                |
|                |
|  4          4  |
------------------"""

    zar5 = """------------------
|  5          5  |
|                |
|       5        |
|                |
|  5          5  |
------------------"""

    zar6 = """------------------
| 6            6 |
|                |
| 6            6 |
|                |
| 6            6 |
------------------"""

    if zar == 1:
        print(zar1)
    elif zar == 2:
        print(zar2)
    elif zar == 3:
        print(zar3)
    elif zar == 4:
        print(zar4)
    elif zar == 5:
        print(zar5)
    else :
        print(zar6)

def calistir():
        print(".", end=" " )
        time.sleep(0.5)
        print(".", end=" " )
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
while(True):
    while(True):
        print(kullanicibakiye, "Tl paranız var. İstediğiniz gibi harcamanız dileğiyle")
        masasecimi=['100 Tl lik masa için','500 Tl lik masa için ','1000 Tl lik masa için','2500 Tl lik masa için', \
            '5.000 Tl lik masa için ','10.000 Tl lik masa için','25.000 Tl lik masa için ','50.000 Tl lik masa için ','100.000Tl lik masa için']
        b = 0
        for j in masasecimi:
            b = b + 1
            print( b,".",j)
            time.sleep(0.5)
        masasecimi=input("Lütfen oynamak istedğiniz masa numarasını giriniz. : ")
        
        if(masasecimi=="1"):
            bahis=100
        elif(masasecimi=="2"):
            bahis=500
        elif(masasecimi=="3"):
            bahis=1000
        elif(masasecimi=="4"):
            bahis=2500
        elif(masasecimi=="5"):
            bahis=5000
        elif(masasecimi=="6"):
            bahis=10000
        elif(masasecimi=="7"):
            bahis=25000
        elif(masasecimi=="8"):
            bahis=50000
        elif(masasecimi=="9"):
            bahis=100000
        os.system('CLS')
        if (kullanicibakiye<bahis):
            print("\nBakiyenizden yüksek masa seçimi yaptınız. Tekrar deneyiniz. \n")
        else:
            break
    kullanicibakiye=kullanicibakiye-bahis
    
   
    while(True):
        ysr  = random.randint(1,6)
        print("Sıra ysr'nin, ysr'ye gelen zar:" )
        time.sleep(0.5)
        zarGorsellestir(ysr)
        time.sleep(0.5)
        kullanici=input("Sıra sizde, zar atmak için enter tuşuna basın:")
        if (kullanici==""):
            kullanici = random.randint(1,6)
            print('size gelen zar:' )
            time.sleep(0.5)
            zarGorsellestir(kullanici)
            time.sleep(0.5)
        if(ysr > kullanici):
            print("ysr kazandı")
            toplam = toplam + 1
    
        elif(kullanici > ysr):
            print("siz kazandınız.")
            toplam = toplam - 1

        elif(kullanici==ysr):
            i=i-1
            print("Beraberlik dolayısıyla tekrar zar atılmalı.")
        i=i+14

        if(i==3):
            i=0
            break
        print("Diğer tura geçtiniz.")
        calistir()


    os.system('CLS')
    print("Oyun sonu.")

    if (toplam<0):
        print("Siz kazandınız.")
        kullanicibakiye = kullanicibakiye + bahis*2
        print(kullanicibakiye)

    elif(toplam>0):
        print("ysr kazandı.")
        print("Kalan bakiyeniz: ", kullanicibakiye)


    a=(input("oyundan çıkmak için 0 a bas. Tekrar oynamak için enter a basınız."))
    if (a=='0'):
        break 

"""
@yasirtavlasoglu
"""