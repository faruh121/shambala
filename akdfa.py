def lagrange_interpolation(x_points, y_points, x):

    result = 0.0
    n = len(x_points)
    
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if i != j:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        result += term
        
    return result

# Данные таблицы
x_points = [0.27, 0.93, 1.46, 2.11, 2.87]
y_points = [2.60, 2.43, 2.06, 0.25, -2.60]

# Задание 2
x_a = 1.02
x_b = 2.34
f_a = lagrange_interpolation(x_points, y_points, x_a)
f_b = lagrange_interpolation(x_points, y_points, x_b)
print(f"Значение функции в точке x = {x_a}: {f_a}")
print(f"Значение функции в точке x = {x_b}: {f_b}")

# Задание 4
# a) x = 1.02 и x = 0.65
x_a1 = 1.02
x_a2 = 0.65
f_a1 = lagrange_interpolation(x_points, y_points, x_a1)
f_a2 = lagrange_interpolation(x_points, y_points, x_a2)
print(f"Значение функции в точке x = {x_a1}: {f_a1}")
print(f"Значение функции в точке x = {x_a2}: {f_a2}")

# b) x = 1.28
x_b1 = 1.28
f_b1 = lagrange_interpolation(x_points, y_points, x_b1)
print(f"Значение функции в точке x = {x_b1}: {f_b1}")