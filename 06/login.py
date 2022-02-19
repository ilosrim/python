logins = ["ab", "bc", "be", "bf", "ca"]
login = input("Yangi login kiriting: ")

if login.lower() in logins:
	print(f"{login} logini band, boshqa login kiriting!")
else:
	print("Xush kelibsiz yangi foydalanuvchi!")