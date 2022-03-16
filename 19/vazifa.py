class Shaxs:
  def __init__(self, ism, familiya, passport, t_yil):
    """Shaxslar haqida ma'lumot"""
    self.ism=ism
    self.familiya=familiya
    self.passport=passport
    self.t_yil=t_yil

    def get_info(self):
      """Shaxs haqida ma'lumot qaytaruvchi metod"""
      info = f"{self.ism} {self.familiya}, "
      info += f"Passport: {self.passport}, {self.t_yil}-yilda tug'ilgan"
      return info
    
    def get_age(self, yil):
      """Shaxsning yoshini qaytaruvchi metod"""
      return yil - t_yil

class Talaba(Shaxs):
  """Talaba klasi"""
  def __init__(self, ism, familiya, passport, t_yil, id_raqam, manzil):
    super().__init__(ism, familiya, passport, t_yil)
    self.id_raqam=id_raqam
    self.manzil=manzil
    self.bosqich=2
    self.fanlar=[]

    def get_id(self):
      """ID raqamni qaytaruvchi metod"""
      return self.id_raqam

    def get_bosqich(self):
      """Bosqichni qaytaruvchi metod"""
      return self.bosqich

    def get_info(self):
      """Talaba haqida malumot qaytaruvchi metod"""
      info = f"{self.ism} {self.familiya}. "
      info += f"{self.bosqich}-bosqich, ID raqam: {self.id_raqam}"
      return info
    
    def subcribe_fan(self, fan):
      return self.fanlar.append(fan)

class Manzil:
  def __init__(self, uy, kocha, tuman, viloyat):
    self.uy=uy
    self.kocha=kocha
    self.tuman=tuman
    self.viloyat=viloyat

    def get_manzil(self):
      """Manzilni qaytaruvchi metod"""
      manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
      manzil += f"{self.kocha} ko'chasi, {self.uy} uy"
      return manzil

class Fan:
  def __init__(self, nomi):
    self.nomi=nomi

bio = Fan("Biologiya")
Chim = Fan("Kimyo")
Mat = Fan("Matematika")

talaba_manzil = Manzil(82, "Yangiqishloq", "Uchko'prik", "Farg'ona")
talaba1 = Talaba("Mirsoli", "Mirsultonov", "FB2523124", 1998, "0123456789", talaba_manzil)

print(talaba1.manzil.viloyat)