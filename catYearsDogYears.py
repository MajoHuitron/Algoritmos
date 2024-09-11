def calculate_pet_ages(human_years):
    # Inicializar los años para el gato y el perro
    if human_years == 1:
        cat_years = 15
        dog_years = 15
    elif human_years == 2:
        cat_years = 15 + 9
        dog_years = 15 + 9
    else:
        cat_years = 15 + 9 + (human_years - 2) * 4
        dog_years = 15 + 9 + (human_years - 2) * 5

    return [human_years, cat_years, dog_years]


# Prueba de la función con un ejemplo (3 años humanos)
print(calculate_pet_ages(3))
