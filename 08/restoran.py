menu = {
	"osh":15000,
	"sho'rva":12000,
	"kavob":12000,
	"lag'mon":18000,
	"lavash":25000,
	"tandir":50000,
	"manti":5000
}

print("3 ta taom buyurtma bering.")
buyurtmalar = []

for n in range(0, 3):
	buyurtmalar.append(input(f"{n+1}-taom: ").lower())

for buyurtma in buyurtmalar:
	if buyurtma in menu:
		print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
	else:
		print(f"Kechirasiz bizda {buyurtma} yo'q.")