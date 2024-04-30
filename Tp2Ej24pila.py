def posicion_personaje(pila, nombre_personaje):
    posicion = None
    temp_pila = []

    while pila:
        personaje = pila.pop()
        temp_pila.append(personaje)
        if personaje[0] == nombre_personaje:
            posicion = len(temp_pila)

    # Restaurar la pila original
    while temp_pila:
        pila.append(temp_pila.pop())

    return posicion

def personajes_mas_de_cinco_peliculas(pila):
    personajes = []
    for personaje in pila:
        if personaje[1] > 5:
            personajes.append(personaje)
    return personajes

def cantidad_peliculas_personaje(pila, nombre_personaje):
    for personaje in pila:
        if personaje[0] == nombre_personaje:
            return personaje[1]
    return 0 

def personajes_por_inicial(pila, iniciales):
    personajes = []
    for personaje in pila:
        if personaje[0][0].upper() in iniciales:
            personajes.append(personaje[0])
    return personajes

pila_personajes = [("Iron Man", 7), ("Captain America", 6), ("Black Widow", 6),
                   ("Thor", 5), ("Hulk", 4), ("Rocket Raccoon", 3), ("Groot", 3),
                   ("Doctor Strange", 3), ("Black Panther", 2), ("Spider-Man", 4)]

print("Posición de Rocket Raccoon:", posicion_personaje(pila_personajes.copy(), "Rocket Raccoon"))
print("Posición de Groot:", posicion_personaje(pila_personajes.copy(), "Groot"))

print("Personajes que participaron en más de 5 películas:", personajes_mas_de_cinco_peliculas(pila_personajes.copy()))

print("Cantidad de películas de Black Widow:", cantidad_peliculas_personaje(pila_personajes.copy(), "Black Widow"))

print("Personajes con nombre que empieza con C, D o G:", personajes_por_inicial(pila_personajes.copy(), ['C', 'D', 'G']))
