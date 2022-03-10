import random as r

son = int(input("Son kiriting: "))
r_son = r.randint(1,10)
def son_top(son):
  while True:
    if son > r_son:
      print("Bu sondan kichikroq")
    if son < r_son:
      print("Bu sondan kattaroq")
    else:
      print("To'g'ri")
      break
son_top(son)
