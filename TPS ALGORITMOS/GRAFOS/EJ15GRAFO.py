# 15. Se requiere implementar un grafo para almacenar las siete maravillas arquitectónicas moder-
# nas y naturales del mundo, para lo cual se deben tener en cuenta las siguientes actividades:

# a. de cada una de las maravillas se conoce su nombre, país de ubicación (puede ser más de
# uno en las naturales) y tipo (natural o arquitectónica);
# b. cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar
# la distancia que las separa;
# c. hallar el árbol de expansión mínimo de cada tipo de las maravillas;
# d. determinar si existen países que dispongan de maravillas arquitectónicas y naturales;
# e. determinar si algún país tiene más de una maravilla del mismo tipo;
# f. deberá utilizar un grafo no dirigido.

from grafo import Graph


# a. Crear un grafo para almacenar las maravillas
# f. deberá utilizar un grafo no dirigido.
grafo = Graph(dirigido=False)

maravillas = [
    {"nombre": "Machu Picchu", "pais": ["Perú"], "tipo": "arquitectonica"},
    {"nombre": "Chichén Itzá", "pais": ["México"], "tipo": "arquitectonica"},
    {"nombre": "Cristo Redentor", "pais": [
        "Brasil"], "tipo": "arquitectonica"},
    {"nombre": "Coliseo de Roma", "pais": [
        "Italia"], "tipo": "arquitectonica"},
    {"nombre": "Taj Mahal", "pais": ["India"], "tipo": "arquitectonica"},
    {"nombre": "Gran Muralla China", "pais": [
        "China"], "tipo": "arquitectonica"},
    {"nombre": "Petra", "pais": ["Jordania"], "tipo": "arquitectonica"},
    {"nombre": "Gran Cañón", "pais": ["Estados Unidos"], "tipo": "natural"},
    {"nombre": "Aurora Boreal", "pais": [
        "Canadá", "Noruega", "Finlandia"], "tipo": "natural"},
    {"nombre": "Parque Nacional de Komodo",
        "pais": ["Indonesia"], "tipo": "natural"},
    {"nombre": "Monte Everest", "pais": ["Nepal", "China"], "tipo": "natural"},
    {"nombre": "Cataratas del Iguazú", "pais": [
        "Argentina", "Brasil"], "tipo": "natural"},
    {"nombre": "Isla Jeju", "pais": ["Corea del Sur"], "tipo": "natural"},
    {"nombre": "Montaña de la Mesa", "pais": ["Sudáfrica"], "tipo": "natural"},
    # Otra maravilla arquitectónica en Brasil para el ultimo punto
    {"nombre": "Otro Monumento", "pais": ["Brasil"], "tipo": "arquitectonica"}
]

for maravilla in maravillas:
    grafo.insert_vertice(maravilla["nombre"])

# Ahora declaramos la relaciones entre maravillas (aristas) donde esta el inicio-destino-distancia
relaciones = [
    ("Machu Picchu", "Chichén Itzá", 4190), ("Machu Picchu", "Cristo Redentor", 3320),
    ("Machu Picchu", "Coliseo de Roma", 10570), ("Machu Picchu", "Taj Mahal", 17240),
    ("Machu Picchu", "Gran Muralla China", 17980), ("Machu Picchu", "Petra", 12890),
    ("Chichén Itzá", "Cristo Redentor",
     6610), ("Chichén Itzá", "Coliseo de Roma", 9320),
    ("Chichén Itzá", "Taj Mahal", 14440), ("Chichén Itzá", "Gran Muralla China", 12300),
    ("Chichén Itzá", "Petra", 11720), ("Cristo Redentor", "Coliseo de Roma", 9160),
    ("Cristo Redentor", "Taj Mahal",
     14050), ("Cristo Redentor", "Gran Muralla China", 17590),
    ("Cristo Redentor", "Petra", 12150), ("Coliseo de Roma", "Taj Mahal", 5960),
    ("Coliseo de Roma", "Gran Muralla China",
     8180), ("Coliseo de Roma", "Petra", 2320),
    ("Taj Mahal", "Gran Muralla China", 3210), ("Taj Mahal", "Petra", 4310),
    ("Gran Muralla China", "Petra", 6840), ("Gran Cañón", "Aurora Boreal", 3500),
    ("Gran Cañón", "Parque Nacional de Komodo",
     13800), ("Gran Cañón", "Monte Everest", 12400),
    ("Gran Cañón", "Cataratas del Iguazú",
     8230), ("Gran Cañón", "Isla Jeju", 10390),
    ("Gran Cañón", "Montaña de la Mesa", 16130), ("Aurora Boreal",
                                                  "Parque Nacional de Komodo", 10120),
    ("Aurora Boreal", "Monte Everest",
     6170), ("Aurora Boreal", "Cataratas del Iguazú", 10920),
    ("Aurora Boreal", "Isla Jeju", 6980), ("Aurora Boreal", "Montaña de la Mesa", 13440),
    ("Parque Nacional de Komodo", "Monte Everest",
     5470), ("Parque Nacional de Komodo", "Cataratas del Iguazú", 16900),
    ("Parque Nacional de Komodo", "Isla Jeju",
     3980), ("Parque Nacional de Komodo", "Montaña de la Mesa", 11070),
    ("Monte Everest", "Cataratas del Iguazú",
     16350), ("Monte Everest", "Isla Jeju", 4750),
    ("Monte Everest", "Montaña de la Mesa",
     9430), ("Cataratas del Iguazú", "Isla Jeju", 18560),
    ("Cataratas del Iguazú", "Montaña de la Mesa",
     8420), ("Isla Jeju", "Montaña de la Mesa", 13220)
]


