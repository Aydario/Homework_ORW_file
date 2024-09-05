from pprint import pprint


def create_cook_book(file):
    cook_book = {}
    with open(file, 'r', encoding='utf-8') as f:
        for dish in f.read().split('\n\n'):
            name, total_ingredients, *ingredients = dish.split('\n')
            cook_book[name] = []
            for ingredient in ingredients:
                ingredient_name, quantity, measure = ingredient.split(' | ')
                cook_book[name].append({
                    'ingredient_name': ingredient_name,
                    'quantity': quantity,
                    'measure': measure
                })
    return cook_book

pprint(create_cook_book('1.task_1\cook_book.txt'))
