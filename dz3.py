import random

day = 1

class Father:
	def __init__(self, name):
		self.health = 100
		self.name = name
		self.gladness = 50
		self.money = 100

class Son: 
	def __init__(self, name, father):
		self.name = name
		self.gladness = 25
		self.money = 0
		self.health = 75
		self.father = father
	
	

	def print_all_properties(self):
		print(f"\n<========================================>")
		print(f"\n|\t<=== Name: {self.name} ===> \t\t|")
		print(f"|\t<=== Health: {self.health} ===> \t\t|")
		print(f"|\t<=== Gladness: {self.gladness} ===> \t\t|")
		print(f"|\t<=== Money: {self.money} ===> \t\t|")
		print(f"|\t<=== Day: {day} ===> \t\t|")
		print(f"\n<========================================>")

	def na_pivo(self):
		if (self.father.money > 0) and (self.money < 0):
			print("<=== Batya day deneg! ===>")
			self.money += 10
		else:
			self.gladness += 5
			self.money -= 10
			self.health -= 1
			print(" <=== Pivoooooo.... ===>")
	def kachalka(self):
		if (self.father.money > 0):
			print("<=== kachaemsya ===>")
			self.health += 5
		else:
			print("<=== na turniki ===> ")
			self.health += 2
	def gaming(self):
		self.gladness += 10
		self.health -= 2
		print("<=== Igraem v Tanki... ===>")
		
	def batya_na_rabotu(self):
		self.money += 20
		self.health -= 3
		self.gladness -= 10
		print("<=== Dengi..... ===>")


Analtolii = Father("Nick")
Ansatasia = Son("Eva", Analtolii)
Ansatasia.print_all_properties()

while Ansatasia.health > 0:
	day += 1
	cube = random.randint(1, 4)
	if (cube == 1):
		Ansatasia.na_pivo()
		Ansatasia.print_all_properties()
	elif (cube == 2):
		Ansatasia.kachalka()
		Ansatasia.print_all_properties()
	elif (cube == 3):
		Ansatasia.gaming()
		Ansatasia.print_all_properties()
	elif (cube == 4):
		Ansatasia.batya_na_rabotu()
		Ansatasia.print_all_properties()