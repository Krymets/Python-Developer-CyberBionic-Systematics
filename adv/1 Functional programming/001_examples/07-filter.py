﻿"""Приклад використання функції filter"""

numbers = [3, 2, -1, 0, 15, -8, -7, 3, -3, 8]
positive_numbers = filter(lambda x: x > 0, numbers)
print(positive_numbers)
print(type(positive_numbers))
print(list(positive_numbers))
print(type(positive_numbers))
