# def son_kopaytir(*sonlar):
  # yigindi=0
  # for n in sonlar:
    # yigindi*=n
  # return yigindi
# print(son_kopaytir(2,3,4))

def talaba_malumot(kursi, yoshi, **malumot):
  malumot['kursi']= kursi
  malumot['yoshi']=yoshi
  return malumot

talaba1 = talaba_malumot(4, 24, ism="Mirsoli", familiya="Mirsultonov")
print(talaba1)
