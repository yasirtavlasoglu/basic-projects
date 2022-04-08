import random
import time

liste = []
print("-"*75)
print("  Çekilişi Başlatmak İçin 'başlat', İptal Etmek İçin 'iptal' Yazınız.")
print("-"*75)
time.sleep(1)
while True:
    try:
        giris = input(" Çekilişe Katılacak Kişiler: ")
        if giris == "iptal":
            print("-"*75)
            sor = input(" Kişiyi mi iptal edeceksiniz (kisi), Yoksa çekilişi mi? (cekilis): ")
            time.sleep(1)
            print("-"*75)
            if sor == "kisi":
                sor1 = input(" Kimi İptal Etmek İstiyorsun? : ")
                time.sleep(1)
                print("-"*40)
                if sor1 in liste:
                    yer = liste.index(sor1)
                    liste.pop(yer)
                    print(" Kişiyi Çekilişten İptal Ettik.")
                    print(liste)
                    time.sleep(1)
                else:
                    print(" Böyle Bir Kişi Çekilişte Yok.")
                    print("-"*40)
                    print(liste)
                    time.sleep(1)
                    print("-"*40)
            elif sor == "cekilis":
                try:
                    while True:
                        liste.pop()
                except:
                    print(" Çekiliş İptal Edilmiştir.")
                    break
        elif giris == "başlat":
            print("-"*40)
            sor2 = int(input(" Çekilişi Kaç Kişi Kazanacak? : "))
            time.sleep(1)
            sonuc = random.sample(liste,sor2)
            if len(liste) < sor2 :
                print(" Kazanacak Kişi Sayısı Girilen Kişi Sayısından Fazla Olamaz! ")
                time.sleep(1)
                print(" Lütfen Tekrar Deneyiniz! ")
                time.sleep(1)
            else:
                print("-"*40)
                print(" Kazananlar: ",sonuc)
                print("-"*40)
                break
        else:
            liste.append(giris)
    except:
        print(" Hatalı Giriş Yaptınız!\nLütfen Tekrar Deneyiniz! ")
        print()
        time.sleep(1)

"""
@yasirtavlasoglu
"""