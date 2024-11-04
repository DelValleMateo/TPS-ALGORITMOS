# Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, can-
# tidad de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. Y ade-
# más la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo. Se pide resolver

# las siguientes actividades utilizando lista de lista implementando las funciones necesarias:
# a. obtener la cantidad de Pokémons de un determinado entrenador;
# b. listar los entrenadores que hayan ganado más de tres torneos;

# [115]

# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
# d. mostrar todos los datos de un entrenador y sus Pokémos;
# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
# (tipo y subtipo);
# g. el promedio de nivel de los Pokémons de un determinado entrenador;
# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
# i. mostrar los entrenadores que tienen Pokémons repetidos;
# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Te-
# rrakion o Wingull;
# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
# como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
# deberán mostrar los datos de ambos;


entrenadores = [
    {
        "nombre": "Ash Ketchum",
        "torneos_ganados": 7,
        "batallas_perdidas": 50,
        "batallas_ganadas": 120,
        "pokemones": [
            {"nombre": "Pikachu", "nivel": 80, "tipo": "Eléctrico", "subtipo": None},
            {"nombre": "Bulbasaur", "nivel": 65,
                "tipo": "Planta", "subtipo": "Veneno"},
            {"nombre": "Squirtle", "nivel": 60, "tipo": "Agua", "subtipo": None},
            {"nombre": "Greninja", "nivel": 90,
                "tipo": "Agua", "subtipo": "Siniestro"}
        ]
    },
    {
        "nombre": "Goh",
        "torneos_ganados": 2,
        "batallas_perdidas": 10,
        "batallas_ganadas": 40,
        "pokemones": [
            {"nombre": "Cinderace", "nivel": 75, "tipo": "Fuego", "subtipo": None},
            {"nombre": "Flygon", "nivel": 70, "tipo": "Tierra", "subtipo": "Dragón"},
            {"nombre": "Golurk", "nivel": 65,
                "tipo": "Tierra", "subtipo": "Fantasma"},
            {"nombre": "Sobble", "nivel": 50, "tipo": "Agua", "subtipo": None},
            {"nombre": "Scyther", "nivel": 60, "tipo": "Bicho", "subtipo": "Volador"}
        ]
    },
    {
        "nombre": "Leon",
        "torneos_ganados": 10,
        "batallas_perdidas": 5,
        "batallas_ganadas": 100,
        "pokemones": [
            {"nombre": "Charizard", "nivel": 100,
                "tipo": "Fuego", "subtipo": "Volador"},
            {"nombre": "Rillaboom", "nivel": 85,
                "tipo": "Planta", "subtipo": None},
            {"nombre": "Haxorus", "nivel": 88, "tipo": "Dragón", "subtipo": None}
        ]
    },
    {
        "nombre": "Chloe",
        "torneos_ganados": 1,
        "batallas_perdidas": 8,
        "batallas_ganadas": 30,
        "pokemones": [
            {"nombre": "Eevee", "nivel": 45, "tipo": "Normal", "subtipo": None},
            {"nombre": "Espeon", "nivel": 55, "tipo": "Psíquico", "subtipo": None}
        ]
    },
    {
        "nombre": "Raihan",
        "torneos_ganados": 4,
        "batallas_perdidas": 15,
        "batallas_ganadas": 60,
        "pokemones": [
            {"nombre": "Duraludon", "nivel": 85,
                "tipo": "Acero", "subtipo": "Dragón"},
            {"nombre": "Flygon", "nivel": 80, "tipo": "Tierra", "subtipo": "Dragón"},
            {"nombre": "Garchomp", "nivel": 85,
                "tipo": "Dragón", "subtipo": "Tierra"},
            {"nombre": "Togekiss", "nivel": 75,
                "tipo": "Hada", "subtipo": "Volador"},
            {"nombre": "Tyranitar", "nivel": 82,
                "tipo": "Roca", "subtipo": "Siniestro"}]
    }
]

# a. obtener la cantidad de Pokémons de un determinado entrenador;
print("-----------------------------------------------------------------------------------------------------------------------")
print("PUNTO A")
print(" ")


def cantidad_pokemones():
    cantidad_pokemon = 0
    for entrenador in entrenadores:
        if 'pokemones' in entrenador:
            for pokemon in entrenador['pokemones']:
                cantidad_pokemon += 1
            print("El entrenador ",
                  entrenador['nombre'], "tiene", cantidad_pokemon, "pokemones")
            cantidad_pokemon = 0


cantidad_pokemones()

print(" ")

