# Lista de superhéroes
# 6. Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,
# casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesa-
# rias para poder realizar las siguientes actividades:

# a. eliminar el nodo que contiene la información de Linterna Verde

# b. mostrar el año de aparición de Wolverine

# c. cambiar la casa de Dr. Strange a DC

# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
# “traje” o “armadura”

# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
# sea anterior a 1963

# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla

# g. mostrar toda la información de Flash y Star-Lord

# h. listar los superhéroes que comienzan con la letra B, |M y S

# i. determinar cuántos superhéroes hay de cada casa de comic.


superheroes = [
    {
        "nombre": "Spider-Man",
        "año_aparicion": 1962,
        "casa_comic": "Marvel",
        "biografia": "Peter Parker, un joven que obtiene habilidades arácnidas después de ser mordido por una araña radiactiva."
    },
    {
        "nombre": "Batman",
        "año_aparicion": 1939,
        "casa_comic": "DC",
        "biografia": "Bruce Wayne, un millonario que combate el crimen en Gotham City usando su intelecto y habilidades físicas, con su caracteristico traje."
    },
    {
        "nombre": "Mujer Maravilla",
        "año_aparicion": 1941,
        "casa_comic": "DC",
        "biografia": "Diana, princesa de las Amazonas, que lucha por la justicia, el amor y la igualdad en el mundo."
    },
    {
        "nombre": "Iron Man",
        "año_aparicion": 1963,
        "casa_comic": "Marvel",
        "biografia": "Tony Stark, un genio inventor y empresario que crea una armadura avanzada para convertirse en el superhéroe Iron Man."
    },
    {
        "nombre": "Linterna Verde",
        "año_aparicion": 1940,
        "casa_comic": "DC",
        "biografia": "Hal Jordan, un piloto que se convierte en miembro de la Green Lantern Corps, una fuerza policial intergaláctica."
    },
    {
        "nombre": "Wolverine",
        "año_aparicion": 1974,
        "casa_comic": "Marvel",
        "biografia": "Logan, un mutante con habilidades regenerativas y garras de adamantium."
    },
    {
        "nombre": "Doctor Strange",
        "año_aparicion": 1963,
        "casa_comic": "Marvel",
        "biografia": "Stephen Strange, un neurocirujano que se convierte en el Hechicero Supremo para proteger la Tierra contra amenazas místicas."
    },
    {
        "nombre": "Capitana Marvel",
        "año_aparicion": 1968,
        "casa_comic": "Marvel",
        "biografia": "Carol Danvers, una ex-piloto de la Fuerza Aérea que obtiene superpoderes y se convierte en una de las heroínas más poderosas del universo."
    },
    {
        "nombre": "Flash",
        "año_aparicion": 1940,
        "casa_comic": "DC",
        "biografia": "Barry Allen, un científico forense que obtiene la capacidad de moverse a supervelocidad después de un accidente en su laboratorio."
    },
    {
        "nombre": "Star-Lord",
        "año_aparicion": 1976,
        "casa_comic": "Marvel",
        "biografia": "Peter Quill, un aventurero intergaláctico y líder de los Guardianes de la Galaxia."
    },
    {
        "nombre": "Superman",
        "año_aparicion": 1938,
        "casa_comic": "DC",
        "biografia": "Clark Kent, un extraterrestre del planeta Krypton que posee poderes sobrehumanos en la Tierra."
    },
    {
        "nombre": "Aquaman",
        "año_aparicion": 1941,
        "casa_comic": "DC",
        "biografia": "Arthur Curry, el rey de la Atlántida que tiene la capacidad de comunicarse con la vida marina y posee una fuerza sobrehumana."
    },
    {
        "nombre": "Thor",
        "año_aparicion": 1962,
        "casa_comic": "Marvel",
        "biografia": "El dios del trueno, originario de Asgard, que protege tanto su hogar como la Tierra con su poderoso martillo Mjolnir."
    },
    {
        "nombre": "Viuda Negra",
        "año_aparicion": 1964,
        "casa_comic": "Marvel",
        "biografia": "Natasha Romanoff, una espía y asesina altamente entrenada que se convierte en una agente de S.H.I.E.L.D. y miembro de los Vengadores."
    },
    {
        "nombre": "Flecha Verde",
        "año_aparicion": 1941,
        "casa_comic": "DC",
        "biografia": "Oliver Queen, un millonario que combate el crimen como un arquero experto con un arco y una variedad de flechas especiales."
    }
]

# #a. eliminar el nodo que contiene la información de Linterna Verde
print("-----------------------------------------------------------------------------------------------------------------------")
print("PUNTO A")
print(" ")


personaje = "Linterna Verde"

for heroe in superheroes:
    if heroe["nombre"] == personaje:
        superheroes.remove(heroe)
        break

for heroe in superheroes:
    print(heroe)

