kitoblar_savol = "Yaxshi ko'rgan kitoblaringizni kiriting: "
kitoblar = []
while True:
  qiymat = input(kitoblar_savol)
  if qiymat == 'stop':
    break
  else:
    kitoblar.append(qiymat.title())
print(kitoblar)