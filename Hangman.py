
name = input("Whats your name? ")
print("Hello " +name, ",Welcome to Hangman!!")
myString = "Arizona"
mysteryWord = list(myString)
print(mysteryWord)
Guesslist = []

for letter in mysteryWord:
	Guesslist.append("_")

print(Guesslist)

#How to replace a certain index
Guesslist[3] = "z"
print(Guesslist)
letter = input("Enter a letter:")
if letter in mysteryWord:
	print("That letter is in the word")
else:
	print("The letter is not in the word")

count = 0
Guesslist = list(mysteryWord)
for letter2 in Guesslist:
	if letter2 == letter:
		print(count)
		count += 1