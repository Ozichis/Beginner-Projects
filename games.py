import random

def rps():
	base = {"r":"Rock", "p":"Paper", "s":"Scissors"}
	c_c = random.choice(["r", "p", "s"])
	player_choice = input("Make your choice between (r)ock, (p)aper, (s)cissors: ")
	while player_choice[0].lower() not in ["r", "p", "s"]:
		print("That's a wrong choice")
		player_choice = input("Make your choice between (r)ock, (p)aper, (s)cissors: ")
	real_choice = player_choice[0].lower()
	if (real_choice == "r" and c_c == "p") or (real_choice == "p" and c_c == "s") or (real_choice == "s" and c_c == "r"):
		print(f"Computer Choice: {base[c_c]}")
		print(f"Your Choice: {base[real_choice]}")
		print(f"You lost\n\n\n")
	elif real_choice == c_c:
		print(f"Computer Choice: {base[c_c]}")
		print(f"Your Choice: {base[real_choice]}")
		print(f"It's a tie\n")
	else:
		print(f"Computer Choice: {base[c_c]}")
		print(f"Your Choice: {base[real_choice]}")
		print(f"You won\n\n\n")
	
def guessing_game(num):
	random_number = random.randint(1, num)
	opinion = 0
	while opinion != random_number:
		opinion = int(input(f"Guess a number from 1 to {num}: "))
		if opinion > random_number:
			print("Your guess is higher than the correct number.")
			pass
		if opinion < random_number:
			print("Your guess is lower than the correct number.")
			pass
	print(f"Hurray! you got the correct number, {random_number}")

while True:
	print("Press 1 to play rock, paper, scissors")
	print("Press 2 to play a guessing game")
	ans = int(input("Choice->"))
	if ans == 1:
		exit = "n"
		while exit != "y":
			rps()
			exit = input("Do you want to exit. (y)es, (n)o: ")
	if ans == 2:
		exit = "n"
		while exit != "y":
			guessing_game(10)
			exit = input("Do you want to exit. (y)es, (n)o: ")