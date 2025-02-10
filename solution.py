def quadratic_solve(a, b, c):
    return f"Solving for a={a}, b={b}, c={c}"

params = {"a": 1, "b": -3, "c": 2}
print(quadratic_solve(**params))  # Правильное использование ** для распаковки словаря
