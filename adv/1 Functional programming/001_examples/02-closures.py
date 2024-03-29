﻿"""Приклад замикання"""


def make_closure():
    # Створили змінну
    variable = 42

    # Створили функцію, яка має доступ до змінної батьківської функції
    def closure():
        return variable

    # Повернули створену функцію з батьківської
    return closure


# Ми вже дізналися, що ми можемо зберігати функції у звичайних змінних. Зберігаємо отриману функцію змінну fn
fn = make_closure()

# Запускаємо отриману функцію та виводимо її результат
print(fn)
print(fn())
print(type(fn))