# b. listar los entrenadores que hayan ganado más de tres torneos;
print("-----------------------------------------------------------------------------------------------------------------------")
print("PUNTO B")
print(" ")


def torneos_ganados():
    Ganadores_De_Torneo = []
    for entrenador in entrenadores:
        if entrenador['torneos_ganados'] > 3:
            Ganadores_De_Torneo.append(entrenador['nombre'])
    return Ganadores_De_Torneo


ganadores = torneos_ganados()
print(ganadores)

print(" ")
# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
print("-----------------------------------------------------------------------------------------------------------------------")
print("PUNTO C")
print(" ")


def pokemon_mayor_nivel():
    mayor_entrenador = 0
    nombre_mayor = 0
    nombre_pokemon = 0
    pokemon_mayor = 0

    for entrenador in entrenadores:
        if entrenador['torneos_ganados'] > mayor_entrenador:
            nombre_mayor = entrenador['nombre']
            mayor_entrenador = entrenador['torneos_ganados']
            for pokemon in entrenador['pokemones']:
                if pokemon['nivel'] > pokemon_mayor:
                    nombre_pokemon = pokemon['nombre']
                    pokemon_mayor = pokemon['nivel']
    print("Pokemon", nombre_pokemon, "Nivel", pokemon_mayor,
          "Entrenador", nombre_mayor, "Torneos Ganados", mayor_entrenador)


pokemon_mayor_nivel()

print(" ")
# d. mostrar todos los datos de un entrenador y sus Pokémos
print("-----------------------------------------------------------------------------------------------------------------------")
print("PUNTO D")
print(" ")


def informacion_entrenador():
    entrenador_info = {}
    for entrenador in entrenadores:
        if entrenador['nombre'] == 'Ash Ketchum':
            entrenador_info['nombre'] = entrenador["nombre"]
            entrenador_info['torneos ganados'] = entrenador["torneos_ganados"]
            entrenador_info['batallas ganadas'] = entrenador["batallas_ganadas"]
            entrenador_info['batallas perdidas'] = entrenador["batallas_perdidas"]
    return entrenador_info


def informacion_pokemon():
    pokemones_info = []
    for entrenador in entrenadores:
        if entrenador['nombre'] == 'Ash Ketchum':
            for pokemon in entrenador["pokemones"]:
                pokemon_info = {
                    'nombre': pokemon["nombre"],
                    'nivel': pokemon["nivel"],
                    'tipo': pokemon["tipo"],
                    'subtipo': pokemon["subtipo"]
                }
                pokemones_info.append(pokemon_info)
    return pokemones_info


b = informacion_entrenador()
print(b)

a = informacion_pokemon()
print(a)

print(" ")

# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
print("-----------------------------------------------------------------------------------------------------------------------")
print("PUNTO E")
print(" ")


def porcentaje_ganadas():
    porcentaje = []
    for entrenador in entrenadores:
        batallas_totales = entrenador['batallas_ganadas'] + \
            entrenador['batallas_perdidas']
        if batallas_totales > 0:
            porcentaje_ganadas = (
                entrenador['batallas_ganadas'] / batallas_totales) * 100
            if porcentaje_ganadas > 79:
                porcentaje.append(entrenador['nombre'])
    return porcentaje


entrenadores_alto_porcentaje = porcentaje_ganadas()
print(entrenadores_alto_porcentaje)

print(" ")

# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador (tipo, subtipo)
print("-----------------------------------------------------------------------------------------------------------------------")
print("PUNTO F")
print(" ")


def tipo_pokemones():
    pokemones_tipo = []
    for entrenador in entrenadores:
        tiene_fuego = False
        tiene_planta = False
        tiene_agua = False
        tiene_volador = False
        for pokemon in entrenador['pokemones']:
            if pokemon['tipo'] == 'Fuego' or pokemon['subtipo'] == 'Fuego':
                tiene_fuego = True
            if pokemon['tipo'] == 'Planta' or pokemon['subtipo'] == 'Planta':
                tiene_planta = True
            if pokemon['tipo'] == 'Agua' or pokemon['subtipo'] == 'Agua':
                tiene_agua = True
            if pokemon['tipo'] == 'Volador' or pokemon['subtipo'] == 'Volador':
                tiene_volador = True

        if (tiene_fuego and tiene_planta) or (tiene_agua and tiene_volador):
            pokemones_tipo.append(entrenador['nombre'])
    return pokemones_tipo


TiposPokemones = tipo_pokemones()
print("Los entrenadores con tipo fuego/planta o agua/volador son", TiposPokemones)

