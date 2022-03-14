class Talaba:
  def __init__(self, ism, familiya, t_yil):
    """Talaba hususiyatlari"""
    self.ism=ism
    self.familiya=familiya
    self.t_yil=t_yil
    self.bosqich=4

  def get_name(self):
    return self.ism
  
  def get_last_name(self):
    return self.familiya
  
  def get_age(self, yil):
    return yil-self.t_yil

  def get_info(self):
    """Talaba haqida malumot"""
    return f"Talaba {self.ism} {self.familiya} {self.t_yil}-yil, {self.bosqich}-bosqich o'quvchisi."

  def set_bosqich(self, bosqich):
    """Talabaning kursini yangilovchi metod"""
    self.bosqich=bosqich

  def update_bosqich(self):
    """Talabaning kursini 1 taga oshirivchi metod"""
    self.bosqich += 1

talaba1=Talaba("Mirsoli", "Mirsultonov", 1998)
# talaba1.bosqich=3

talaba1.update_bosqich()
talaba1.update_bosqich()
print(talaba1.get_info())


talaba2 = Talaba("Hasan", "Husanov", 1995)
talaba3 = Talaba("Eshmat", "Toshmatov", 2002)

class Fan:
  def __init__(self, nomi):
    self.nomi=nomi
    self.talabalar_soni=0
    self.talabalar=[]

  def get_name(self):
    """Fan nomi"""
    return self.nomi

  def add_students(self, talaba):
    """Fanga yangi talabalar qo'shuvchi metod"""
    self.talabalar.append(talaba)
    self.talabalar_soni+=1
  
  def get_students(self):
    """Fanga yozilgan talabalar haqida malumot"""
    return [x.get_info() for x in self.talabalar]

  def get_stunets_num(self):
    """Fanga yozilgan talabalar soni"""
    return self.talabalar_soni

kimyo = Fan("Organik kimyo")
kimyo.add_students(talaba1)
kimyo.add_students(talaba2)
kimyo.add_students(talaba3)

# k_talabalari = kimyo.get_students()
print(kimyo.get_students())



def see_methods(kalass):
  return [method for method in dir(kalass) if method.startswith('__') is False]

print(dir(Talaba))
print(see_methods(Talaba))
print(see_methods(talaba1))

# __dict__ metodi obyektning hususiyatlarini lug'at ko'rinishida qaytaradi
print(talaba2.__dict__.keys())
print(talaba2.__dict__.values())
