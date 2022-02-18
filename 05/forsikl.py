# for sikli
mehmonlar = ["Ali", "Vali", "Hasan", "Husan"]
for mehmon in mehmonlar:
	print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")

s_kv = []
for x in range(1,11):
	print(f"{x}-ning kvadrati {x**2}-ga teng.")
	s_kv.append(x**2)

print(s_kv)

dostlar = []
print("5 ta eng yaqin do'stingizni kiriting:")
for n in range(5):
	dostlar.append(input(f"{n+1}-do'stingizni kiriting:\n"))
print(dostlar)