"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv


staff = [
    {
        'name': 'Anton',
        'age': '22',
        'job': 'Architect'
    },

    {
        'name': 'Ilya',
        'age': '20',
        'job': 'Designer'
    },

    {
        'name': 'Nastya',
        'age': '21',
        'job': 'Psychologist'
    },

    {
        'name': 'Arseny',
        'age': '25',
        'job': 'Manager'
    }
]


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('staff.csv', 'w', encoding='utf-8') as file:
        fields = ['name', 'age', 'job']

        writer = csv.DictWriter(file, fields, delimiter=';')
        writer.writeheader()
        writer.writerows(staff)


if __name__ == "__main__":
    main()
