print("Ikkita son kiriting")
son1 = float(input("Birinchi son: "))
son2 = float(input("Ikkinchi son: "))

if son1 == son2:
	print(f"{son1}={son2}")
elif son1 > son2:
	print(f"{son1}>{son2}")
else:
	print(f"{son1}<{son2}")
