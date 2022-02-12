import math
import random

durum = True
while durum:
    def menu():
        print("""                                                                  
        ,--.   ,--.          ,--.                             ,--.  ,--.,--.     
        |   `.'   | ,--,--.,-'  '-. ,---. ,--,--,--. ,--,--.,-'  '-.`--'|  |,-.  
        |  |'.'|  |' ,-.  |'-.  .-'| .-. :|        |' ,-.  |'-.  .-',--.|     /  
        |  |   |  |\ '-'  |  |  |  \   --.|  |  |  |\ '-'  |  |  |  |  ||  \  \  
        `--'   `--' `--`--'  `--'   `----'`--`--`--' `--`--'  `--'  `--'`--'`--' 
        
        Matematik Hesaplama'ya Hoş Geldiniz Lütfen İşlem Seçiniz: """)

    def islemler():
        print("""
        1- Alan Hesaplama
        2- Çevre Hesaplama
        3- OBEB Hesaplama
        4- İnç Hesaplama
        5- Mil Hesaplama
        6- Rastgele Sayı Hesaplama
        7- Üslü Sayı Hesaplama
        
        8- Çıkış
        """)

    def alanhesapla():
        print("""
        1- Dikdörtgen (veya Kare) alanı hesapla
        2- Üçgen alanı hesapla
        3- Daire alanı hesapla
        """)
        alansecim = int(input("İşleminizi Giriniz(1-3): "))
        while alansecim < 1 or alansecim > 3:
            alansecim = int(input("İşleminizi 1-3 arasında seçiniz: "))
        if alansecim == 1:
            taban = float(input("Taban (a) cm (Örn. 70.5):"))
            yukseklik = float(input("Yükseklik (h) cm (Örn. 54.45):"))
            sonuc = taban * yukseklik
            print("Sonuç = ",sonuc)
        elif alansecim == 2:
            taban = float(input("Taban (a) cm (Örn. 70.5):"))
            yukseklik = float(input("Yükseklik (h) cm (Örn. 54.45):"))
            sonuc = (taban * yukseklik) / 2
            print("Sonuç = ", sonuc)
        elif alansecim == 3:
            yaricap = float(input("Yarıçap (r) cm (Örn. 34.5):"))
            sonuc = math.pi * (yaricap * yaricap)
            print("Sonuç = ", sonuc)

    def cevrehesapla():
        print("""
        1- Dikdörtgen çevresi hesapla
        2- Eşkenar Üçgen çevresi hesapla
        3- Daire çevresi hesapla
        """)
        cevresecim = int(input("İşleminizi Giriniz(1-3): "))
        while cevresecim < 1 or cevresecim > 3:
            cevresecim = int(input("İşleminizi 1-3 arasında seçiniz: "))

        if cevresecim == 1:
            taban = float(input("Taban (a) cm (Örn. 70.5):"))
            yukseklik = float(input("Yükseklik (h) cm (Örn. 54.45):"))
            sonuc = (taban + yukseklik) * 2
            print("Sonuç = ", sonuc)

        elif cevresecim == 2:
            kenar = float(input("Bir Kenarın Uzunluğu (a) cm (Örn. 124,58):"))
            sonuc = kenar * 3
            print("Sonuç = ", sonuc)

        elif cevresecim == 3:
            yaricap = float(input("Yarıçap (r) cm (Örn. 14.52):"))
            sonuc = 2 * (math.pi * yaricap)
            print("Sonuç = ", sonuc)

    def obebhesapla():
        a = int(input("Birinci Sayıyı Giriniz: "))
        b = int(input("İkinci Sayıyı Giriniz: "))

        ebob = None
        fark = None

        if a > b:
            fark = a - b

        elif a < b:
            fark = b - a

        else:
            fark = 0

        if fark == 0:

            ebob = a

        else:
            for i in range(1, fark + 1):
                if a % i == 0 and b % i == 0:
                    ebob = i

        print("Sonuç = ",ebob)

    def inchesapla():
        print("""
        1- Cm Değeri Gir
        2- Inch Değeri Gir
        """)
        inchsecim = int(input("İşleminizi Giriniz(1-2): "))
        while inchsecim < 1 or inchsecim > 2:
            inchsecim = int(input("İşleminizi 1-2 arasında seçiniz: "))

        if inchsecim == 1:
            cm = int(input("Santimetre Giriniz (Örn. 14): "))
            sonuc = cm / 2.54
            print("Sonuç = ",sonuc)

        if inchsecim == 2:
            inch = int(input("Inch Giriniz (Örn. 42): "))
            sonuc = inch * 2.54
            print("Sonuç = ",sonuc)

    def milhesapla():
        print("""
        1- Mili kilometreye çevir
        2- Kilometreyi mile çevir
        """)
        milsecim = int(input("İşleminizi Giriniz(1-2): "))
        while milsecim < 1 or milsecim > 2:
            milsecim = int(input("İşleminizi 1-2 arasında seçiniz: "))

        if milsecim == 1:
            mil = float(input("Uzunluk (Örn. 150,75): "))
            sonuc = mil * 1.609344
            print("Sonuç = ",sonuc)

        if milsecim == 2:
            km = float(input("Uzunluk (Örn. 61,15): "))
            sonuc = km / 1.609344
            print("Sonuç = ",sonuc)

    def rahesapla():
        sayilar = []
        kucuksayi = int(input("Minimum Sayıyı Giriniz: "))
        buyuksayi = int(input("Maximum Sayıyı Giriniz: "))
        adet = int(input("Kaç Adet Sayı İstiyorsunuz: "))

        for i in range(0,adet):
            rastgelesayi = random.randint(kucuksayi,buyuksayi)
            sayilar.append(rastgelesayi)

        print(sayilar)

    def uslusayihesapla():
        taban = int(input("Taban (a) (Örn. 3):"))
        kuvvet = int(input("Kuvvet (n) (Örn. 6):"))
        sonuc = 1
        for i in range(kuvvet):
            sonuc = sonuc * taban

        print("Sonuç = ",sonuc)

    def calistir():
        try:
            menu()
            islemler()
            sec = int(input("İşleminizi Giriniz(1-8): "))
            while sec < 1 or sec > 8:
                sec = int(input("İşleminizi 1-8 arasında seçiniz: "))

            if sec == 1:
                alanhesapla()
            if sec == 2:
                cevrehesapla()
            if sec == 3:
                obebhesapla()
            if sec == 4:
                inchesapla()
            if sec == 5:
                milhesapla()
            if sec == 6:
                rahesapla()
            if sec == 7:
                uslusayihesapla()
            if sec == 8:
                global durum
                durum = False
        except:
            print("Hata! İşlemleri Doğru Yaptığınızdan emin olun.")

    calistir()