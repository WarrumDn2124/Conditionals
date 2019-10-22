print("Welcome to the To Do list")
todoList = []

for todo in todoList:
	print(todoList)
while True:
	print("Enter a to add an item")
	print("Enter r to remove an item")
	print("Enter p to print the list")
	print("Enter q to quit")
	choice = input("Choose : ")
	
	if choice == "q":
		break
	elif choice == "a":
		if choice == "a":
			
			MyList = input ("What do you need to be reminded of?? ")
			todoList.append(MyList)
	elif choice == "r":
		todoList.remove(input("What do you want to forget?"))
	elif choice == "p":
		print(todoList)
	
	else:
		print("You didnt choose a prescribed letter that was listed!")