print(" ")
# # b. mostrar el año de aparición de Wolverine
print("-----------------------------------------------------------------------------------------------------------------------")
print("PUNTO B")
print(" ")


def aparicion_año():
    for heroe in superheroes:
        if heroe["nombre"] == "Wolverine":
            año_aparicion = heroe["año_aparicion"]
            print("")
            print(f"El año de aparición de Wolverine es {año_aparicion}.")
            print("")
            break


aparicion_año()
print(" ")
# # c. cambiar la casa de Dr. Strange a DC
print("-----------------------------------------------------------------------------------------------------------------------")
print("PUNTO C")
print(" ")


def cambiarcasa():
    for heroe in superheroes:
        if heroe["nombre"] == "Doctor Strange":
            heroe["casa_comic"] = "DC"
            break


cambiarcasa()

for heroe in superheroes:
    print(heroe)
print(" ")
# # d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
# # “traje” o “armadura”
print("-----------------------------------------------------------------------------------------------------------------------")
print("PUNTO D")
print(" ")


def biografia():
    resultado_biografia = []
    for heroe in superheroes:
        if "traje" in heroe["biografia"] or "armadura" in heroe["biografia"]:
            resultado_biografia.append(heroe["biografia"])

    return resultado_biografia


resultado = biografia()
print(resultado)
print(" ")
# # e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
# # sea anterior a 1963
print("-----------------------------------------------------------------------------------------------------------------------")
print("PUNTO E")
print(" ")


def nombre_casa():
    resultado_nombre_casa = []
    for heroe in superheroes:
        if heroe["año_aparicion"] < 1963:
            resultado_nombre_casa.append(heroe["nombre"])
            resultado_nombre_casa.append(heroe["casa_comic"])
            resultado_nombre_casa.append(heroe["año_aparicion"])
    return resultado_nombre_casa


casa_nombre = nombre_casa()
print(casa_nombre)
print(" ")
# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla
print("-----------------------------------------------------------------------------------------------------------------------")
print("PUNTO F")
print(" ")


def mostrar_casa():
    resultado_mostrar_casa = []
    for heroe in superheroes:
        if heroe["nombre"] == "Capitana Marvel":
            resultado_mostrar_casa.append(heroe["nombre"])
            resultado_mostrar_casa.append(heroe["casa_comic"])
        if heroe["nombre"] == "Mujer Maravilla":
            resultado_mostrar_casa.append(heroe["nombre"])
            resultado_mostrar_casa.append(heroe["casa_comic"])
    return resultado_mostrar_casa


casa_mostrar = mostrar_casa()
print(casa_mostrar)
print(" ")
# g. mostrar toda la información de Flash y Star-Lord
print("-----------------------------------------------------------------------------------------------------------------------")
print("PUNTO G")
print(" ")


def informacion():
    informacion_heroes = []
    for heroe in superheroes:
        if heroe["nombre"] == "Flash":
            informacion_heroes.append(heroe["nombre"])
            informacion_heroes.append(heroe["año_aparicion"])
            informacion_heroes.append(heroe["casa_comic"])
            informacion_heroes.append(heroe["biografia"])
        if heroe["nombre"] == "Star-Lord":
            informacion_heroes.append(heroe["nombre"])
            informacion_heroes.append(heroe["año_aparicion"])
            informacion_heroes.append(heroe["casa_comic"])
            informacion_heroes.append(heroe["biografia"])
    return informacion_heroes


heroes_informacion = informacion()
print(heroes_informacion)
print(" ")
# h. listar los superhéroes que comienzan con la letra B, |M y S|
print("-----------------------------------------------------------------------------------------------------------------------")
print("PUNTO H")
print(" ")


def inicial_nombre():
    nombre = []
    for heroe in superheroes:
        if heroe["nombre"][0] == "B":
            nombre.append(heroe["nombre"])
        if heroe["nombre"][0] == "M":
            nombre.append(heroe["nombre"])
        if heroe["nombre"][0] == "S":
            nombre.append(heroe["nombre"])
    return nombre


inicialdelnombre = inicial_nombre()
print(inicialdelnombre)
print(" ")
# i. determinar cuántos superhéroes hay de cada casa de comic.
print("-----------------------------------------------------------------------------------------------------------------------")
print("PUNTO I")
print(" ")


def casa_marvel():
    MarvelCasa = 0
    for heroe in superheroes:
        if "Marvel" in heroe["casa_comic"]:
            MarvelCasa += 1
    return MarvelCasa


def casa_dc():
    CasaDC = 0
    for heroe in superheroes:
        if "DC" in heroe["casa_comic"]:
            CasaDC += 1
    return CasaDC


Marvel_Casa = casa_marvel()
print(f"En la casa Marvel viven {Marvel_Casa} heroes")

DC_Casa = casa_dc()
print(f"En la casa DC viven {DC_Casa} heroes")
