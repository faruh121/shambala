from scipy.stats import binom

def probability_headphones_failure(n, p):
    k = int(0.3 * n)  # количество наушников, которые должны выйти из строя
    return binom.pmf(k, n, p)

# Пример использования
n = 1000  # количество наушников в партии
p = 0.005  # вероятность выхода из строя одного наушника
result = probability_headphones_failure(n, p)
print(f"Вероятность того, что 30% партии выйдет из строя:", result)

