class Queue:

    def __init__(self):
        self.__elements = []

    def arrive(self, element):
        self.__elements.append(element)

    def attention(self):
        if len(self.__elements) > 0:
            return self.__elements.pop(0)
        else:
            return None

    def size(self):
        return len(self.__elements)

    def peek(self, index):
        if 0 <= index < len(self.__elements):
            return self.__elements[index]
        return None

    def insert_at(self, index, element):
        if 0 <= index <= len(self.__elements):
            self.__elements.insert(index, element)

    def remove_at(self, index):
        if 0 <= index < len(self.__elements):
            return self.__elements.pop(index)
        return None


# Crear la cola de personajes
queue = Queue()

# Agregar personajes a la cola
queue.arrive({"name": "Luke Skywalker", "planeta": "Tatooine"})
queue.arrive({"name": "Han Solo", "planeta": "Corellia"})
queue.arrive({"name": "Leia Organa", "planeta": "Alderaan"})
queue.arrive({"name": "Yoda", "planeta": "Dagobah"})
queue.arrive({"name": "Jar Jar Binks", "planeta": "Naboo"})
queue.arrive({"name": "Chewbacca", "planeta": "Kashyyyk"})
queue.arrive({"name": "Wicket", "planeta": "Endor"})

print("--------------------------------------------------------")
print("Punto A")


def mostrar_personajes(queue):
    planetas = ["Alderaan", "Endor", "Tatooine"]
    for i in range(queue.size()):
        personaje = queue.peek(i)
        if personaje["planeta"] in planetas:
            print(
                f"Personaje: {personaje['name']}, Planeta: {personaje['planeta']}")


# Mostrar personajes de Alderaan, Endor y Tatooine
mostrar_personajes(queue)

print("--------------------------------------------------------")
print("Punto B")


def indicar_planeta(queue, names):
    for i in range(queue.size()):
        personaje = queue.peek(i)
        if personaje["name"] in names:
            print(f"{personaje['name']} es del planeta {personaje['planeta']}")


# Buscar los planetas de Luke Skywalker y Han Solo
indicar_planeta(queue, ["Luke Skywalker", "Han Solo"])

# PUNTO C


def insert_before_yoda(queue, personaje_nuevo):
    for i in range(queue.size()):
        if queue.peek(i)["name"] == "Yoda":
            queue.insert_at(i, personaje_nuevo)
            break


# Insertar un nuevo personaje antes de Yoda
personaje_nuevo = {"name": "Ahsoka Tano", "planet": "Shili"}
insert_before_yoda(queue, personaje_nuevo)


# PUNTO D


def remove_proximo_jarjar(queue):
    for i in range(queue.size()):
        if queue.peek(i)["name"] == "Jar Jar Binks":
            queue.remove_at(i + 1)
            break


# Eliminar el personaje después de Jar Jar Binks
remove_proximo_jarjar(queue)
