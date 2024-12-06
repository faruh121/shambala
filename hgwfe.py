def add_nambers(**kwargs):
    return sum(kwargs.values())


result = add_nambers(a=5, b=10, c=15)
print(result)  # 30