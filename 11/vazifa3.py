# d=2r
# p=2r*pi
# S=PI*R**2

from cmath import pi
from xml.etree.ElementTree import PI


radius = int(input("Aylananing radiusini kiriting: "))

def my_math(radius, pi=3.14159):
  aylana = {
    "radius": radius,
    "diametr": 2 * radius,
    "perimetr": 2 * radius * pi,
    "yuza": pi * radius ** 2,
  }
  return aylana
aylana = my_math(radius, pi)
print(aylana)