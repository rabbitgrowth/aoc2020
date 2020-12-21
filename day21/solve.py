from collections import defaultdict

foods = []
with open('input.txt') as f:
    for line in f:
        lhs, rhs = line.rstrip('\n').removesuffix(')').split(' (contains ')
        ingredients = set(lhs.split(' '))
        allergens   = set(rhs.split(', '))
        foods.append((ingredients, allergens))

allergen_map = defaultdict(list)
for ingredients, allergens in foods:
    for allergen in allergens:
        allergen_map[allergen].append(ingredients)

identified = {}
while len(identified) < len(allergen_map):
    for allergen, ingredient_sets in allergen_map.items():
        ingredients = set.intersection(*ingredient_sets) - set(identified)
        if len(ingredients) == 1:
            (ingredient,) = ingredients
            identified[ingredient] = allergen

print(sum(ingredient not in identified
          for ingredients, _ in foods
          for ingredient in ingredients))
print(','.join(sorted(identified, key=identified.get)))
