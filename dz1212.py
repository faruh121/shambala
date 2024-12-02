# Исходный словарь
slovar = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value1",  # Дубликат значения
    "key4": "value3",
    "key5": "value2",  # Дубликат значения
}

# Новый словарь для хранения уникальных элементов
slovar_1 = {}

# Итерация по исходному словарю
for i, a in slovar.items():
    if a not in slovar_1.values():
        slovar_1[i] = a

# Вывод результата
print("Исходный словарь:", slovar)
print("Словарь без дубликатов:", slovar_1)
