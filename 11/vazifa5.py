son = int(input("Son kiriting: "))

def fibonacci_soni(son):
  sonlar = []
  for x in range(son):
    if x == 0 or x == 1:
      sonlar.append(1)
    else:
      sonlar.append(sonlar[x-1] + sonlar[x-2])
  return sonlar
print(fibonacci_soni(son))