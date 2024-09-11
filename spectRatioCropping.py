import math


def convert_to_16_9(x, y):
    # 16:9 aspect ratio significa que el ancho/alto = 16/9
    aspect_ratio = 16 / 9

    # Calcular el nuevo ancho (x) basado en la altura (y) y la relación de aspecto
    new_x = math.ceil(y * aspect_ratio)

    return new_x, y


# Probar la función con el ejemplo dado (374 x 280)
original_x, original_y = 374, 280
new_resolution = convert_to_16_9(original_x, original_y)
print(f"Nueva resolución: {new_resolution[0]} x {new_resolution[1]}")
