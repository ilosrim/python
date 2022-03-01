ism = input("Ismingiz: ")
familiya = input("Familiyangiz: ")

def salom_ber(ism, familiya):
  """Fodyalanuvchi ismini qabul qilib, 
  unga salom beruvchi funksiya"""
  print(f"Foydalanuvchi ismi: {ism.title()}\n"
        f"Foydalanuvchi familiyasi: {familiya.title()}")

salom_ber(ism, familiya)
print(salom_ber.__doc__)
