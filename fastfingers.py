import datetime
import time

try:
    print("Hoşgeldiniz!")
    print()
    print("-"*45)
    print("  !! Kendi Cümlenizi Mi Yazmak İstersiniz?\n  !! Yoksa Uygulamaya Ait Cümleleri Mi?")
    print("-"*45)
    print()
    print("="*30)
    giris = input("  kendi & uygulama : ")
    print("="*30)
    print()

    if giris== "kendi":
        cumle = input("Lütfen Cümlenizi Giriniz: ")
        print("*"*(len(cumle)+3))
        print(" "+cumle)
        print("*" * (len(cumle)+3))
        input("Hazır olduğunuzda ENTER 'e basınız. ")
        print("ENTER 'e basınca sonuç gösterilir")
        print("Süre başladı")
        print()

        basla = datetime.datetime.now()

        yazi = input("Yazınız: ")

        bitir = datetime.datetime.now()

        hiz = basla - bitir
        sure = abs(round(hiz.total_seconds(), 2))

        time.sleep(1.5)
        print(f"{sure} saniyede yazdın.")

    elif giris=="uygulama":

        def secenek():
            print("-"*23)
            print("  kolay - orta - zor")
            print("-"*23)
            print()
            derece = input("Lütfen Bir Derece Seçiniz: ")
            print()

            if derece=="kolay":
                print("-"*36)
                kolaycumle = print("  CÜMLENİZ : merhabalar, ben yasir.")
                print("-" * 36)
                print()
                input("!! Hazır olduğunuzda ENTER 'e basınız. ")
                print("!! ENTER 'e basınca sonuç gösterilir")
                print("!! Süre başladı")
                print()

                basla = datetime.datetime.now()

                yazi = input("Yazınız: ")

                bitir = datetime.datetime.now()

                hiz = basla - bitir
                sure = abs(round(hiz.total_seconds(), 2))

                time.sleep(1.5)
                print(f"{sure} saniyede yazdın.")

            elif derece=="orta":
                print("-" * 48)
                ortacumle = print("  CÜMLENİZ : Merhabalar, Ben Yasir Tavlaşoğlu")
                print("-" * 48)
                print()
                input("!! Hazır olduğunuzda ENTER 'e basınız. ")
                print("!! ENTER 'e basınca sonuç gösterilir")
                print("!! Süre başladı")
                print()

                basla = datetime.datetime.now()

                yazi = input("Yazınız: ")

                bitir = datetime.datetime.now()

                hiz = basla - bitir
                sure = abs(round(hiz.total_seconds(), 2))

                time.sleep(1.5)
                print(f"{sure} saniyede yazdın.")

            elif derece=="zor":
                print("-" * 75)
                zorcumle = print("CÜMLENİZ = Merhabalar, Ben Yasir Tavlaşoğlu, Tanıştığıma Memnun Oldum.")
                print("-" * 75)
                print()
                input("!! Hazır olduğunuzda ENTER 'e basınız. ")
                print("!! ENTER 'e basınca sonuç gösterilir")
                print("!! Süre başladı")
                print()

                basla = datetime.datetime.now()

                yazi = input("Yazınız: ")

                bitir = datetime.datetime.now()

                hiz = basla - bitir
                sure = abs(round(hiz.total_seconds(), 2))

                time.sleep(1.5)
                print(f"{sure} saniyede yazdın.")

        secenek()

    else:
        print("ERROR!")

except:
    print("ERROR!")


"""
    @yasirtavlasoglu
"""