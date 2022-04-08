# Inheritance

class Animal:
	def __init__(self, name, color):
		self.name=name
		self.color=color
	def get_name(self):
		return self.name

class Cat(Animal):
	def myau(self):
		print("Myauuu...")
class Dog(Animal):
	def wuf(self):
		print("Wufff...")

jack = Dog("Jack", "white")
jack.wuf()

##########################################

class A:
	def method(self):
		print("First class")
class B(A):
	def second_method(self):
		print("Second class")
class C(B):
	def third_method(self):
		print("Thrid method")

c = C()
c.method()
c.second_method()
c.third_method

##########################################