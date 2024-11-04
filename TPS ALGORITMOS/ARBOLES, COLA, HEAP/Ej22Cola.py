class Cola:

    def __init__(self):
        self.__elementos = []

    def llegar(self, elemento):
        self.__elementos.append(elemento)

    def atender(self):
        if len(self.__elementos) > 0:
            return self.__elementos.pop(0)
        else:
            return None

    def tamaño(self):
        return len(self.__elementos)

    def mirar(self, indice):
        if 0 <= indice < len(self.__elementos):
            return self.__elementos[indice]
        return None


# Crear la cola de personajes de MCU
cola_mcu = Cola()

# Agregar personajes a la cola
cola_mcu.llegar({"nombre_personaje": "Tony Stark",
                "nombre_superheroe": "Iron Man", "genero": "M"})
cola_mcu.llegar({"nombre_personaje": "Steve Rogers",
                "nombre_superheroe": "Capitán América", "genero": "M"})
cola_mcu.llegar({"nombre_personaje": "Natasha Romanoff",
                "nombre_superheroe": "Black Widow", "genero": "F"})
cola_mcu.llegar({"nombre_personaje": "Carol Danvers",
                "nombre_superheroe": "Capitana Marvel", "genero": "F"})
cola_mcu.llegar({"nombre_personaje": "Scott Lang",
                "nombre_superheroe": "Ant-Man", "genero": "M"})
cola_mcu.llegar({"nombre_personaje": "Peter Parker",
                "nombre_superheroe": "Spider-Man", "genero": "M"})


print("----------------------------------------------------------------")
print("Punto A")


def buscar_personaje_capitana_marvel(cola):
    for i in range(cola.tamaño()):
        personaje = cola.mirar(i)
        if personaje["nombre_superheroe"] == "Capitana Marvel":
            return personaje["nombre_personaje"]
    return None


# Buscar el nombre del personaje de Capitana Marvel
print("El nombre del personaje de Capitana Marvel es:",
      buscar_personaje_capitana_marvel(cola_mcu))


print("----------------------------------------------------------------")
print("Punto B")


def mostrar_superheroes_femeninos(cola):
    for i in range(cola.tamaño()):
        personaje = cola.mirar(i)
        if personaje["genero"] == "F":
            print(f"Superhéroe femenino: {personaje['nombre_superheroe']}")


# Mostrar los superhéroes femeninos
mostrar_superheroes_femeninos(cola_mcu)


print("----------------------------------------------------------------")
print("Punto C")


def mostrar_personajes_masculinos(cola):
    for i in range(cola.tamaño()):
        personaje = cola.mirar(i)
        if personaje["genero"] == "M":
            print(f"Personaje masculino: {personaje['nombre_personaje']}")


# Mostrar personajes masculinos
mostrar_personajes_masculinos(cola_mcu)


print("----------------------------------------------------------------")
print("Punto D")


def buscar_superheroe_scott_lang(cola):
    for i in range(cola.tamaño()):
        personaje = cola.mirar(i)
        if personaje["nombre_personaje"] == "Scott Lang":
            return personaje["nombre_superheroe"]
    return None


# Buscar el superhéroe de Scott Lang
print("El superhéroe de Scott Lang es:",
      buscar_superheroe_scott_lang(cola_mcu))


print("----------------------------------------------------------------")
print("Punto E")


def mostrar_nombres_con_s(cola):
    for i in range(cola.tamaño()):
        personaje = cola.mirar(i)
        if personaje["nombre_personaje"].startswith("S") or personaje["nombre_superheroe"].startswith("S"):
            print(
                f"Nombre del personaje: {personaje['nombre_personaje']}, Superhéroe: {personaje['nombre_superheroe']}, Género: {personaje['genero']}")


# Mostrar los personajes cuyos nombres comienzan con S
mostrar_nombres_con_s(cola_mcu)


print("----------------------------------------------------------------")
print("Punto F")


def buscar_carol_danvers(cola):
    for i in range(cola.tamaño()):
        personaje = cola.mirar(i)
        if personaje["nombre_personaje"] == "Carol Danvers":
            return personaje["nombre_superheroe"]
    return None


# Determinar si Carol Danvers está en la cola
superheroe_carol = buscar_carol_danvers(cola_mcu)
if superheroe_carol:
    print("Carol Danvers es el superhéroe:", superheroe_carol)
else:
    print("Carol Danvers no está en la cola")
