#парсим текст
def parse_recipe():
    with open("recipes.txt") as file:
        lines = [line.strip() for line in file if line.strip()]
#Получаем название блюда и кол-во ингридиентов
    recipe_name = lines[0]
    ingredients_count = int(lines[1])
#Формируем словарь ингридиентов
    ingredients = []
    for line in lines[2:2 + ingredients_count]:
        name, quantity, measure = map(str.strip, line.split("|"))
        ingredients.append({
            "ingredient_name": name,
            "quantity": int(quantity),
            "measure": measure
        })
#Возращаем итоговый слловарь
    return {recipe_name: ingredients}

recipe_dict = parse_recipe()
print(recipe_dict)

#Как добиться результата равному тому что указан в примере?