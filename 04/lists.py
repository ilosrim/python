mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
narhlar = [12000, 18000, 10900, 22000] # narhlar ro'yxati (sonlar)
sonlar = ['bir', 'ikki', 3, 4, 5] # sonlar va matnlar aralash ro'yxat
ismlar = [] # bo'sh ro'yxat

print("Birinchi meva: " + mevalar[0])

sonlar[1] = 2
print(sonlar)

# Yangi elemt qo'shish
mevalar.append("qovoq")
print(mevalar)

# Listning istalgan joyiga element qo'shish uchun insert() metodidan foydalaniladi
mevalar.insert(1, "gilos")
print(mevalar)

# Elementni o'chirish
del mevalar[0]
print(mevalar)
len_meva = len(mevalar)-1
del mevalar[len_meva]
print(mevalar)

# Qiymati bo'yicha o'chirish
mevalar.remove("anjir")
print(mevalar)

# Elementni sug'urib olish
bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
mahsulot = bozorlik.pop(1)
print(f"Men {mahsulot} oldim")
print(f"Olinmagan mahsulotlar ro'yxati: {bozorlik}")

cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
cars.sort(reverse=True)
print(cars)

nums = [64,11,65,9,263,1,6,4]
nums.sort()
print(nums)

mehmonlar = ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh', 'Shamsiddin']
print("sorted() qaytargan ro'yxat:", sorted(mehmonlar))
print("Asl ro'yxat o'zgarmas qoldi:", mehmonlar)

ages = [12, 98, 34, 65, 34, 76, 11]
ages.sort()
print(ages)
print(sorted(ages, reverse=True))

fruits = ['pear','banana','apple','watermelon','lemon']
fruits.reverse()
print(fruits)

# range() FUNKTSIYASI
sonlar = list(range(1,11)) # 
print(sonlar)

juft_sonlar = list(range(0,20,2))
toq_sonlar = list(range(1,20,2))
print("Juft sonlar: ", juft_sonlar)
print("Toq sonlar: ", toq_sonlar)

narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]

arzon = min(narhlar)
qimmat = max(narhlar)
jami = sum(narhlar)

print(arzon)
print(qimmat)
print(jami)

cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
three = cars[0:4] # 0-indexdan boshlab 4 ta element ajratib ol
print(three)
print(cars[2:5])

print(cars[:4]) # Ro'yxat boshidan 4-gacha kesadi (0,1,2,3)
print(cars[2:]) # 2-elementdan boshlab ro'yxat oxirigacha kesib oladi

sonlar = [1, 2, 3, 4, 5] # donlar degan ro'yxat yaratamiz
sonlar2 = sonlar # sonlar2 degan ro'yxatni sonlar ga tenglaymiz
sonlar2.append(6) # sonlar2 ga 6 sonini qo'shamiz
sonlar2.append(7) # sonlar2 ga 7 sonini qo'shamiz
print("Bu sonlar ro'yxati:", sonlar)
print("Bu sonlar2 ro'yxati:", sonlar2)
sonlar3 = sonlar[:]
sonlar3.append(8)
print("Bu sonlar3 ro'yxati:", sonlar3)

# TUPLES - O'ZGARMAS RO'YXAT
tomonlar = (20,3.2,48)
print(tomonlar)

toys = ('bus','car','bear','dino','snake','lizard')
print(toys[0])
print(toys[-1])
print(toys[2:5])

# VAZIFA
"""
1. O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
2. Ro'yxatning uzunligini konsolga chiqaring
3. sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
4. sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
5. Asl ro'yxatni qaytadan konsolga chiqaring
6. reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
7. sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
8. 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
9. Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
10. Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
11. Ro'yxatdagi elementlar sonini hisoblang
12. Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
13. taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
14. nonushta degan yangi ro'yxatga taomlardan nusxa oling
15. Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
16. Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
17. Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
"""
davlatlar = ["Uzbekistan", "Kazakistan", "Kirgizistan", "Tadjikistan", "Turkmanistan", "Turkiya", "Azarbayjan", "Vengriya", "Ukraina"]
print(davlatlar)
print(len(davlatlar))
print(sorted(davlatlar))
print(sorted(davlatlar, reverse=True))
print(davlatlar)
davlatlar.reverse()
print(davlatlar)
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)

j_son = list(range(120,1200,2))
y = sum(j_son)
print(y)
k = min(j_son)
m = max(j_son)
print(m-k)
print(len(j_son))

# 1 2 3 4 5 6 7 8 9 10
r_boshidan = j_son[0:20]
r_ortasidan = j_son[530:550]
r_oxiridan = j_son[-20:]
print(r_boshidan)
print(r_ortasidan)
print(r_oxiridan)

taomlar = ["Manti", "Honim", "Osh", "Kabob", "Chuchvara"]
nonushta = taomlar[:]
nonushta.remove("Manti")
nonushta.remove("Honim")
nonushta.remove("Osh")
nonushta.append("Non")
nonushta.append("Shakar")
nonushta.append("Choy")

print(taomlar)
print(nonushta)

nonushta2 = ("Asal" "Choy")
nonushta2[0] = "Shakar" # TypeError: 'str' object does not support item assignment