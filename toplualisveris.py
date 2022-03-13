import time
import webbrowser

try:
    print("-"*35)
    print("  Toptancıya Hoşgeldin Kaptan!")
    print("-"*35)
    time.sleep(1.5)
    print()
    print("--------------------")
    print("1) Hepsiburada")
    print("2) Trendyol")
    print("3) GittiGidiyor")
    print("4) N11")
    print("5) Vatan Bilgisayar")
    print("6) Media Markt")
    print("7) Teknosa")
    print("8) Amazon")
    print("9) Bangood")
    print("10) AliExpress")
    print("--------------------")
    print()
    giris = int(input("Seçimini Yap Kaptan: "))
    time.sleep(1.5)

    if (giris==1):
        print("-"*40)
        print("  Hepsiburada'ya Yönlendiriliyorsunuz...")
        print("-" * 40)
        time.sleep(1.5)
        webbrowser.open("https://www.hepsiburada.com/")

    elif (giris==2):
        print("-"*40)
        print("  Trendyol'a Yönlendiriliyorsunuz...")
        print("-" * 40)
        time.sleep(1.5)
        webbrowser.open("https://www.trendyol.com/")

    elif (giris==3):
        print("-"*40)
        print("  GittiGidiyor'a Yönlendiriliyorsunuz...")
        print("-" * 40)
        time.sleep(1.5)
        webbrowser.open("https://www.gittigidiyor.com/")

    elif (giris==4):
        print("-"*40)
        print("  N11'e Yönlendiriliyorsunuz...")
        print("-" * 40)
        time.sleep(1.5)
        webbrowser.open("https://www.n11.com/")

    elif (giris==5):
        print("-"*40)
        print("  Vatan Bilgisayar'a Yönlendiriliyorsunuz...")
        print("-" * 40)
        time.sleep(1.5)
        webbrowser.open("https://www.n11.com/")

    elif (giris==6):
        print("-"*40)
        print("  Media Markt'a Yönlendiriliyorsunuz...")
        print("-" * 40)
        time.sleep(1.5)
        webbrowser.open("https://www.mediamarkt.com.tr/?utm_source=mediamarkt.com&utm_medium=own-button&utm_term=headernavigation-link~turkey")

    elif (giris==7):
        print("-"*40)
        print("  Teknosa'ya Yönlendiriliyorsunuz...")
        print("-" * 40)
        time.sleep(1.5)
        webbrowser.open("https://www.teknosa.com/")

    elif (giris==8):
        print("-"*40)
        print("  Amazon'a Yönlendiriliyorsunuz...")
        print("-" * 40)
        time.sleep(1.5)
        webbrowser.open("https://www.amazon.com.tr/")

    elif (giris==9):
        print("-"*40)
        print("  Bangood'a Yönlendiriliyorsunuz...")
        print("-"*40)
        time.sleep(1.5)
        webbrowser.open("https://tr.banggood.com/")

    elif (giris==10):
        print("-"*40)
        print("  AliExpress'e Yönlendiriliyorsunuz...")
        print("-"*40)
        time.sleep(1.5)
        webbrowser.open("https://tr.aliexpress.com/")

    else:
        print("-"*30)
        print("  Yanlış Tuşlama Yapıldı!")
        print("-" *30)
        time.sleep(2)

except:
    print("-" * 30)
    print("  Yanlış İşlem Yaptınız!")
    print("-" * 30)
    time.sleep(2)

"""
@yasirtavlasoglu
"""