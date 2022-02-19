son = int(input("Istalgan butun son kirting: "))

for i in range(2, 11):
	if son%i == 0:
		print(f"{son} soni {i} soniga qoldiqsiz bo'linadi.")
	# else:
	# 	print(f"{son} soni {i} soniga qoldiqli bo'linadi.")