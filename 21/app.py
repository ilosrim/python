def decor(func):
	def wrap():
		print("==========")
		func()
		print("==========")
	return wrap()

@decor
def print_text():
	print("Hello World!")
	
print_text = decor(print_text)
print_text()