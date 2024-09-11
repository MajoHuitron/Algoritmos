import math

def litres_drunk(time):
    # Nathan bebe 0.5 litros por hora, y redondeamos hacia abajo al número entero más pequeño
    return math.floor(time * 0.5)

# Probar la función con ejemplos
print(litres_drunk(3))     # Debería devolver 1
print(litres_drunk(6.7))   # Debería devolver 3
print(litres_drunk(11.8))  # Debería devolver 5
