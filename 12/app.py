# Moslashuvchan funksiya
# *args

# def summa(*sonlar):
    # """Kiritilgan sonlar yig'indisini hisoblovchi funksiya"""
    # yigindi = 0
    # for n in sonlar:
        # yigindi+=n
    # return yigindi
# print(summa(1,2,3,6,5,4,7,8,9))
def summa(*sonlar):
  return sum(sonlar)
print(summa(1,2,3))

# **kwargs - keyword arguments
def avto_info(kompaniya, model, **malumotlar):
  """Avto haqidagi malumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
  malumotlar['kompaniya']=kompaniya
  malumotlar['model']=model
  return malumotlar
avto1 = avto_info("GM", "Lacetti", rang='qora', yil=2005)
print(avto1)