print(" ")

# g. el promedio de nivel de los Pokémons de un determinado entrenador;
print("-----------------------------------------------------------------------------------------------------------------------")
print("PUNTO G")
print(" ")


def nivel_total():
    niveles_totales_pokemon = 0
    for entrenador in entrenadores:
        if entrenador['nombre'] == 'Ash Ketchum':
            for pokemon in entrenador["pokemones"]:
                niveles_totales_pokemon += pokemon['nivel']
    return niveles_totales_pokemon


tot_nivel = nivel_total()


def pokemones_ash():
    cantidad_pokemon = 0
    for entrenador in entrenadores:
        if entrenador['nombre'] == 'Ash Ketchum':
            for pokemon in entrenador['pokemones']:
                cantidad_pokemon += 1
    return cantidad_pokemon


pokemon_cantidad = pokemones_ash()


promedio_niveles = tot_nivel / pokemon_cantidad
print(f"El promedio total de niveles en Ash Ketchum es de {promedio_niveles}")


print(" ")

# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
print("-----------------------------------------------------------------------------------------------------------------------")
print("PUNTO H")
print(" ")


def encontrar_pikachu():
    Entrenador_Con_Pikachu = []
    for entrenador in entrenadores:
        for pokemon in entrenador['pokemones']:
            if pokemon['nombre'] == 'Pikachu':
                Entrenador_Con_Pikachu.append(entrenador['nombre'])
    return Entrenador_Con_Pikachu


Pikachu = encontrar_pikachu()
print(f"El entrenador con Pikachu es {Pikachu}")

print(" ")

# i. mostrar los entrenadores que tienen Pokémons repetidos;
print("-----------------------------------------------------------------------------------------------------------------------")
print("PUNTO I")
print(" ")


def pokemones_repetidos():
    pokemones = []
    for entrenador in entrenadores:
        pokemones_vistos = []
        tiene_repetidos = False
        for pokemon in entrenador['pokemones']:
            if pokemon['nombre'] in pokemones_vistos:
                tiene_repetidos = True
                break
            else:
                pokemones_vistos.append(pokemon['nombre'])
        if tiene_repetidos:
            pokemones.append(entrenador['nombre'])
    return pokemones


entrenadores_con_pokemon_repetido = pokemones_repetidos()
if len(entrenadores_con_pokemon_repetido) > 0:
    print("Los siguientes entrenadores tienen Pokémon repetidos:")
    for nombre_entrenador in entrenadores_con_pokemon_repetido:
        print(nombre_entrenador)
else:
    print("Ningún entrenador tiene Pokémon repetidos.")

print(" ")


# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Te-
# rrakion o Wingull;

print("-----------------------------------------------------------------------------------------------------------------------")
print("PUNTO J")
print(" ")


def encontrar_pokemon():
    buscar = {"Tyrantrum", "Terrakion", "Wingull"}
    entrenadores_especificos = []
    for entrenador in entrenadores:
        if 'pokemones' in entrenador:
            for pokemon in entrenador['pokemones']:
                if pokemon['nombre'] in buscar:
                    entrenadores_especificos.append(entrenador['nombre'])


entrenadores_especificos = encontrar_pokemon()
print("Los entrenadores con Tyrantrum, Terrakion o Wingull son:",
      entrenadores_especificos)


print(" ")

# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
# como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
# deberán mostrar los datos de ambos;

print("-----------------------------------------------------------------------------------------------------------------------")
print("PUNTO K")
print(" ")

nombre_entrenador = input("Ingresa el nombre del entrenador: ")
nombre_pokemon = input("Ingresa el nombre del Pokémon: ")


def ingresar():
    inf_entrenador = []
    for entrenador in entrenadores:
        if entrenador['nombre'] == nombre_entrenador:
            for pokemon in entrenador['pokemones']:
                if pokemon['nombre'] == nombre_pokemon:
                    inf_entrenador.append(entrenador['nombre'])
                    inf_entrenador.append(entrenador['torneos_ganados'])
                    inf_entrenador.append(entrenador['batallas_ganadas'])
                    inf_entrenador.append(entrenador['batallas_perdidas'])
            return pokemon, inf_entrenador
    return None, None


entrenador_encontrado, pokemon_encontrado = ingresar()

if entrenador_encontrado is not None and pokemon_encontrado is not None:
    print("Entrenador encontrado:", entrenador_encontrado)
    print("Pokemon encontrado:", pokemon_encontrado)
else:
    print("El entrenador no tiene ese Pokémon.")

print(" ")
