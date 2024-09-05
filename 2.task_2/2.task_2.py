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
                    'quantity': int(quantity),
                    'measure': measure
                })
    return cook_book


def get_shop_list_by_dishes(dishes, person_count, file='2.task_2\cook_book.txt'):
    list_products = {}
    cook_book = create_cook_book(file)
    for dish in dishes:
        for ingredients in cook_book[dish]:
            if ingredients['ingredient_name'] not in list_products:
                list_products[ingredients['ingredient_name']] = {
                    'measure': ingredients['measure'],
                    'quantity': ingredients['quantity'] * person_count
                }
            else:
                list_products[ingredients['ingredient_name']]['quantity'] += \
                    ingredients['quantity'] * person_count
    return list_products

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
