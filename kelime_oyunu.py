from random import choice

try:
    while True:
        print()
        print("#"*80)
        print("#"*30+ "Kelime Tahmin Oyunu"+ "#"*29)
        print("#"*80)

        kelime = choice(["türkiye","suriye","iran","afganistan","ermenistan","azerbaycan","japonya","çin","ırak","hindistan","maldivler","pakistan","moğolistan","nepal","arabistan","tayland","ürdün","gürcistan ","israil","lübnan","vietnam","kore","filipinler","malezya","tayvan","katar","fransa","rusya","almanya","ispanya","italya","lüksemburg","hollanda","isviçre","belçika","avusturya","slovakya","romanya","ukrayna","danimarka","litvanya","hırvatistan","norveç","finlandiya","isveç","arnavutluk","letonya","makedonya","yunanistan","kıbrıs","sırbistan","kosova","vatikan","portekiz","bulgaristan","arjantin","uruguay","şili","peru"])

        kelime = kelime.upper()

        harfsayisi = len(kelime)

        print("\nKelimemiz {} harflidir.".format(harfsayisi))
        print()

        tahminler = []
        hata = []

        deneme = 7

        while deneme > 0:
            tabela = ""

            for harf in kelime :
                if harf in tahminler:
                    tabela = tabela + harf

                else:
                    tabela = tabela + "_"

            if tabela ==kelime:
                print("Kelimeyi Doğru Bildiniz. Tebrik Ederiz!")
                break

            print("Kelimeyi Tahmin Ediniz", tabela)
            print(deneme, "CANIN VAR!")

            Tahmin= input("Bir Harf Giriniz\n>>>>")
            Tahmin = Tahmin.upper()
            print("-"*20)
            if Tahmin == kelime:
                print("Doğru Bildin!")
                break

            if Tahmin in tahminler or Tahmin in hata:
                print("{} daha önce söylendi. Lütfen başka bir harf söyleyin.".format(Tahmin))

            elif Tahmin in kelime:
                rpt= kelime.count(Tahmin)
                print("Doğru!, {0} harfi kelimemiz içerisinde {1} kere geçiyor.".format(Tahmin,rpt))
                tahminler.append(Tahmin)
            else:
                print("Yanlış!, Kelimede bu harf yok.")
                hata.append(Tahmin)
                deneme=deneme -1
        if deneme == 0:
            print("Hiç Hakkınız Kalmadı. Başaramadın. ")
            print("Kelimemiz {}".format(Tahmin))

        print("Oyundan Çıkmak İstiyorsanız ',' Tuşuna Basınız. Devam Etmek İçin Herhangi Bir Başka Tuşa Basınız.")
        devam = input(">>>>")
        devam = devam.upper()
        if devam == ",":
            break
        else:
            continue
except:
    print("Yanlış Bir İşlem Yapıldı!")