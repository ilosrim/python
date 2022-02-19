import math
# IF ELSE
"""
 Ternary Operator in Python
 [on_true] if [expression] else [on_false] 
"""

avtolar = ['audi','Bmw','volvo','kia','hyundai']
for avto in avtolar:
	if avto.lower() == "bmw":
		print(avto.upper())
	else:
		print(avto.title())

ism = input("Ismingizni kiriting: ").lower()
# if ism != "admin":
# 	print("Xayir")
# else:
# 	print("Hush kelibsiz!")
print("Hush kelibsiz") if ism == "admin" else print("Hayir!")


son = int(input("Son kiriting: "))
kv = son**2
s_kv = int(input(f"{son}-ning kvadrati nechchi?\n"))

if s_kv == son**2:
	print("Tog'ri")
else:
	print("Xato")

x, y = 50, 20
print("x>y") if x>y else print("x<y")

# AMALIYOT
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
	if car != "gm":
		print(car.title())
	else:
		print(car.upper())

print("Ikkita son kiriting")
son1 = int(input("Birinchi son: "))
son2 = int(input("Ikkinchi son: "))
print("Sonlar teng") if son1 == son2 else print("Teng emas")

son_ = int(input("Istalgan son kiritng: "))
print("Musbat son") if son_ >= 0 else print("Manfiy son")

son_1 = int(input("Musbat son kiriting: "))
if son_1 >= 0:
	print(math.sqrt(son_1))
else:
	print("Musbat son kiriting!")