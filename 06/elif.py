yosh = int(input("Yoshingizni kiriting: "))
if yosh <= 4:
	price = 0
elif yosh <= 12:
	price = 5000
elif yosh <= 60:
	price = 15000
else:
	price = 20000

print(f"Sizga kirish {price} so'm")

kun = input("Bugun qaysi kun?\n")
if kun.lower() == 'shanba' or kun.lower() == "Yakshanba":
	day = "dam olish kuni"
else:
	day = "ish kuni"
print(f"Bugun {day}.")

kun2 = input("Bugun nima kun? ")
harorat = float(input("Havo harorati qanday? "))
if (kun2.lower()=='shanba' or kun2.lower()=='yakshanba') and harorat>=30:
    print("Cho'milgani ketdik!")
elif (kun2.lower()=='shanba' or kun2.lower()=='yakshanba') and harorat<30:
    print("Uyda dam olamiz!")

narh = 15000
choy = True
non = False
kompot = True
assorti = False
salat = True

if choy and non:
	narh += 10000
else:
	narh += 5000
print(f"Jami narh {narh} so'm.")

#Quyidagi har bir shart alohida tekshiriladi va bir-biriga bog'liq emas
if choy:   # agar choy olsa
    print("Mijoz choy oldi.")
    narh = narh + 3000
if salat:  # agar salat olsa
    print("Mijoz salat oldi.")
    narh = narh + 5000
if non:    # agar non olsa
    print("Mijoz non oldi.")
    narh = narh + 2000
if kompot: # agar kompot olsa
    print("Mijoz kompot oldi.")
    narh = narh + 5000
if assorti: # agar assorti olsa
    print("Mijoz assorti oldi.")
    narh = narh + 15000
    
print(f"Jami {narh} so'm")

menu = ["osh", "lag'mon", "sho'rva", "chuchvara", "qozonkabob", "kabob"]
ovqat = input("Buyurtma bering: ").lower()
if ovqat in menu:
	print("Buyurtma qabul qilindi")
else:
	print("Afsuski bunday taom yo'q!")
buyurtmalar = ["lag'mon", "osh", "jo'ja"]
if buyurtmalar:
	for taom in buyurtmalar:
	if taom in menu:
		print(f"{taom} menuda bor")
	else:
		print(f"{taom} menuda yo'q")
else:
	print("Savatchangiz bo'sh!")