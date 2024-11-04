def hash_tipo(tipo):
    return tipo


def hash_ultimo_digito(numero):
    return int(numero) % 10


def hash_nivel(nivel):
    return int(nivel) // 10


tabla_tipo = {}
tabla_ultimo_digito = {}
tabla_nivel = {}


def agregar_pokemon(numero, nombre, tipos, nivel):
    for tipo in tipos:
        if hash_tipo(tipo) not in tabla_tipo:
            tabla_tipo[hash_tipo(tipo)] = []
        tabla_tipo[hash_tipo(tipo)].append((numero, nombre, tipos, nivel))

    if hash_ultimo_digito(numero) not in tabla_ultimo_digito:
        tabla_ultimo_digito[hash_ultimo_digito(numero)] = []
    tabla_ultimo_digito[hash_ultimo_digito(numero)].append(
        (numero, nombre, tipos, nivel))

    if hash_nivel(nivel) not in tabla_nivel:
        tabla_nivel[hash_nivel(nivel)] = []
    tabla_nivel[hash_nivel(nivel)].append((numero, nombre, tipos, nivel))


def mostrar_pokemons_por_digito(digitos):
    resultado = []
    for digito in digitos:
        if digito in tabla_ultimo_digito:
            resultado.append(tabla_ultimo_digito[digito])
    return resultado


def mostrar_pokemons_por_nivel(niveles):
    resultado = []
    for nivel in niveles:
        if nivel in tabla_nivel:
            resultado.append(tabla_nivel[nivel])
    return resultado


def mostrar_pokemons_por_tipo(tipos):
    resultado = []
    for tipo in tipos:
        if tipo in tabla_tipo:
            resultado.append(tabla_tipo[tipo])
    return resultado


pokemons = [
    ("001", "Bulbasaur", ["Planta", "Veneno"], 5),
    ("004", "Charmander", ["Fuego"], 10),
    ("007", "Squirtle", ["Agua"], 7),
    ("025", "Pikachu", ["Eléctrico"], 15),
    ("087", "Dewgong", ["Agua", "Hielo"], 20),
    ("149", "Dragonite", ["Dragón", "Volador"], 30),
    ("198", "Murkrow", ["Siniestro", "Volador"], 10),
    ("437", "Bronzong", ["Acero", "Psíquico"], 25),
    ("479", "Rotom", ["Eléctrico", "Fantasma"], 35)
]

for pokemon in pokemons:
    agregar_pokemon(*pokemon)

print("Pokémon cuyos números terminan en 3, 7 y 9:")
for pokemon in mostrar_pokemons_por_digito([3, 7, 9]):
    print(pokemon)

print("\nPokémon cuyos niveles son múltiplos de 2, 5 y 10:")
for pokemon in mostrar_pokemons_por_nivel([2, 5, 10, 20, 25, 30, 35, 40, 45, 50]):
    print(pokemon)

print("\nPokémon de los tipos Acero, Fuego, Eléctrico, Hielo:")
for pokemon in mostrar_pokemons_por_tipo(["Acero", "Fuego", "Eléctrico", "Hielo"]):
    print(pokemon)
