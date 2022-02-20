talaba_0 = {
    'ism':'alijon',
    'familiya':'shamshiyev',
    'yosh':22,
    'fakultet':'matematika',
    'kurs':4
    }

print(talaba_0.items())
for key, value in talaba_0.items():
    print("Key: ", key)
    print("Value: ", value)

telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
    }

for k, q in telefonlar.items():
    print(f"{k.title()}ning telefoni {q}")


mahsulotlar = { # Do'kondagi mahsulotlar
  'olma':10000,
  'anor':20000,
  'uzum':40000,
  'anjir':25000,
  'shaftoli':30000
    }

print(mahsulotlar.keys())
print('Do\'kondagi mahsulotlar:')
for mahsulot in mahsulotlar.keys():
  print(mahsulot.title())
# Yuqoridagi kodimizda, for siklida .keys() metodini ishlatmasak ham huddi shu natija chiqadi.
bozorlik = ['anor','uzum','non','baliq']
for mahsulot in mahsulotlar:
  if mahsulot in bozorlik:
    print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")