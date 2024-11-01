import random

# Параметры зала
rows = 6
seats = 12

# Создание зала
hall = [['о' for _ in range(seats)] for _ in range(rows)]

# Случайное занятие мест
for _ in range(random.randint(1, rows * seats // 3)):
    row = random.randint(0, rows - 1)
    seat = random.randint(0, seats - 1)
    hall[row][seat] = 'з'

# Вывод зала
print("Кинозал:")
for row in hall:
    print(' '.join(row))

# Запрос количества мест
num_seats = int(input("Введите количество необходимых рядом расположенных мест: "))

# Поиск доступных мест
found = False
for row in range(rows):
    for start_seat in range(seats - num_seats + 1):
        if all(hall[row][start_seat + i] == 'о' for i in range(num_seats)):
            print(f"Доступные места: Ряд {row + 1}, Места: {', '.join(map(str, range(start_seat + 1, start_seat + num_seats + 1)))}")
            found = True
            break
    if found:
        break

if not found:
    print("К сожалению, нет доступных мест для вашего запроса.")