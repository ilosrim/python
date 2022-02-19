yosh = int(input("Yoshingizni kiriting: "))

if yosh<=4 or yosh>=60:
	price = 0
elif yosh <= 18:
	price = 10000
else:
	price = 20000
print(f"Muzeyga kirish {price} so'm")