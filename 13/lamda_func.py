import math
a=9
ildiz=lambda a : math.sqrt(a)
print(ildiz(a))

def daraja(n):
  return lambda x : x**n

kvadrat = daraja(2)
kub = daraja(3)
print(f"3 ning kavrati {kvadrat(3)}, kubi {kub(3)} ga teng.")

sonlar = list(range(11))
ildizlar = list(map(math.sqrt, sonlar))
print(ildizlar)

# kvadrat hisoblash
def daraja2(x):
  return x**x
print(list(map(daraja2, sonlar)))

# lambda orqali
kvadratlar = list(map(lambda x : x**x, sonlar))
print(kvadratlar)

# map() ga bir necha ro'yxat uzatish
a=[2,5,8,6]
b=[7,4,3,2, 2]
a_plus_b = list(map(lambda x,y:x+y, a,b))
print(a_plus_b)

ismlar=['hasan','husan','eshmat','toshmat']
print(list(map(lambda ism:ism.title(), ismlar)))

# filter() funksiyasi
import random as r

sonlar = r.sample(range(100), 10)

def juftmi(x):
  return x%2==0
juft_sonlar=list(filter(juftmi, sonlar))
print(sonlar)
print(juft_sonlar)

# lamda yordamida
juft_sonlar2 = list(filter(lambda x:x%2==0, sonlar))
print(juft_sonlar2)

mevalar=["olma", "o'rik", "shaftoli", "olcha", "gilos", "banan", "anjir", "anor"]
mevalar_b=list(filter(lambda meva:meva.startswith('a'), mevalar))
print(mevalar_b)

meva_uzun=list(filter(lambda meva:len(meva)>=5, mevalar))
print(meva_uzun)

meva_bosh_oxiri=list(filter(lambda meva: meva.startswith('a')
                             and meva.endswith('r')
                             or len(meva)==4, mevalar))
print(meva_bosh_oxiri)
