def katta_harf(ismlar):
  yangi_ismlar = []
  for n in ismlar:
    yangi_ismlar.append(n.title())
  return yangi_ismlar

ismlar = ['ali', 'vali', 'hasan', 'husan']
bolalar = katta_harf(ismlar[:])
print(bolalar)
print(ismlar)