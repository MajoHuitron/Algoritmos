def mango(quantity, price_per_mango):
    # Por cada 3 mangos, 1 es gratis, por lo que calculamos cuántos se pagan
    paid_mangoes = quantity - (quantity // 3)
    return paid_mangoes * price_per_mango

# Probar la función con ejemplos
print(mango(2, 3))  # Debería devolver 6
print(mango(3, 3))  # Debería devolver 6
print(mango(5, 3))  # Debería devolver 12
print(mango(9, 5))  # Debería devolver 30
