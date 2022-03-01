from datetime import datetime

# 1. Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.
# hozirgi_yil = datetime.now()
# # print(hozirgi_yil.year)
# # print(type(hozirgi_yil))

# ism = input("Ismingiz: ")
# t_yil = int(input("Tug'ilgan yilingiz: "))

# def yosh(ism, t_yil):
#   print(f"{ism.title()}, sizning yoshingiz {int(hozirgi_yil.year) - t_yil} da.")

# yosh(ism, t_yil)

# 2. Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.
# son = float(input("Son kiriting: "))

# def kvadrat_va_kub(son):
#   print(f"Sonning kvadrati: {son**2}\n"
#         f"Sonning kubi: {son**3}")
# kvadrat_va_kub(son)

# 3. Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.
# son = float(input("Son kiriting: "))
# def juft_or_toq(son):
#   if son%2 != 0:
#     print("Toq son")
#   else:
#     print("Toq son")
# juft_or_toq(son)

# 4. Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing. Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.
# son1 = float(input("Son kiriting: "))
# son2 = float(input("Son kiriting: "))
# if son1 > son2:
#   print(son1)
# elif son1 < son2:
#   print(son2)
# else:
#   print("Sonlar teng")

# 5. Foydalanuvchidan x va y sonlarini olib, x^y ni konsolga chiqaruvchi funksiya yozing.
# son1 = float(input("Son kiriting: "))
# son2 = float(input("Son kiriting: "))
# def kv(son1, son2):
#   print(son1**son2)
# kv(son1, son2)

# 6. Yuqoridagi funksiyada y uchun 2 standart qiymatini bering.
# x = float(input("Son kiriting: "))
# y = float(input("Son kiriting: "))
# def kv(x, y=2):
#   print(x**y)
# kv(x, y)

# 7. Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya yozing. Natijalarni konsolga chiqaring.
son = float(input("Son kiriting: "))

def my_func(son):
  for n in range(2, 11):
    if son%n == 0:
      print(f"{son} {n}-ga qoldiqsiz bo'linadi.")
    
my_func(son)