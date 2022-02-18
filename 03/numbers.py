# SONLAR

a = 20
b = 3
c = a + b
print(c)

radius = int(input("Son kiriting: "))
PI = 3.14569
diametr = 10
aylana = PI * radius * diametr
print(aylana)

# UZUN SONLARNI KIRITISH
aholi_soni = 7_562_842_000
print(aholi_soni)

# BIR NECHTA O'ZGARUVCHIGA QIYMAT BERISH
x, y, z = 498, 94, 6

ism = 'Jobir'
yosh = 36
# xabar = ism + ' ' + yosh + ' yoshda'
# xabar = f"{ism} {yosh} yoshda"
xabar = ism + ' ' + str(yosh) + ' yoshda'

print(xabar)
print(type(yosh))

t_yil = int(input("Tug'ilgan yilingizni kiriting: "))
sana = 2022 - t_yil
print("Yoshingiz: " + str(sana))