# Написать код, который записывает матрицу от пользователя и выводит элемент по зпросу индекса реализовать метод зендаля

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

# Ввод индексов для получения элемента
try:
    ind_stroki = int(input("Индекс строки: "))
    ind_stolbsa = int(input("Индекс столбца: "))
except ValueError:
    print("Ошибка ввода. Пожалуйста, введите целые числа.")
    exit()

elm = take_element(matrisa, ind_stroki, ind_stolbsa)
print(f"Данный элемент находится на позиции ({ind_stroki}, {ind_stolbsa}): {elm}")