#!/usr/bin/python

import math


recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
ingredients = { 'milk': 131, 'butter': 48, 'flour': 3 }

def recipe_batches(recipe, ingredients):
	batches = None
	if(recipe.keys() != ingredients.keys()):
		return 0
	else:
		for i in recipe.items():
			for j in ingredients.items():
				if(j[1] < i[1]):
					return 0
				else:
					result = j[1] / i[1]
					if batches == None or result < batches:
						batches = result
	
	return int(batches)


recipe_batches(recipe,ingredients)

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))