import pandas as pd
print("Welcome to AMB Online Data Plans")
name = input("What is your name:  ")
age = int(input("How old are you: "))
sex = input("Male or Female:  ")
if sex not in ['Male', 'Female']:
	print(" Invalid type")
	sex = 'Unknown'
restart = ('Y')
chances = 3
balance = 674.15
data = 3600
pin = int(input( "Enter Your 4-Digit Pin"))
while chances >= 0:
	if pin == (1234):
		print("You Entered your pin correctly\n")
		while restart not in ('n', 'NO', 'no', 'N'):
			print("Please Press 1 for your balance\n")
			print("Kindly  Press 2 To Get 100MB\n")
			print("Kindly  Press 3 To Get 1GB\n")
			print("Kindly Press 4 To Get 3GB\n")
			print("Kindly Press 5 to get 5GB\n")
			print("Kindly Press 6 for your data\n")
			print("Kindly Press 7 to pay in\n")
			print("Kindly Press 8 to see your Entry Information\n")
			print( "Kindly Press 9 to Sign-in")
			option = int(input("What would you like to choose: "))
			if option == 1:
				option1 = ('y')
				print("Your balance is Ã£",balance, '\n')
			elif option == 2:
				option2 = ('y')
				data = data + 100
				print("You now have ",data,"MB", '\n')
				print("It has removed Ã£41.66 from your balance\n")
				balance = balance - 41.66
				print("You now have Ã£",balance, '\n')
			elif option == 3:
				data = data + 1200
				print("You now have ",data,"MB", '\n')
				balance = balance - 500
				print("You now have Ã£", balance, '\n')
				print("Warning: It removed Ã£500 from your balance\n")
				restart = input("Would you like to go back:  ")
				if restart in ('n', 'NO', 'no', 'N'):
					print("Thank you")
					break
			elif option == 4:
				option4 = ('y')
				data = data + 3600
				print("It added 3GB to your data")
				balance = balance - 1500
				print("Warning: It removed 1500 from your balance..Try paying in")
			elif option == 5:
				option5 = ('y')
				data = data + 6000
				print("Your data is now ",data, "GB")
				balance = balance - 2500
				print("\nYour Balance is now Ã£", balance)
				restart = ('y')
			elif option == 6:
				print("Your data is ",data, "GB")
			elif option == 7:
				pay_in = float(input("How much would you like to pay in:  "))
				balance = balance + pay_in
				print("Your balance is now Ã£",balance)
			elif option == 8:
				print("These Are Your Entry Information\n")
				print("Name:   " + name, '\n')
				print("Age:  ",age, " years old\n")
				print("Sex:   ",sex, '\n')
			elif option == 9:
				a = int(input(" Do you want to register your (1)company or (2)yourself"))
				if a == 1:
					b = input( "Company name: ")
					c = int(input(" Company phone number: "))
					print(" Welcome, your company name is " + b)
				if a == 2:
					name = input( "Your name: ")
					number = int(input("Your phone number: "))
					email = input(" Your E-mail address: ")
					print(" Welcome, your name is " + name)
			if balance < 0:
				balance = 0				
		else:
				print("Please Enter a correct number")
				chances = chances - 1
				restart = ('n')
				if chances == 0:
					print("Too many tries!!")
					break
	while pin != (1234):
			pin = int(input( "Enter your pin again: "))
			print("Incorrect please")
			chances = chances - 1
			if chances == 0:
				print("Too many tries")
				break					