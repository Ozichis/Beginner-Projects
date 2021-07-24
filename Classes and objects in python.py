class Car():
	pass
	
honda = Car()
tata = Car()

honda.modelname = 'City'
honda.year = '2017'
honda.price = 100000

tata.modelname = 'Bolt'
tata.year = 2016
tata.price = 600000

print(honda.price)

# Changer
class race():
	def __init__(self, modelnames, yearm, amount):
		self.modelnames = modelnames
		self.yearm = yearm
		self.amount = amount
		
amandan = race('City', 2017, 90000)
patan = ('Bolt', 2016, 800000)
print(amandan.amount)

class Driver():
	def __init__(self, name, age, driver_rate):
		self.name = name
		self.age = age
		self.driver_rate = driver_rate
	def amount_inc(self):
		self.amount = (self.price * 1.15)
	
John = Driver('John', 38, '97%')
Kingsley = Driver('Kingsley', 33, '39%')
print(Kingsley.driver_rate)
John.dd = 1500

print(John.__dict__)
print(Kingsley.__dict__)

