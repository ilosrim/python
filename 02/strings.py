shahar = "Farg'ona"
davlat = "O'zbekiston"

ism = 'Ahmad'
familiya = 'Qayum'
print("Mening ismim " + ism + ' ' + familiya + '.')

# f-string metodi
print(f"Mening ismim {ism} {familiya}.")

# Maxsus belgilar
print("Hello World")
print("Hello \tWorld")
print("Hello \nWorld")

# upper() va lower()
print(ism.upper())
print(familiya.lower())

# title() va capitalize()
# title har bir yangi so'zning birinchi harflarini katta qiladi
# capiatlize faqat birinchi so'zning birinchi harfini katta qiladi

name = "james bond"
print(name.title())
print(name.capitalize())

# strip(), rstrip() va lstrip() metodlari
# Bu metodlar matnning boshi va oxiridagi bo'sh joylarni olib tashlaydi.
meva = "		olma		"
print(f"Men {meva.rstrip()} yaxshi ko'raman.")
print(f"Men {meva.lstrip()} yaxshi ko'raman.")
print(f"Men {meva.strip()} yaxshi ko'raman.")
print(f"Men {meva} yaxshi ko'raman.")

# INPUT
new_name = input("Ismingiz nima?\n")
print("Salom " + new_name.title())