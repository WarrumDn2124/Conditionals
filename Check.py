#This is a review to make sure nothing was lost over break

#Daniel Warrum
#Period 2

# Variable Declaration and assignment
# Example
myVar = "Hello"
# You try to declare two variables 1 string and 1 number, and assign values
myNum = 5

# While loop
# Example
x = 10
while x < 10:
	print(x)
	x = x - 1 

# Print your name 100 times	
Name = 100
while Name > 0:
	print("Daniel" + str(Name))
	Name = Name - 1

MyName = "DAN"
print("Hello " + MyName)	

FAV = " The MATRIX"
print("My favorite movie is" + str(FAV))

	
NAME = input("What is your name: ")
print("Your name is: " + NAME)
 
Song = input("What is your favorite song? ")
print("Your favorite song is: " + str(Song))

# Casting is changing the type of variable
MyNumber = 40 
print("My number is " + str(MyNumber)) 
num1 = input("Enter a number : ")
num1 = int(num1) + 10
print("num1 + 10 is " + str(num1))

num2 = input("Enter a number : " )
num3 = input("Enter a second number : ")
num4 = int(num2) + int(num3)
print("The two numbers together equal : " + str(num4))

num1 = int(input("Type a number: "))
if num1 > 100:
	print("Your number is greater than 100")

elif num1 == 100:
	print("Your number is equal to 100")
else:
	print("Your number is less than 100")

Birth = input("Is it your birthday??? ")
if Birth == yes:
	print("HAPPY birthday")
if Birth == no:
	print("Its not your birthday")