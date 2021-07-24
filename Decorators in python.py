# This is an example code for decorators
def func1(name):
	return f"Hello {name}"
	
	
def func2(name):
	return f"{name} , how you doing?\n"
	
	
def func3(func4):
	return func4('Dear learner')
	
print(func3(func1))
print(func3(func2))

# Let me show you another example
def func():
	print("first function")
	def func1():
		print("first child function\n")
	def func2():
		print("second child function")
		
	func2()
	func1()
			
func()

# Let me show you another example
def func(n):
	def func1():
		return "loanerCamp"
	def func2():
		return "python\n"
	if n == 1:
		return func1
	else:
		return func2
a = func(1)
b = func(2)
print(a())
print(b())

# Let me show you some more examples for you to understand it better
def function1(function):
	def wrapper():
		print("hello")
		function()
		print("welcome to python tutorial by loanerCamp\n")
	return wrapper
def function2():
	print("pythonistan")
	
function2 = function1(function2)

function2()

# Let's make some changes to the last program
def function1(function):
	def wrapper():
		print("hello")
		function()
		print("welcome to python tutorial by loanerCamp\n")
	return wrapper
@function1
def function2():
	print("pythonistan")
	
function2()

# You can see that it gives you the same output
# Let me show you another
def function1(function):
	def wrapper(*args, **kwargs):
		print("Hello")
		function(*args, **kwargs)
		print("welcome to loanerCamp python tutorial\n")
	return wrapper
	
@function1
def function2(name):
		print(f"{name}")
		
		
function2("Dear learner")

# This is another example of decorators	
def function1(function):
	def wrapper(*args, **kwargs):
		print("It worked\n")
	return wrapper
	
		
@function1
def function2(name):
		print(f"{name}")
		
function2("python")

# Let's learning fancy decorators
# There are sets of Decorators
# 1. Class decorators
# 2. Stateful decorators
# 3. Classes As decorator
# Let me show you an example
class Square:
		def __init__(self,side):
			self._side = side
		@property
		def side(self):
			return self._side
		@side.setter
		def side(self, value):
			if value >= 0:
				self._side = value
			else:
				print("error")
		@property
		def area(self):
			return self._side **2
		@classmethod
		def unit_square(cls):
			return cls(1)
s = Square(5)
print(s.side)
print(s.area)

# Let me show you a few more examples
import functools
def singleton(cls):
	@functools.wraps(cls)
	def wrapper(*args, **kwargs):
		if not wrapper.instance:
			wrapper.instance = cls(*args, *kwargs)
		return wrapper.instance
		wrapper.instance = None
		return wrapper

@singleton
class one():
	pass
	
first = one()
second = one()

print(first is second)

# This is another 