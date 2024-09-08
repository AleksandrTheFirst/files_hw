import operator
import os


# Задача 1
with open('recipes.txt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        recipe_name = line.strip()
        ingredients_count = file.readline()
        ingredients = []
        for p in range(int(ingredients_count)):
            recipe = file.readline().strip().split(' | ')
            name, quantity, chars = recipe
            ingredients.append({'name': name, 'quantity': quantity, 'measure': chars})
        file.readline()
        cook_book[recipe_name] = ingredients

def get_shop_list_by_dishes(dishes, person_count):
    result_dict = {}
    for dish in dishes:         # идем по списку dishes
        if dish in cook_book:   # если блюдо есть в cook_book
            for one_list in cook_book[dish]:        # идем по списку ингредиентов блюда
                if one_list['name'] in result_dict:      # если ингредиент уже в итоговом списке
                    result_dict[one_list['name']]['quantity'] += int(one_list['quantity']) * person_count  #обновляем значение количества
                else:  # иначе записываем имя ингредиента со списком = ед.изм. * кол-во персон
                    result_dict[one_list['name']] = {'measure': one_list['measure'],'quantity': (int(one_list['quantity']) * person_count) }
        else:
            print('Такого блюда нет в меню')
    print(result_dict)


# Задача 2
def create_file_from_files(files: list):
    if not isinstance(files, list):
        raise ValueError('Путь должен быть задан списком.')
    if not files:
        raise ValueError('Пустой список файлов.')
    tmp_dict = create_sorted_dict(files)
    file_path = f'{os.getcwd()}\\files\\file_to_write.txt'
    str_count = 1
    file_w = open(f'{file_path}', 'w', encoding='utf-8')
    for file_name in tmp_dict.keys():
        file_r = open(f'{os.getcwd()}\\files\\{file_name}', 'r', encoding='utf-8')
        file_w.write(file_name + '\n')
        file_w.write(str(tmp_dict[file_name]) + '\n')
        for string in file_r:
            if str_count == tmp_dict[file_name]:
                file_w.write(f'Строка {str_count} файла {file_name} - {string}\n')
            else:
                file_w.write(f'Строка {str_count} файла {file_name} - {string}')
            str_count += 1
        file_r.close()
        str_count = 1
    file_w = open(f'{file_path}', 'r', encoding='utf-8')
    print(file_w.read())
    file_w.close()
    file_w.close()


# Задача 3
def create_sorted_dict(files):
    tmp_dict = {}
    for file_ in sorted(files):
        file_path = f'{os.getcwd()}\\files\\{file_}'
        tmp_list = []
        with open(file_path, encoding='utf-8') as file:
            for i in file:
                tmp_list.append(i.split('\\n'))
            tmp_dict.setdefault(file_, len(tmp_list))
    sorted_dict = sorted(tmp_dict.items(), key=operator.itemgetter(1))
    return dict(sorted_dict)




files_list = ['1.txt', '2.txt', '3.txt']
create_file_from_files(files_list)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2 )