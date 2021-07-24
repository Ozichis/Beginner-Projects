#This is an example of a lambda function
x=lambda a: a*a
print(x(3))
def new(a):
	return a
new(3)

# This is another example of a lambda function
def new_func(x):
	return(lambda y: x+y)
t = new_func(3)
w = new_func(2)
print(t(3))
print(w(2))

# Lambda within filter()
mylist = [1,2,3,4,5,6]
newlist = list(filter(lambda a: (a/3==2), mylist)) #SYNTAX = filter(function,interable)
print(newlist)

# Lambda within map()
mylist = [1,2,3,4,5,6]
p = list(map(lambda a: (a/3!=2), mylist))
print(p)

# Lambda within reduce()
from functools import reduce
a = reduce(lambda a,b: a+b, [23, 56, 43, 98, 1])
print(a)

# Lambda for Algebra
#Linear equations
s = lambda a: a*a
print(s(4)) 

# This is another example
#3x+4y
d = lambda x,y: 3*x+4*y
print(d(4,7))

#Quadratic equations
#(a+b)^2
c = lambda a,b: (a+b)**2
print(c(3,4))

#Map-Reduce Functions
def new(a):
	return a*a
x = map(new, [1, 2, 3, 4])
print(x)
print(list(x))

#What if we make a change to the last codes
def new(a,b):
	return a*b
x = map(new, [1, 2, 3, 4],[2, 3, 4, 5])
print(x)
print(tuple(x))

#This is another source code for Map-Reduce Functions
st = [1,2,3,4,5]
y = list(map(lambda x: x+3, st))
print(y)

#The Filter() function
#filter(func, interable)
def newl(i):
	if i>=3:
		return i
j = filter(newl, (1,2,3,4,5,6,7))
print(j)
print(tuple(j))

# This is another example with the filter() function
z = filter(lambda x: (x>=3), (1,2,3,4,5,6,7))
print(list(z))

#The reduce function
#reduce(function, iterable)
from functools import reduce
def a(x,y):
	return x+y
s = reduce(a, [1, 3,4,5,6,7, 7, 8, 8])
print(s)

# This is also another example of the reduce function
f = reduce(lambda q,p: q*p, [1,2,3,4,5,6,7,7])
print(f)

# Now we are qoing to learn how to use the filter() within map() function
# This is an example
c = map(lambda x: x+x, filter(lambda x: (x>=4), [2, 3, 4, 5]))
print(tuple(c))

# Map within filter()
d = filter(lambda x: (x>=4), map(lambda x: x+x, [2,3,4,5,6]))
print(set(d))

# Map() and filter() within reduce()
r = reduce(lambda x,y: x+y, map(lambda x: x+x, filter(lambda x: (x<=4), [1,2,3,4,5,6,7])))
print(r)

# We have come to the end of Lambda Functions	