yosh = input("Yoshingiz nechida? (chiqish uchun 'exit' yoki 'quit' yozing) - ")

while True:
  if yosh == 'exit' or yosh == 'quit':
    break
  else:
    if int(yosh) <= 7:
      print("Kirish 2000 so'm")
      break
    elif int(yosh) <= 18:
      print("Kirish 3000 so'm")
      break
    elif int(yosh) <= 65:
      print("Kirish 10000")
      break
    elif int(yosh) > 65:
      print("Kirish tekin")
      break
    else:
      print("Noto'g'ri amal")
      break