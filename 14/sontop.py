import random as r

def sontop(x):
  r_son = r.randint(1, x)
  print(f"Men 1 dan {x} gacha son o'yladim, topa olasizmi?\n")
  taxminlar = 0
  while True:
    taxminlar += 1
    taxmin = int(input(">>> "))
    if taxmin < r_son:
      print(f"Xato, men o'ylagan son bundan kattaroq. Yana harakat qiling: ")
    elif taxmin > r_son:
       print(f"Xato, men o'ylagan son bundan kichikroq. Yana harakat qiling: ")
    else:
      break
  print(f"Tabriklaymiz, {taxminlar} taxmin bilan topdingiz!")
  return taxminlar

def sontop_pc(x):
  input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing, men topaman")
  quyi=1
  yuqori=x
  taxminlar=0
  while True:
    taxminlar+=1
    if quyi != yuqori:
      taxmin = r.randint(quyi, yuqori)  
    else:
      taxmin=quyi
    javob = input(f"Siz {taxmin} sonini o'yladingiz: to'g'ri(t) "
                  f"men o'ylagan son bundan kattaroq (+), yoki kichikroq (-) ".lower())
    if javob == '-':
      yuqori = taxmin-1
    elif javob == '+':
      quyi = taxmin+1
    else:
      break
  print(f"Men {taxminlar} ta taxmin bilan topdim")
  return taxminlar
