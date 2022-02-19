# for sikli
# mehmonlar = ["Ali", "Vali", "Hasan", "Husan"]
# for mehmon in mehmonlar:
# 	print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")

# s_kv = []
# for x in range(1,11):
# 	print(f"{x}-ning kvadrati {x**2}-ga teng.")
# 	s_kv.append(x**2)

# print(s_kv)

# dostlar = []
# print("5 ta eng yaqin do'stingizni kiriting:")
# for n in range(5):
# 	dostlar.append(input(f"{n+1}-do'stingizni kiriting:\n"))
# print(dostlar)

# VAZIFA
"""
1. Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
2. Yuoqirdagi sikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)
3. 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
4. Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
5. Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
"""

# 1, 2
names = ["Mirsoli", "Suhrob", "Samad", "Zoxir", "Po'lat"]
for name in names:
	print(f"Salom {name}, dasturlashga xush kelibsiz ;)")
print(f"Kod {len(names)} marta takrorlandi")

# 3
for toq_son in range(9,100, 2):
	print(f"{toq_son}-ning kubi: {toq_son**3}")

# 4
kinolar = []
print("Eng yaxshi ko'rgan 5 ta kino nomini kiriting:")
for kino in range(0,5):
	kinolar.append(input(f"{kino+1}-kino: ").capitalize())
print(kinolar)

# 5
suhbat = int(input("Bugun nechta odam bilan suhbatlashdingiz? - "))
suhbatdosh = []
print("Ularning ismlarini yozing.")
for son in range(0, suhbat):
	suhbatdosh.append(input(f"{son+1}-suhbatdosh: ").capitalize())

print(suhbatdosh)