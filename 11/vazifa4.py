# son = int(input("Son kiriting: "))

# def tub_son(son):
#   is_prime = True
#   for n in range(2, son):
#     if n>1:
#       for i in range(2, n):
#         if (n%i) == 0:
#           is_prime = False
#           break
#     if is_prime:
#       print(n, "tub son")
#       # else:
#       #   print(son, "tub son emas")
# tub_son(son)

min = int(input("1-son: "))
max = int(input("2-son: "))
def tub_sonlar_top(min, max):
  tub_sonlar = []
  for n in range(min, max + 1):
    tub = True
    if n == 1:
      tub = False
    elif n == 2:
      tub = True
    else:
      for x in range(2, n):
        if n % x == 0:
          tub = False
    if tub:
      tub_sonlar.append(n)

  return tub_sonlar
tub_son = tub_sonlar_top(min, max)
print(tub_son)