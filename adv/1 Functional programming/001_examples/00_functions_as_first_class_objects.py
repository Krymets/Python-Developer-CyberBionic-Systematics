﻿"""Приклад роботи з функціями як з об'єктами першого класу"""

# Створення посилання на об'єкт
out = print

# Тепер у змінних out і print посилання на той самий алгоритм,
# тому ми можемо використовувати out так само, як і print
out('Hello')

# Збереження посилань на функції у структурі даних


def add(x, y):
    return x + y


def sub(x, y):
    return x - y

# Використовуємо функції всередині словника як звичайні змінні
# ВАЖЛИВО: Після add і sub не стоять дужки "()", тому що наше завдання передати їх
# як змінні, а не викликати


operations = {
    '+': add,
    '-': sub
}

# За ключом словника отримуємо повноцінну функцію, яку одразу можна викликати
print(operations['+'](2, 3))
print(operations['-'](2, 3))
out()
out(operations['+'](2, 3))
out(operations['-'](2, 3))