# ismlar = []

# print("Yaqin do'stlaringiz ro'yxatini yuzamiz.")
# n=1
# while True:
#   savol = f"{n}-do'stingiz ismini kiriting: "
#   ism = input(savol)
#   ismlar.append(ism)
#   javob = input("Yana ism qo'shasizmi? (ha/yo'q): ")
#   if javob == 'ha':
#     n+=1
#     continue
#   else:
#     break
# print("Do'stlaringiz ro'yxati:")
# for ism in ismlar:
#   print(ism.title())
  
# print("Do'stlaringiz ismini saqlaymiz.")
# dostlar = {}
# ishora = True
# while ishora:
#   ism = input("Do'stingiz ismini kiriting: ")
#   yosh = int(input(f"{ism.title()}ning yoshini kiritng: "))
#   dostlar[ism] = yosh
#   javob = input("Yana qo'shishni istaysizmi? (ha/yo'q): ")
#   if javob == "yo'q":
#     ishora = False

# for ism, yosh in dostlar.items():
#   print(f"{ism.title()} {yosh} da")

# cars = ["nexia", "lacetti", "matiz", "nexia", "kamaz", "nexia"]
# while 'nexia' in cars:
#   cars.remove('nexia')
# print(cars)

# talabalar = ['hasan', 'husan', 'olim', 'botir']
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#     print(f"{talaba.title()} baholandi")
#     baholangan_talabalar[talaba] = baho