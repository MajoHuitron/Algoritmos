def total_pressure(M1, M2, m1, m2, V, T):
    # Convertir temperatura de grados Celsius a Kelvin
    T_kelvin = T + 273.15

    # Constante de los gases
    R = 0.082  # dm^3 * atm / (mol * K)

    # Calcular la presión total usando la fórmula dada
    P_total = ((m1 / M1) + (m2 / M2)) * R * T_kelvin / V

    return P_total


# Probar la función con valores de ejemplo
M1 = 32  # g/mol
M2 = 28  # g/mol
m1 = 10  # g
m2 = 20  # g
V = 10  # dm^3
T = 25  # °C

print(total_pressure(M1, M2, m1, m2, V, T))  # Debería devolver la presión total en atm
