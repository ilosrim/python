def oraliq(min, max, qadam=1):
  sonlar = []
  while min<max:
    sonlar.append(min)
    min += qadam
  return sonlar

a = oraliq(0,10)
b = oraliq(10, 21, 2)
c = oraliq(20, 31, 3)

print(a)
print(b)
print(c)

def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
  avto = {
    'kompaniya': kompaniya,
    'model': model,
    'rangi': rangi,
    'korobka': korobka,
    'yili': yili,
    'narhi': narhi
  }
  return avto

avto1 = avto_info('UzDeawoo', 'Tiko', 'Oq', 'Mexanika', 2000)
avto2 = avto_info('GM', 'Malibu', 'Qora', 'Avtomat', 2010, 30000)

avtolar = [avto1, avto2]

print("Avtolar ro'yxati:")
for avto in avtolar:
  if avto['narhi']:
    narh = avto['narhi']
  else:
    narh = 'Bebaho'
  print(f"{avto['rangi'].title()} {avto['model']}, narhi: {avto['narhi']}")