def usd_to_cny(usd):
    # Tasa de conversión de USD a CNY
    conversion_rate = 6.75

    # Convertir USD a CNY
    cny = usd * conversion_rate

    # Devolver el resultado como string formateado con 2 decimales
    return f"{cny:.2f} Chinese Yuan"


# Probar la función con ejemplos
print(usd_to_cny(15))  # Debería devolver '101.25 Chinese Yuan'
print(usd_to_cny(465))  # Debería devolver '3138.75 Chinese Yuan'
