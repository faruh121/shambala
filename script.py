# Написать код, который записывает матрицу от пользователя и выводит элемент по зпросу индекса реализовать метод зендаля

import numpy as np

def сreate_matrca(stroki, stolbsi):
    matrisa = []
    for i in range(stroki):
        stroka = []
        for j in range(stolbsi):
            stroka.append(i * stolbsi + j) 
        matrisa.append(stroka)
    return matrisa

def take_element(matrisa, ind_stroki, ind_stolbsa):
    try:
        return matrisa[ind_stroki][ind_stolbsa]
    except IndexError:
        return "Введенный индекс находится вне диапазона"

def check_convergence(a):
    n = len(a)
    for i in range(n):
        diag = abs(a[i][i])
        sum_ot = sum(abs(a[i][j]) for j in range(n) if j != i)
        if diag < sum_ot:
            print("Матрица не сходится")
            return False
    return True

def gauss_seidel(a, b, max_iterations=100, tolerance=1e-10):
    n = len(a)
    x = np.zeros(n)
    
    for iteration in range(max_iterations):
        x_new = np.copy(x)
        for i in range(n):
            sum1 = sum(a[i][j] * x_new[j] for j in range(i))
            sum2 = sum(a[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - sum1 - sum2) / a[i][i]
        
        # Проверка сходимости
        if np.linalg.norm(x_new - x, ord=np.inf) < tolerance:
            print(f"Решение найдено за {iteration + 1} итераций.")
            return x_new
        
        x = x_new
    
    print("Достигнуто максимальное количество итераций.")
    return x

# Ввод размеров матрицы
try:
    stroki = int(input("Введите количество строк: "))
    stolbsi = int(input("Введите количество столбцов: "))
except ValueError:
    print("Ошибка ввода. Пожалуйста, введите целые числа.")
    exit()

matrisa = сreate_matrca(stroki, stolbsi)
print("Матрица:")
for i in matrisa:
    print(i)

# Ввод коэффициентов b
b = []
for i in range(stroki):
    b.append(int(input(f"Введите свободный член для уравнения {i + 1}: ")))

# Проверка сходимости
if check_convergence(matrisa):
    solution = gauss_seidel(matrisa, b)
    print("Решение системы уравнений:", solution)