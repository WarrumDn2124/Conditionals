# Calculations, ptinting, variables

# Printing to the screen
# The Built in function Print(), prints to the screen
# It will print both screen and numbers
print("Printing to the screen..")
print("Hello")# a string
print("Hello")
print(6) # A number 
print(6 + 6)

# Performing calculations
# Addition +
# Subtraction -
# Multiplication
# Division /
# Exponents **
# Modulo %

print(4 -2) #Sub -> 2
print(4 *2) 
print(4 /3)
print(4 **3)

print("Modulo Operater Test..")
print(5 % 3)
print(10%2)
print(16%3)
#Modulo gives remainders
# Python follows The Order Of Operations
print(4-2*3)
print((4-2) * 3)

#Variables are used to hold data
# Variables are declared and set to a value
badluck = 13 # Declared the variable called badluck and intialized it to 13
# I can print the variable using it's name
print("badluck = " +  str(badluck)) # Cast it to a string:
goodluck = "4"
print("goodluck =" + goodluck)
badluck + 5 # This is pointless
print(badluck)
badluck = badluck + 5 # now badluck is 18
print(badluck)
# You can also save input into vaariable
# Using input(), A prompt goes inside the ()
name = input ("Whats your name")
print("Hello" + name)
print(name * 10)
name = name + "\n"# Escape Charecter(newline)
print(name * 10)

base = input("Enter the base number:")
exp = input ("Enter the exponent:")
print(int(base)  ** int(exp))