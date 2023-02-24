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

def number_of_times_of_name(students):
    names = {}
    for student in students:
        name = student['first_name']
        names[name] = names.get(name, 0) + 1
    return names

for repetition_rate in number_of_times_of_name(students):
    print(f'{repetition_rate}: {number_of_times_of_name(students)[repetition_rate]}')

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

def most_common_name(students):
    max_number_repetitions = max(number_of_times_of_name(students).values())
    for repetition_rate in number_of_times_of_name(students):
        if number_of_times_of_name(students)[repetition_rate] == max_number_repetitions:
            return repetition_rate

print(f'Самое повторяющиеся имя: {most_common_name(students)}')

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
    print(f'Самое повторяющиеся имя в {class_counter} классе: {most_common_name(grade)}')
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

def number_of_boys_and_girls(grade):
    students = grade['students']
    gender = {'boys': 0, 'girls': 0}
    for student in students:
        name = student['first_name']
        if is_male[name] == True:
            gender['boys'] += 1
        else:
            gender['girls'] += 1
    return gender

for grade in school:
        number_of_boys = number_of_boys_and_girls(grade)['boys']
        number_of_girls = number_of_boys_and_girls(grade)['girls']
        name_grade = grade['class']
        print(f'Класс {name_grade}: девочки {number_of_girls}, мальчики {number_of_boys}')

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

max_boys = max_girls = 0
for grade in school:
    if max_boys < number_of_boys_and_girls(grade)['boys']:
        max_boys = number_of_boys_and_girls(grade)['boys']
        class_max_boys = grade['class']
    if max_girls < number_of_boys_and_girls(grade)['girls']:
        max_girls = number_of_boys_and_girls(grade)['girls']
        class_max_girls = grade['class']

print(f'Больше всего мальчиков в классе: {class_max_boys}\nБольше всего девочек в классе: {class_max_girls}')