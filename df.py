# def lagrange(x, x_values, y_values):
#     n = len(x_values)
#     result = 0
#     for i in range(n):
#         term = y_values[i]
#         for j in range(n):
#             if i != j:
#                 term *= (x - x_values[j]) / (x_values[i] - x_values[j])
#         result += term
#     return result



def lagrange(x, x_values, y_values):
    n = len(x_values)
    result = 0
    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if i != j:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term
    return result

# Данные из задачи
x_values = [0.27, 0.93, 1.46, 2.11, 2.87]
y_values = [2.60, 2.43, 2.06, 0.25, -2.60]

# Точки, в которых нужно найти значения функции
points = [1.02, 0.65, 1.28]

# Расчет значений
results = {x: lagrange(x, x_values, y_values) for x in points}
print(results)
