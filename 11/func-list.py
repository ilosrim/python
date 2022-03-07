def bahola(ismlar):
  baholar = {}
  while ismlar:
    ism = ismlar.pop()
    baho = input(f"Talaba {ism.capitalize()}ning bahosini kiriting: ")
    baholar[ism]=baho
  return baholar

talabalar = ['ali', 'vali', 'g\'ani']
baholar = bahola(talabalar[:])
print(baholar)