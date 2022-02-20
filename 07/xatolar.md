```py
	print "Hello World!"
	Natija: SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Hello World!")?
```
```py
	print("Hello World!
	Natija: SyntaxError: EOL while scanning string literal
```
```py
	print("Hello World!"
	Natija: SyntaxError: unexpected EOF while parsing
```
```py
	print("O'ngacha sanaymiz")
	for n in range(10):
	print(n+1)
	Natija: IndentationError: expected an indented block
```
```py
	RunTime Error
	son = input("Istalgan son kiriting: ")
	print(f"{son} ning kvadrati {son**2} ga teng")
	Natija: TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
```
```py
	prit("Hello World!")
	Natija: NameError: name 'prit' is not defined
```
```py
	son = int(input("Istalgan son kiriting: "))
	if son>=0:
	    print("Musbat son")
	else:
	    print("Manfiy son")	
	input = 45.5
	ValueError
```
```py
	mevalar = ['olma','anor','uzum']
	print(mevalar[3])
	Natija: IndexError: list index out of range
```
```py
	x, y = 50, 50
	z = 250/(x-y)
	Natija: ZeroDivisionError: division by zero
```
```py
	son = float(input("Istalgan son kiriting: "))
	ildiz = son**1/2
	print(f"{son} ning ildizi {ildiz} ga teng")
	Yuqoridagi natijaga e'tibor bersangiz, 9 sonining ildizi 4.5 deb chiqdi. Sababi, 2-qatorda ildizni hisoblashda foydalanuvchi kiritgan son avval 1-darajaga oshirildi va undan keyin 2 ga bo'lindi. Kodni to'g'rilaymiz:

	son = float(input("Istalgan son kiriting: "))
	ildiz = son**(1/2)
	print(f"{son} ning ildizi {ildiz} ga teng")
```