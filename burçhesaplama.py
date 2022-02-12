burclar = {
    "ocak":{
        "Oğlak":list(range(1,21)),
        "Kova":list(range(21,32))},

    "şubat":{
        "Kova":list(range(1,19)),
        "Balık":list(range(21,30)),},

    "mart":{
        "Balık":list(range(1,21)),
        "Koç":list(range(21,32)),},

    "nisan":{
        "Koç":list(range(1,21)),
        "Boğa":list(range(21,32)),},

    "mayıs":{
        "Boğa":list(range(1,21)),
        "İkizler":list(range(21,32)),},

    "haziran":{
        "İkizler":list(range(1,22)),
        "Yengeç":list(range(21,32)),},

    "temmuz":{
        "Yengeç":list(range(1,23)),
        "Aslan":list(range(21,32)),},

    "ağustos":{
        "Aslan":list(range(1,23)),
        "Başak":list(range(21,30)),},

    "eylül":{
        "Başak":list(range(1,23)),
        "Terazi":list(range(21,32)),},

    "ekim":{
        "Terazi":list(range(1,24)),
        "Akrep":list(range(21,32)),},

    "kasım":{
        "Akrep":list(range(1,23)),
        "Yay":list(range(21,32)),},

    "aralık":{
        "Yay":list(range(1,22)),
        "Oğlak":list(range(21,32)),}
}

gun = int(input("Gün: "))
ay = input("Ay: ")

cs = burclar[ay]

for burc, gunler in cs.items():
    if gun in gunler:
        print(f"{gun} {ay} {burc} burcudur.")
