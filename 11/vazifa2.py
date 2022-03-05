son1 = float(input("1-sonni kiriting: "))
son2 = float(input("2-sonni kiriting: "))
son3 = float(input("3-sonni kiriting: "))

def k_qaytar(son1, son2, son3):
  if son1>son2 and son1>son3:
    return son1
  elif son2>son1 and son2>son3:
    return son2
  else:
    return son3
katta_son = k_qaytar(son1, son2, son3)
print(katta_son)