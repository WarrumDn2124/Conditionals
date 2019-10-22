# Conditionals

age = input("Whats your age:")#Prompt for age

# CHeck if the age is more than 17, so the preson
# Can see R rated movies
age = int(age)
if age > 17: # Everything in the if statement only runs if the condition is true.
    print("You can see an R rated movie")

else:print("You cannot see an R rated movie, too bad so sad")

print("Have a nice day!")
# You can check all conditions
# >,<, >=,<=,==(== means equal to)
birthday = input ("Is today your birthday(yes or no?)")
if birthday == "yes":
    print("Happy Birthday!!")

print("Have a nice day!")    

mynum = 7
guess = input("Guess a number between 1 and 10:")
guess = int(guess)
if guess == mynum:
	print("You guessed correctly")
elif guess > mynum:
	print("Too high!")
else:
	print("Too low!")
print("Thanks for playing!")