import sontop as st

def main():
	x = int(input("Son kirting: "))
	taxminlar_user = st.sontop(x)
	taxminlar_pc = st.sontop_pc(x)
	if taxminlar_user < taxminlar_pc:
		print("Tabriklaymiz, siz yutdingiz.")
	elif taxminlar_user > taxminlar_pc:
		print("Siz yutqazdingiz")
	else:
		print("Durrang")
main()
