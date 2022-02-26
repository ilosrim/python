# Input
# ism = input("Ismingizni kiriting: ")
# yosh = int(input(f"Salom {ism.title()}, yoshingiz nechchida: "))
# print(f"{ism.title()}, siz {yosh} yoshdasiz.")

# while
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# qiymat = ''
# while qiymat != 'exit':
#   qiymat = input(savol)
#   if qiymat != 'exit':
#     print(float(qiymat)**2)

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#   qiymat = input("Istalgan son kiriting: ")
#   if qiymat == 'exit':
#     break
#   else:
#     print(f"{qiymat}-ning kvadrati {float(qiymat)**2}-ga teng")

# print('1-dastur tugadi.')
# sonlar = list(range(1,11))
# for son in sonlar:
#   if son == 5:
#     continue
#   else:
#     print(f"{son}-ning kvadrati {float(son**2)}-ga teng.")
# print('2-dastur tugadi.')

# son=0
# while son<=10:
#   son+=1
#   if son%2!=0:
#     continue
#   else:
#     print(son)

son = 0
while son<10:    
    if son%2!=0:
        continue
    else:
        print(son)
    son += 1