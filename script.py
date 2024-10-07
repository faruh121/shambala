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
        return "Индекс вне диапазона"

stroki = 10
stolbsi = 12
matrisa = сreate_matrca(stroki, stolbsi)

print("Сгенерированная матрица:")
for i in matrisa:
    print(i)


ind_stroki = int(input("Введите индекс строки: "))
ind_stolbsa = int(input("Введите индекс столбца: "))


elm = take_element(matrisa, ind_stroki, ind_stolbsa)
print(f"Элемент на позиции ({ind_stroki}, {ind_stolbsa}): {elm}")