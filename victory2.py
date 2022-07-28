"""
В проекте создать новый модуль victory.py. Задание
Написать или улучшить программу Викторина из предыдущего дз (Для тренировки предлагаю не пользоваться никакими библиотеками кроме random)
Есть 10 известных людей и их даты рождения в формате '02.01.1988' ('dd.mm.yyyy') - предлагаю для тренировки пока использовать строку
Программа выбирает из этих 10-и 5 случайных людей, это можно реализовать с помощью модуля random и функции sample
Пример использования sample:
import random
numbers = [1, 2, 3, 4, 5]

# 2 - количество случайных элементов
result = random.sample(numbers, 2)

print(result) # [5, 1]

После того как выбраны 5 случайных людей, предлагаем пользователю ввести их дату рождения
пользователь вводит дату в формате 'dd.mm.yyyy'

Например 03.01.2009, если пользователь ответил неверно, то выводим правильный ответ, но уже в следующем виде: третье января 2009 года, склонением можно пренебречь

В конце считаем количество правильных и неправильных ответов и предлагаем начать снова
"""

import random
print('Играем в викторину. Угадайте даты рождения известных личностей')
#словарь личностей и дат рождения
people_dates = {
    'Пушкин':'06.06.1799',
    'Эйнштейн':'14.03.1879',
    'Илон Маск':'28.06.1971',
    'Леонардо да Винчи':'15.04.1452',
    'Дэвиг Гарретт':'04.09.1980',
    'Билл Гейтс':'28.10.1955',
    'Чайковский':'07.05.1840'
    }

#посторяем тест - 1, нет - 0
repeat = 1
while repeat != 0:
    #используем список
    random_dict = random.sample(list(people_dates.keys()),3)
    print(random_dict)
    # накопитель баллов
    score = 0
    for i in random_dict:
        print(i)
        answer = input('Ваша дата:')
        if answer == people_dates[i]:
            score += 1
            print ('Верно')
        else:
            print('Неверно')
    print('Ваш счет', round(score / len(random_dict) * 100),'%')
    print('Повторим викторину? да или нет?')
    answer_repeat = input()
    if answer_repeat == 'да' or answer_repeat == 'Да':
        repeat = 1
    else:
        repeat = 0
print('Спасибо за участие')






