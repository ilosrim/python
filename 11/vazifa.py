from datetime import datetime
h_vaqt = datetime.now()

# ism = input("Ism: ")
# familiya = input("Familiya: ")
# t_yil = int(input("Tug'ulgan yil: "))
# t_joy = input("Tug'ulgan joy: ")
# email = input("Email: ")
# t_raqam = input("Telefon raqam: ")
def malumot(ism, familiya, t_yil, t_joy, email='', t_raqam=None):
  mijoz = {
    'ism': ism,
    'familiya': familiya,
    't_yil': t_yil,
    'yosh':h_vaqt.year-t_yil,
    't_joy': t_joy,
    'email': email,
    't_raqam': t_raqam
  }
  return mijoz

mijozlar = []
while True:
  ism = input("Ism: ")
  familiya = input("Familiya: ")
  t_yil = int(input("Tug'ulgan yil: "))
  t_joy = input("Tug'ulgan joy: ")
  email = input("Email: ")
  t_raqam = input("Telefon raqam: ")
  mijozlar.append(malumot(ism, familiya, t_yil, t_joy, email, t_raqam))
  javob = input("Yana davom etasizmi? (ha/yo'q) \n")
  if javob != 'ha':
    break

for mijoz in mijozlar:
  print(f"{mijoz['ism'].title()} {mijoz['familiya'].title()},\n"
        f"{mijoz['yosh']} yoshda, telefoni: {mijoz['t_raqam']}"
  )