def decora(funcion):
	#a = function
	def wrapper(*args, **kwargs):
		a = funcion(*args, **kwargs)
		print(a)
		print("yo le agrego 1")
		b =  a ** 2
		print(b)
	return wrapper


@decora
def sumar(a, x):
	f = a + x
	return f

sumar(2,2)	