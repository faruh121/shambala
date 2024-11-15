cena_bukv = {
    'A': 1, 'B': 1, 'C': 1,
    'D': 2, 'E': 2, 'F': 2,
    'G': 3, 'H': 3, 'I': 3,
    'J': 4, 'K': 4, 'L': 4,
    'M': 5, 'N': 5, 'O': 5,
    'P': 6, 'Q': 6, 'R': 6,
    'S': 7, 'T': 7, 'U': 7,
    'V': 8, 'W': 8, 'X': 8,
    'Y': 9, 'Z': 9
}

a = input("Введите текст: ")


for i in ".,!?":
    a = a.replace(i, "")


slova = a.split()


max_ochki = 0
samoedorogslovo = ""


for i in slova:
    ochki = sum(cena_bukv.get(b, 0) for b in i)  
    if ochki > max_ochki:  
        max_ochki = ochki
        samoedorogslovo = i  


print("Самое дорогое слово:", samoedorogslovo, "с количеством очков:", max_ochki)
