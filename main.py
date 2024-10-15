def checarr(t):
    if not t:  
        return True
    return all(x == t[0] for x in t)

# Примеры использования
print(checarr((1, 1, 1)))  # True
print(checarr((1, 2, 1)))  # False
print(checarr(()))  