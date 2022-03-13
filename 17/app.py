# Class yaratish
from datetime import datetime
yil =  datetime.now()
h_yil = int(yil.year)

class Talaba:
  def __init__(self, ism, familiya, t_yil):
    self.name=ism
    self.lastname=familiya
    self.born=t_yil
  
  def tanishtir(self):
    return f"Mening ismim {self.name.title()}, {self.born}-yilda tug'ilganman."
  
  def get_name(self):
    return self.name
  def get_age(self, yil):
    return yil-self.born

talaba1 = Talaba("mirsoli", "mirsultonov", 1998)
talaba2 = Talaba("hasan", "husanov", 2000)
talaba3 = Talaba("toshmat", "eshmatov", 1992)

print(talaba1.tanishtir())
print(talaba1.get_age(h_yil))

print(talaba2.tanishtir())
print(talaba2.get_age(h_yil))

print(talaba3.tanishtir())
print(talaba3.get_age(h_yil))

