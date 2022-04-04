from uuid import uuid4

class Avto:
  num_avto = 0
  def __init__(self, make, model, rang, yil, narh, km=0):
    self.make=make
    self.model=model
    self.rang=rang
    self.yil=yil
    self.narh=narh
    self.__km=km
    self.__id=uuid4()
    Avto.num_avto += 1

  def get_km(self):
    return self.__km
  
  def get_id(self):
    return self.__id

  def update_km(self, up_km):
    if up_km>0:
      self.__km+=up_km
    else:
      print("Mashina km-ini kamaytirib bo'lmaydi!")

avto1= Avto("GM", "Malibu", "oq", 2020, 50000, 10)
print(avto1.get_id())
avto1.update_km(20)
print(avto1.get_km())
print(avto1.num_avto)