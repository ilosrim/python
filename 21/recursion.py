# n! = n * (n-1)!

def factorial(x):
	"""Factorial"""
	if x == 1:
		return 1
	else:
		return x * factorial(x-1)

print(factorial(5))

def is_even(x):
	if x == 0:
		return True
	else:
		return is_odd(x-1)

def is_odd(x):
	return not is_even(x)

print(is_odd(13))
print(is_even(22))

def fib(x):
  if x == 0 or x == 1:
    return 1
  else: 
    return fib(x-1) + fib(x-2)
print(fib(4))

first = {1,2,3,4,5,6}
second = {4,5,6,7,8,9}

print(first | second)
print(first & second)
print(first - second)
print(second - first)
print(first ^ second)

"""
Data Structures


As we have seen in the previous lessons, Python supports the following data structures: lists, dictionaries, tuples, sets.

When to use a dictionary:
- When you need a logical association between a key:value pair.
- When you need fast lookup for your data, based on a custom key.
- When your data is being constantly modified. Remember, dictionaries are mutable.

When to use the other types:
- Use lists if you have a collection of data that does not need random access. Try to choose lists when you need a simple, iterable collection that is modified frequently.
- Use a set if you need uniqueness for the elements.
- Use tuples when your data cannot change.
"""