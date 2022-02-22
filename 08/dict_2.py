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
    'vali':'iphone x',
    'halim':'iphone x',
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

# keys()
print(mahsulotlar.keys())

print('Do\'kondagi mahsulotlar:')
for mahsulot in mahsulotlar.keys():
  print(mahsulot.title())
# Yuqoridagi kodimizda, for siklida .keys() metodini ishlatmasak ham huddi shu natija chiqadi.
bozorlik = ['anor','uzum','non','baliq']
for mahsulot in mahsulotlar:
  if mahsulot in bozorlik:
    print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")

print("Do'konimizdagi mahsulotlar:")
for mahsulot in sorted(mahsulotlar):
  print(mahsulot.title())

# values()
print(telefonlar.values())
for tel in set(telefonlar.values()):
  print(tel.title())

p_dict = {
  "variables":"o'zgaruvchilar, ular orqali har xil malumotlarni saqlab olsak bo'ladi",
  "string":"matn malumot turi.",
  "integer":"son malumot turi.",
  "boolean":"mantiqiy qiymat malumot turi.",
  "list":"har xil turdagi malumotlarni o'zida saqlovchi malumot turi.",
  "tuoles":"o'zgarmas list yaratish",
  "for":"list yoki shu kabi malumotlar ichidan aylanib o'tish uchun hizmat qiluvchi funksiya.",
  "while":"list yoki shu kabi malumotlar ichidan aylanib o'tish uchun hizmat qiluvchi funksiya.",
  "dictionary":"key-value pairs ko'rinishida malumot saqlovchi tur."
}
for k, v in sorted(p_dict.items()):
  print(f"{k} so'zining manosi - {v}.")

davlatlar = {
  "usa":"washington",
  "uzbbekistan":"tashkent",
  "great britain":"london",
  "germany":"berlin",
  "italy":"rome",
  "france":"paris",
  "chine":"pekin",
  "japan":"tokio"
}

print("Davlat nomi:\t Davlat poytaxti:")
for k, v in sorted(davlatlar.items()):
  print(f"{k.title()}\t\t {v.title()}")

# print('Dunyo davlatlari:')
# for davlat in sorted(davlatlar):
#     print(davlat.upper())

# print('\nDavlatlarning poytaxtlari')
# for poytaxt in sorted(davlatlar.values()):
#   print(poytaxt.title())

davlat = input("Qaysi davlat poytaxtini bilishni hohlaysiz?\n").lower()
# for k, v in davlatlar.items():
if davlat in davlatlar:
  if davlat.keys() == 'usa':
    print(f"{davlat.upper()}-ning poytaxti {davlat.title()}.")
  else:
    print(f"{davlat.title()}-ning poytaxti {v.title()}.")
else:
  print("Bu davlat haqida ma'lumot hozircha yo'q.")