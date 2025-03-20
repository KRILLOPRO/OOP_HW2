import os


def read_cookbook(filename):
    cook_book = {}
    with open(filename, encoding='utf-8') as file:
        while line := file.readline().strip():
            dish_name = line
            ingredients_count = int(file.readline().strip())
            ingredients = []
            for _ in range(ingredients_count):
                ingredient_name, quantity, measure = file.readline().strip().split(' | ')
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure
                })
            cook_book[dish_name] = ingredients
    return cook_book


def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                name = ingredient['ingredient_name']
                if name in shop_list:
                    shop_list[name]['quantity'] += ingredient['quantity'] * person_count
                else:
                    shop_list[name] = {
                        'measure': ingredient['measure'],
                        'quantity': ingredient['quantity'] * person_count
                    }
    return shop_list


def merge_files(file_list, output_file):
    file_data = []

    for file in file_list:
        with open(file, encoding='utf-8') as f:
            lines = f.readlines()
            file_data.append((file, len(lines), lines))

    file_data.sort(key=lambda x: x[1])

    with open(output_file, 'w', encoding='utf-8') as f:
        for file_name, line_count, lines in file_data:
            f.write(f"{file_name}\n{line_count}\n")
            f.writelines(lines)
            f.write('\n')


# Использование
cook_book = read_cookbook('recipes.txt')
print(cook_book)  # Выведет словарь с рецептами

shopping_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2, cook_book)
print(shopping_list)  # Выведет список покупок

merge_files(['1.txt', '2.txt'], 'result.txt')  # Объединит файлы в result.txt