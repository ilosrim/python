mahsulotlar = ["yog'", "kartoshka", "piyoz", "sabzi", "makaron", "mosh", "guruch", "no'xot", "loviya", "go'sht"]

savat = []
print("Iltimos, savatga 5 ta mahsulot kiriting!")
for i in range(0,5):
	savat.append(input(f"{i+1}-mahsulot: ").lower())

bor_mahsulot = []
yoq_mahsulot = []
# if savat:
# 	for mahsulot in savat:
# 		if mahsulot in mahsulotlar:
# 			print(f"{mahsulot.capitalize()} do'konimizda bor.")
# 		else:
# 			print(f"{mahsulot.capitalize()} do'konimizda yo'q!")
# else:
# 	print("Savat bosh', uni to'ldiring!")

if savat:
	for mahsulot in savat:
		if mahsulot in mahsulotlar:
			bor_mahsulot.append(mahsulot)
		else:
			yoq_mahsulot.append(mahsulot)
else:
	print("Savat bosh', uni to'ldiring!")
	
if yoq_mahsulot:
	print("Do'konimizda quyidagi mahsulotlar yo'q:")
	for mahsulot in yoq_mahsulot:
		print(mahsulot)
else:
	print("Siz so'ragan barcha mahsulotlar do'konimizda bor.")