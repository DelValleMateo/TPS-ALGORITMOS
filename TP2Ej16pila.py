def interseccion_pilas(pila1, pila2):
    interseccion = []
    temp_pila = []

    while pila1:
        temp_pila.append(pila1.pop())

    while temp_pila:
        elemento = temp_pila.pop()
        if elemento in pila2:
            interseccion.append(elemento)

    return interseccion

pila_episodio_v = ["Luke Skywalker", "Princess Leia", "Han Solo", "Darth Vader"]
pila_episodio_vi = ["Rey", "Finn", "Kylo Ren", "Poe Dameron", "Han Solo"]

resultado_interseccion = interseccion_pilas(pila_episodio_v, pila_episodio_vi)

print("Intersección de pilas:", resultado_interseccion)