for origen, destino, distancia in relaciones:
    grafo.insert_arista(origen, destino, distancia)

# c. hallar el árbol de expansión mínimo de cada tipo de las maravillas;

# Creamos dos subgrafos para poder dividir los tipos de maravillas
grafo_natural = Graph(dirigido=False)
grafo_arquitectonico = Graph(dirigido=False)


def tipo_arbol(nombre, maravillas):
    for i in maravillas:
        if i["nombre"] == nombre:
            return i["tipo"]
    return None


for maravilla in maravillas:
    nombre = maravilla["nombre"]
    tipo = maravilla["tipo"]
    if tipo == "natural":
        grafo_natural.insert_vertice(nombre)
    elif tipo == "arquitectonica":
        grafo_arquitectonico.insert_vertice(nombre)

for origen, destino, distancia in relaciones:
    tipo_origen = tipo_arbol(origen, maravillas)
    tipo_destino = tipo_arbol(destino, maravillas)
    if tipo_origen == "natural" and tipo_destino == "natural":
        grafo_natural.insert_arista(origen, destino, distancia)
    elif tipo_origen == "arquitectonica" and tipo_destino == "arquitectonica":
        grafo_arquitectonico.insert_arista(origen, destino, distancia)


arbol_natural = grafo_natural.kruskal("Cataratas del Iguazú")
arbol_arquitectonico = grafo_arquitectonico.kruskal("Cristo Redentor")

print("----------------------------------------------------------------")
print("Punto C")
print("")
print("Árbol de expansión mínimo para las maravillas naturales:")
print("")
print(arbol_natural)

print("")
print("Arbol de expansion minima para las maravillas arquitectonicas:")
print("")
print(arbol_arquitectonico)
print("")
print("----------------------------------------------------------------")
# d. determinar si existen países que dispongan de maravillas arquitectónicas y naturales;
print("Punto D")
pais_maravillas = {}

for maravilla in maravillas:
    for pais in maravilla["pais"]:
        if pais not in pais_maravillas:
            # se utiliza el set para que se eviten los duplicados
            pais_maravillas[pais] = set()
        pais_maravillas[pais].add(maravilla["tipo"])

# Determinar países con maravillas de ambos tipos
paises_ambos_tipos = [pais for pais,
                      tipos in pais_maravillas.items() if len(tipos) > 1]

print("")
print("Los paises que tienen maravillas tanto naturales como arquitectonicas son:")
print("")
print(paises_ambos_tipos)
print("")
print("----------------------------------------------------------------")
# e. determinar si algún país tiene más de una maravilla del mismo tipo;
print("Punto E")
print("")
pais_maravillas_conteo = {}

# Recorrido de las maravillas
for maravilla in maravillas:
    tipo = maravilla["tipo"]
    for pais in maravilla["pais"]:
        if pais not in pais_maravillas_conteo:
            pais_maravillas_conteo[pais] = {"natural": 0, "arquitectonica": 0}

        pais_maravillas_conteo[pais][tipo] += 1

# Verificamos si un pais tiene mas de una maravilla del mismo tipo
for pais, tipos in pais_maravillas_conteo.items():
    for tipo, conteo in tipos.items():
        if conteo > 1:
            print(
                f"El país {pais} tiene más de una maravilla de tipo {tipo} ({conteo} maravillas).")
print("")
