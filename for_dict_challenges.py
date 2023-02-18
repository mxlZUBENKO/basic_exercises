# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]


names = {}
for student in students:
    name = student['first_name']
    if names.get(name) == None:
        names[name] = 1
    else:
        names[name] += 1
for i in names:
    print(f'{i}: {names[i]}')

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]


names = {}
for student in students:
    name = student['first_name']
    if names.get(name) == None:
        names[name] = 1
    else:
        names[name] += 1
max_number_repetitions = max(names.values())
for i in names:
    if names[i] == max_number_repetitions:
        print(f'Самое частое имя среди учеников: {i}')


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]


class_counter = 1
for grade in school_students:
    names = {}
    for student in grade:
        name = student['first_name']
        if names.get(name) == None:
            names[name] = 1
        else:
            names[name] += 1
    max_number_repetitions = max(names.values())
    for i in names:
        if names[i] == max_number_repetitions:
            print(f'Самое частое имя в классе {class_counter}: {i}')
    class_counter += 1


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}


for grade in school:
    boys = girls = 0
    name_grade = grade['class']
    for student in grade['students']:
        if is_male[student['first_name']] == True:
            boys += 1
        else:
            girls += 1
    print(f'Класс {name_grade}: мальчики {boys}, девочки {girls}')

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}


boy = {}
girl = {}
for grade in school:
    boys = girls = 0
    name_grade = grade['class']
    for student in grade['students']:
        if is_male[student['first_name']] == True:
            boys += 1
        else:
            girls += 1
    boy[name_grade] = boys
    girl[name_grade] = girls


max_boy = max(boy.values())
max_girl = max(girl.values())
for i in boy:
    if boy[i] == max_boy:
        print(f'Больше всего мальчиков в классе {i}')
for i in girl:
    if girl[i] == max_girl:
        print(f'Больше всего девочек в классе {i}')
