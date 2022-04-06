from itertools import count, accumulate, takewhile, product, permutations

for i in count(3):
	print(i)
	if i >= 11:
		break

nums = list(range(8))
print(nums)
print(list(takewhile(lambda x: x<=6, nums)))

letters = ("A", "B")
print(list(product(letters, range(4))))
print(list(permutations(letters)))

a={1, 2}
print(len(list(product(range(3), a))))

def power(x, y):
  if y == 0:
    return 1
  else:
    return x * power(x, y-1)
		
print(power(2, 3))