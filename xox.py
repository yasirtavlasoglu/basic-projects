
oyuntahtasi = [' ' for x in range(10)]

def ekranagoster():
  print(' ' +oyuntahtasi[1] + ' ' + '|' + ' ' +oyuntahtasi[2] + ' ' + '|' + ' ' +oyuntahtasi[3])
  print("------------")
  print(' ' +oyuntahtasi[4] + ' ' + '|' + ' ' +oyuntahtasi[5] + ' ' + '|' + ' ' +oyuntahtasi[6])
  print("------------")
  print(' ' +oyuntahtasi[7] + ' ' + '|' + ' ' +oyuntahtasi[8] + ' ' + '|' + ' ' +oyuntahtasi[9])

def harfkoy(harf,konum):
  oyuntahtasi[konum] = harf

def alanbosmu(konum):
  return oyuntahtasi[konum] == ' '

def tahtadolu():
  if oyuntahtasi.count(' ')> 1:
    return False
  else:
    return True

def kazanan(oyuntahtasi,harf):
  return (oyuntahtasi[1]== harf and oyuntahtasi[2] == harf and oyuntahtasi[3] == harf) or (oyuntahtasi[4]== harf and oyuntahtasi[5] == harf and oyuntahtasi[6] == harf) or (oyuntahtasi[7]== harf and oyuntahtasi[8] == harf and oyuntahtasi[9] == harf) or (oyuntahtasi[1]== harf and oyuntahtasi[4] == harf and oyuntahtasi[7] == harf) or (oyuntahtasi[2]== harf and oyuntahtasi[5] == harf and oyuntahtasi[8] == harf) or (oyuntahtasi[3]== harf and oyuntahtasi[6] == harf and oyuntahtasi[9] == harf) or (oyuntahtasi[1]== harf and oyuntahtasi[5] == harf and oyuntahtasi[9] == harf) or (oyuntahtasi[3]== harf and oyuntahtasi[5] == harf and oyuntahtasi[7] == harf)


def oyuncuhareketi():
  konum = int(input("1-9 arasında bir konum giriniz :"))
  if alanbosmu(konum):
    harfkoy('X', konum)
    if kazanan(oyuntahtasi,'X'):
      ekranagoster()
      print("Tebrikler Kazandınız.")
      exit()
    ekranagoster()
  else:
    print("Girdiğiniz konum dolu, Tekrar konum giriniz :")
    oyuncuhareketi()

def bilgisayarhareket():
  import random
  musait_konumlar = [konum for konum, harf in enumerate(oyuntahtasi) if harf == ' ' and konum !=0 ]

  hareket= 0

  for harf in ['O', 'X']:
    for i in musait_konumlar:
      kopya_tahta = oyuntahtasi[:]
      kopya_tahta[i] = harf
      if kazanan(kopya_tahta, harf):
        hareket= i
        return hareket

  koseler = []

  for i in musait_konumlar:
    if i in[1,3,7,9]:
      koseler.append(i)

  if len(koseler) > 0:
    hareket= random.choice(koseler)
    return hareket

  if 5 in musait_konumlar:
    hareket =5
    return hareket

  icerisi = []

  for i in musait_konumlar:
    if i in[2,4,6,8]:
      icerisi.append(i)

  if len(icerisi) > 0:
    hareket= random.choice(icerisi)
    return hareket

  
def oyun():
  print("XOX Oyununa Hoşgeldin")
  ekranagoster()
      
  while not tahtadolu():
    
    oyuncuhareketi()
    if tahtadolu():
      print("Oyun Berabere Bitti, Kazanan Yok!")
      exit()

    print("-------------------------------")

    bilgisayar_hareket = bilgisayarhareket()
    harfkoy('O', bilgisayar_hareket)
    if kazanan(oyuntahtasi,'O'):
      ekranagoster()
      print("Bilgisayar Kazandı, Tekrardan Denersin ;)")
      exit()

    ekranagoster()
    if tahtadolu():
      print("Oyun Berabere Bitti, Kazanan Yok!")
      exit()
      
    print("-------------------------------")

oyun()


"""
@yasirtavlasoglu
"""
