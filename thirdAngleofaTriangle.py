def find_third_angle(angle1, angle2):
    # La suma de los ángulos en cualquier triángulo es siempre 180 grados
    return 180 - (angle1 + angle2)

# Probar la función con un ejemplo
print(find_third_angle(60, 60))  # Debería devolver 60
