from statistics import mode


class Avto:
  def __init__(self, model, color, year):
    """
    Avto classining hususiyatlari
    Args:
        model (_type_): avto modeli
        color (_type_): avto rangi
        year (_type_): avto ishlab chiqarilgan yili
    """
    self.model=model
    self.color=color
    self.year=year
    self.km=0
  
  def get_info(self):
    """
    Returns:
        _type_: avto haqida malumot qaytaruvchi funksiya
    """
    return f"{self.color.title()} rangli {self.model}, {self.year}-yilda ishlab chiqarilgan."

  # def set_km(self, km):
  #   self.km = km

  def update_km(self, km):
    self.km += km

avto1 = Avto("damas", "oq", 2010)
print(avto1.get_info())
avto1.update_km(1200)

class Avtosalon:
  def __init__(self, nomi, manzili, s_avto):
    self.nomi=nomi
    self.manzili=manzili
    self.s_avto=s_avto
    self.avtos=[]

  def add_avtos(self, avto):
    self.avtos.append(avto)

  def get_info(self):
    return [x.get_info() for x in self.avtos]

avtosalon1 = Avtosalon("Asaka", "Andijon", ["Damas", "Matiz", "Tiko"])
avtosalon1.add_avtos(avto1)

print(avtosalon1.get_info())

def see_methods(classes):
  return [x for x in dir(classes) if x.startswith('__') is False]

print(dir(Avto))
print(dir(Avtosalon))
print(see_methods(Avto))
print(see_methods(Avtosalon))