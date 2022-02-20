car_0 = {
	"model":"bmw",
	"color":"black"
}
print(car_0["model"])

talaba = {
	"ism":"vali",
	"yosh":20,
	"konikma": [
		"HTML", 
		"CSS", 
		"JS", 
		"TS", 
		"Python",
		"C",
		"C++",
		"C#",
		("ES5", "ES6")
	]
}
print(talaba["konikma"])
talaba["kurs"] = 4
print(talaba)
del talaba["yosh"]
print(talaba)

phone = talaba.get("ism", "Ism mavjud emas!").title()
print(phone)

# Vazifa
# 1, 2
oila = {
	"otam": {
		"ism":"Mirzaahmad",
		"t_yil":1967,
		"viloyat":"Farg'ona",
		"taom":"osh"
	},
	"onam": {
		"ism":"Mamurahon",
		"t_yil":1967,
		"viloyat":"Farg'ona",
		"taom":"sho'rva"
	},
	"akam": {
		"ism":"Mirjalol",
		"t_yil":1991,
		"viloyat":"Farg'ona",
		"taom":"kavob"
	}
}

print(f"Otamning ismi {oila['otam']['ism']}, {oila['otam']['t_yil']}-yilda, {oila['otam']['viloyat']} viloyatida tug'ilgan.")
print(f"Akamning sevimli taomi {oila['akam']['taom']}.")

p_dict = {
	"variables":"o'zgaruvchilar, ular orqali har xil malumotlarni saqlab olsak bo'ladi",
	"string":"matn malumot turi.",
	"integer":"son malumot turi.",
	"boolean":"mantiqiy qiymat malumot turi.",
	"list":"har xil turdagi malumotlarni o'zida saqlovchi malumot turi.",
	"tuoles":"o'zgarmas list yaratish",
	"for":"list yoki shu kabi malumotlar ichidan aylanib o'tish uchun hizmat qiluvchi funksiya.",
	"while":"list yoki shu kabi malumotlar ichidan aylanib o'tish uchun hizmat qiluvchi funksiya.",
	"dictionary":"key-value pairs ko'rinishida malumot saqlovchi tur."
}

soz = input("Biron so'z kiriting: ")
if soz in p_dict:
	print(f"'{soz}' so'zining manosi - {p_dict[soz]}")
else:
	print(f"'{soz}' so'zining manosi hozircha bizning ro'yxatda yo'q ;)")