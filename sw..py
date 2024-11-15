import random

# Создаем список из 5 случайных чисел в диапазоне [-100, 100]
numbers = [random.randint(-100, 100) for _ in range(5)]

# Находим сумму отрицательных элементов
negative_sum = sum(num for num in numbers if num < 0)

# Выводим результат
print("Список случайных чисел:", numbers)
if negative_sum < 0:
    print("Сумма отрицательных элементов:", negative_sum)
else:
    print("Отрицательных элементов нет")
