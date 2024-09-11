def nba_extrap(ppg, mpg):
    # Si minutos por juego es 0, devolvemos 0 para evitar división por cero
    if mpg == 0:
        return 0

    # Extrapolamos los puntos por 48 minutos
    extrapolated_ppg = (ppg / mpg) * 48

    # Redondeamos el resultado al décimo más cercano
    return round(extrapolated_ppg, 1)


# Probar la función con ejemplos
print(nba_extrap(12, 20))  # Debería devolver 28.8
print(nba_extrap(10, 10))  # Debería devolver 48
print(nba_extrap(5, 17))  # Debería devolver 14.1
print(nba_extrap(0, 0))  # Debería devolver 0
