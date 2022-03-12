#sifre olusturucu
import time
print()
print("Şifre Oluşturma Sistemine Hoşgeldiniz!")
print("-----------------------------------")
isim = input("İsminizi Giriniz: ")
soyisim = input("Soyadınızı Giriniz: ")
tarih = input("Doğum Tarihinizi Giriniz: ")
print("-----------------------------------")
isim = isim.lower() #hepsi küçük
soyisim = soyisim.upper() #hepsi büyük
sifre = isim[0] + "." + isim[2] + soyisim[0] + soyisim[2] + tarih
print()
print("------------------------")
print("| Şifreniz : " + sifre + " |")
print("------------------------")

time.sleep(1000)