# math moduli
from math import sqrt, pow, pi, ceil, floor, fabs

x=9
print(sqrt(x))

y=5
print(pow(y,3))

print(pi)

c=4.4
print(ceil(c))
d=4.6
print(floor(c))

f=-55.6
print(fabs(f))

# random moduli
import random as r

# randint(a,b)
a=r.randint(0,100)
print(a)

# choice()
ismlar=['ali','vali','g\'ani', 'eshmat', 'toshmat']
ism=r.choice(ismlar)
print(ism.capitalize())

g=list(range(0,50,5))
print(g)
print(r.choice(g))

k=list(range(11))
print(k)
r.shuffle(k)
print(k)
