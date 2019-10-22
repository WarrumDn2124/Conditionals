favFoods = ["Pizza", "Ice cream", "Chicken"]
print(favFoods[0])
print(favFoods[2])
print(favFoods[1])
print(favFoods)
# Adds to the end of the list
favFoods.append("Burgers")
print(favFoods)
print("My 4th favorite food is " + favFoods[3])
# Insert adds to an index in a list
favFoods.insert(1, "Pasta")
print(favFoods)
# Remove an item from the list 
favFoods.remove("Chicken")
print(favFoods)
# You can remove by the index
favFoods.pop(0)
print(favFoods)

favFoods.insert(0, "Pizza")
# Loop through a list 
for food in favFoods:
	print(food)


numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#Loop through the list and add all of the numbers up.
sum = 0
for num in numlist:
	sum = sum + num



print(sum)
# Length of the list
print(len(favFoods))
# list for our favorite movies
# pompt for a favorite movie
Myfood = input("What is your favorite food? ")
favFoods.append(Myfood)
print(favFoods)

favmovies = ["Dark Knight","The Matrix" ,"Point Break" ]
Mymovies = input("Whats your favorite movie? ")
favmovies.append(Mymovies)
print(favFoods[len(favFoods) - 1])
print(favmovies)