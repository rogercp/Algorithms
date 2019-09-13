#!/usr/bin/python

import math



# recipe = { 'milk': 2, 'sugar': 40, 'butter': 20}
# ingredients = {'milk': 5, 'sugar': 120, 'butter': 500}


def recipe_batches(recipe, ingredients):
	batches = None
	if(recipe.keys() != ingredients.keys()):
		return 0
	else:
		for (j), (r) in zip(ingredients.items(), recipe.items()):
			divide = j[1] // r[1]
			if j[1] < r[1]: 
				return 0 
			else:
				if batches == None or divide < batches:  
					batches = divide
	
	return batches


# recipe_batches(recipe,ingredients)

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))









