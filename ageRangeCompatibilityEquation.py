import math


def dating_range(age):
    if age > 14:
        # Fórmula cuando la edad es mayor que 14
        min_age = math.floor(age / 2 + 7)
        max_age = math.floor((age - 7) * 2)
    else:
        # Fórmula cuando la edad es menor o igual a 14
        min_age = math.floor(age - 0.10 * age)
        max_age = math.floor(age + 0.10 * age)

    return f"{min_age}-{max_age}"


# Probar la función con ejemplos
print(dating_range(27))  # Debería devolver '20-40'
print(dating_range(5))  # Debería devolver '4-5'
print(dating_range(17))  # Debería devolver '15-20'
