# import avto_mod
# 
# avto1 = avto_mod.avto_info("GM", "Lacetti", "oq", "mexanik", 2010, 45000)
# avto_mod.info_print(avto1)

# Qisqa nom bilan modulni chaqirib olish
# import avto_mod as aim
# avto2 = aim.avto_info("gm", "spark", "qora", "avtomat", 2013, 25000)
# aim.info_print(avto2)

# Modul ichcidan malum bir funksiyalarni kochirib olish
# from avto_mod import avto_info, info_print
# avto3 = avto_info("gm", "nexia 3", "oq", "avtomat", 2019, 35000)
# info_print(avto3)

# Funksiyalarga ham qisqa nom berish mumkin
# from avto_mod import avto_info as ainfo, info_print as iprint
# avto4 = ainfo("GM", "cobalt", "oq", "mexanik", 2020, 40000)
# iprint(avto4)

# Modul ichidagi barcha funksiyalarni ko'chirib olish
"""
Diqqat! Bir necha sabablarga ko'ra bu usuldan foydalanish tavsiya qilinmaydi. Katta modullarda yuzlab funksiyalar bo'lishi mumkin,
va funksiya nomi sizning dasturingizdagi boshqa funksiya yoki o'zgaruvchi bilan bir hil nomga ega bo'lsa, dastur xato ishlashiga olib keladi.
"""
from avto_mod import *
avto5 = avto_info("GM", "malibu", "qora", "avtomat", 2021, 100000)
info_print(avto5)
