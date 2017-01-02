#this is a program that contains a function inside an other function this is call recursivity.

#let's creat a function which print a name

def any_name(name):
	return "hello {}".format(name)

print any_name('kevin')

# Great! it's working!

class Person(object):
	"""docstring for Person"""
	name = str
	age = int

	

class Kevin(Person):
	name == 'kevin'
	age == 23