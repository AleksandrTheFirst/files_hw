with open('recipes.txt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        recipe_name = line.strip()
        ingredients_count = file.readline()
        ingredients = []
        for p in range(int(ingredients_count)):
            recipe = file.readline().strip().split(' | ')
            product, quantity, chars = recipe
            ingredients.append({'name': product, 'quantity': quantity, 'measure': chars})
        file.readline()
        cook_book[recipe_name] = ingredients

