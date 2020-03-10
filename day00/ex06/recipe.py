cookbook = {
	'sandwhich': {'ingredients' : ['ham','bread','cheese', 'tomatoes'], 'meal' : 'lunch', 'prep_time' : '10'},
	'cake': {'ingredients' : ['flour', 'sugar', 'eggs'], 'meal' : 'dessert', 'prep_time' : '60'},
	'salad': {'ingredients' : ['avocado', 'arugula', 'tomatoes', 'spinach'], 'meal' : 'lunch', 'prep_time' : '15'}
}

def print_recipe(name) :
	print("Recipe for")

def delete_recipe(name) :
	print("oh")

def add_recipe(name, ingredients, meal, prep_time) :
	print("oh")

def print_cookbook() :
	print("oh")

print("Please select an option by typing the corresponding number:")
print("1: Add a recipe")
print("2: Delete a recipe")
print("3: Print a recipe")
print("4: Print the cookbook")
print("5: Quit\n")

value = input("Choose...\n")
if (value == 1) :
	name = input("Choose name of recipe\n")
	add_recipe(name, ingredients, meal, prep_time)
elif (value == 2) :
	print("Choose recipe to delete\n")
	print_recipe('cake')
elif (value == 3) :
	recipe = input("Please enter the recipe's name to get its details:\n")
	print_recipe(recipe)
elif (value == 4) :
	names = cookbook.keys()
	for x in names :
		print("Recipe for".join()
elif (value == 5) :
	print("\nCookbook closed.")

