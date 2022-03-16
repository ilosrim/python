class Shaxs:
  def __init__(self, ism, familiya, passport, tyil):
    """Shaxslar haqida ma'lumot"""
    self.ism=ism
    self.familiya=familiya
    self.passport=passport
    self.tyil=tyil

  def get_info(self):
    """Shaxs haqida malumot qaytaruvchi metod"""
    info = f"{self.ism} {self.familiya}, "
    info += f"Passport: {self.passport}, {self.tyil}-yilda tug'ilgan"
    return info

  def get_age(self, yil):
    """Shaxsning yoshini qaytaruvchi metod"""
    return yil - self.tyil

class Talaba(Shaxs):
  """Talaba klassi"""
  def __init__(self, ism, familiya, passport, tyil, id_raqam, manzil):
    """Talaba hususiyatlari"""
    super().__init__(ism, familiya, passport, tyil)
    self.id_raqam=id_raqam
    self.bosqich=3
    self.manzil=manzil
    self.fanlar=[]

  def get_id_raqam(self):
    """ID raqamni qaytaruvchi metod"""
    return self.id_raqam
  
  def get_bosqich(self):
    """Bosqichni qaytaruvchi metod"""
    return self.bosqich

  def get_info(self):
    """Talaba haqida ma'lumot"""
    info = f"{self.ism} {self.familiya}. "
    info += f"{self.bosqich}-bosqich, ID raqami: {self.id_raqam}."
    return info

  def fanga_yozil(self, fan):
    return self.fanlar.append(fan)

  def get_fan(self):
    return [fan.get_info() for fan in self.fanlar]

  def remove_fan(self):
    for n in self.fanlar:
      return [n]


class Manzil:
  def __init__(self, uy, kocha, tuman, viloyat):
    self.uy=uy
    self.kocha=kocha
    self.tuman=tuman
    self.viloyat=viloyat

  def get_manzil(self):
    """manzilni ko'rish"""
    manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
    manzil += f"{self.kocha} ko'chasi, {self.uy} uy."
    return manzil

talaba_manzil = Manzil(82, "Yangiqishloq", "Uchko'prik", "Farg'ona")
talaba2 = Talaba("Eshmat", "Toshmatov", "CB5624120", 1998, 99999998, talaba_manzil)
print(talaba2.manzil.get_manzil())

class Fan:
  def __init__(self, nomi):
    self.nomi=nomi

biologiya = Fan("Biologiya")
kimyo = Fan("Kimyo")
matematika = Fan("Matematika")
talaba2.fanga_yozil(kimyo)
print(talaba2.fanlar)
print(talaba2.remove_fan())
print(talaba2.get_fan())