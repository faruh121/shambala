# Написать код, который записывает матрицу от оператора и выводит элемент по зпросу индекса


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

stroki = 10
stolbsi = 12
matrisa = сreate_matrca(stroki, stolbsi)

print("Матрица:")
for i in matrisa:
    print(i)


ind_stroki = int(input("Индекс строки: "))
ind_stolbsa = int(input("Индекс столбца: "))


elm = take_element(matrisa, ind_stroki, ind_stolbsa)
print(f"Данный элемент находится на позиции ({ind_stroki}, {ind_stolbsa}): {elm}")