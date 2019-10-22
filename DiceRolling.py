import random
#Dice Simulator
#Daniel Warrum
#10/2/19
#Period 1

ones = 0
twos = 0
threes = 0
fours = 0
fives = 0
sixes = 0
count = 0
print("Welcome to the Dice-Simulator!")


Dice = int(input("How many times do you want to roll this imaginary dice? : "))
while (count <= Dice):
	count = count + 1
	randomNum = random.randint(1, 6)
	cChoices = [1, 2, 3, 4, 5, 6]
	ComputerRolls = random.choice(cChoices)
	
	if ComputerRolls == 1:
		print("Dice rolled a 1.") 
		ones = ones + 1
	elif ComputerRolls == 2:
		print("Dice rolled a 2.") 
		twos = twos + 1	 
	elif ComputerRolls == 3:
		print("Dice rolled a 3.") 
		threes = threes + 1
	elif ComputerRolls == 4:
		print("Dice rolled a 4.")
		fours = fours + 1
	elif ComputerRolls == 5:
		print("Dice rolled a 5.")
		fives = fives + 1 
	elif ComputerRolls == 6:
		print("Dice rolled a 6.")
		sixes = sixes + 1

print("1's:" + str(ones))
print("2's:" + str(twos))
print("3's:" + str(threes))
print("4's:" + str(fours))
print("5's:" + str(fives))
print("6's:" + str(sixes))
percentone = 100/Dice * ones
percenttwo = 100/Dice * twos
percentthree = 100/Dice * threes
percentfour = 100/Dice * fours
percentfive = 100/Dice * fives
percentsix = 100/Dice * sixes
print("Percents:")
print("1's:" + str(percentone)+"%")
print("2's:" + str(percenttwo)+"%")
print("3's:" + str(percentthree)+"%")
print("4's:" + str(percentfour)+"%")
print("5's:" + str(percentfive)+"%")
print("6's:" + str(percentsix)+"%")


	
