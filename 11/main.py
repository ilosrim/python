def my_func(f, x):
	return f(x)
a = my_func(lambda x: 2*x*x, 5)
print(a)