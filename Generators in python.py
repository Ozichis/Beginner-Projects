# Let's start with what are generators?
# Generators are functions that return traversable objects and produce objects one at a time only when required.
# Next we are going to learn the advantages of using generators?
# 1. They are easy to implement implement_iter()_next_() automatically
# 2. Better memory management and utilization
# 3. They can be used to produce infinite items
# 4. They can also pipeline a number of operations.
# Now we are going to learn how to write generators in python
# To write generators in python we need to make use of the yield keyword instead of return
# This is an example code for generators
def new(dict):
	for x,y in dict.items():		
		yield x,y
a = {1: "Hi", 2: "Welcome"}
b = new(a)
print(b)
next(b)

# This is also another example code
def myfunc(i):
	while i<=3:
		yield i
j = myfunc(2)
print(next(j))

# This is also another example code for generators
def ex():
	n = 3
	yield n
	n = n*n
	yield n
C = ex()
print(next(C))

# Generators with loop
def ex():
	n = 3
	yield n
	n = n*n
	yield n
C = ex()
for x in C:
	print(x)
	
# Generators expressions
f = range(6)
print("List comp", end= ":")
q = [x+2 for x in f]
print(q) 
print(" gen exp", end=':')
r = (x+2 for x in f)
print(r)
for x in r:
	print(x)

# This is also another example code for generators expressions
print( "gen exp", end=" :")
r = (x+2 for x in f) 
print(r)
print(min(r))

# Now we are going to learn all about Use Cases
# The three types of Use Cases are:
# 1. Fibonacci Series.
# 2. Number Stream.
# 3. Simewave

# We would start with the fibonacci
# Fibonacci
def fib():
	f,s = 0,1
	while True:
		yield f
		f,s = s,f+s
for x in fib():
	if x>50:
		break
	print(x, end= " ")
	
# Next we go to Number Stream which generates a number a stream
# Number Stream
a = range(100)
b = (x for x in a)
print(b)
for y in b:
	print(y)
	
# If we change it to
a = range(2, 100, 2)
b = (x for x in a)
print(b)
for y in b:
	print(y)
	
# Now we would learn simewaves that generates sine waves using seaborn
# Simewaves
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sb 
def s(flip = 2):
	 x = np.linspace(0, 14, 100)
	 for i in range(1, 5):
	 	plt.plot(x, np.sin(x + 1 * .5) * (7 - i) * flip)
	 	
sb.set()
s()
plt.show()

# We have come to the end of generators in python