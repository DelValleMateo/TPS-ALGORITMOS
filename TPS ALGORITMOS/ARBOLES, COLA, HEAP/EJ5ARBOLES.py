from AVL import ARBOLAVL

arbol = ARBOLAVL()
datos = [
    ("Iron Man", True), ("Thanos", False), ("Doctor Strange", True),
    ("Loki", False), ("Captain America", True), ("Hela", False),
    ("Captain Marvel", True), ("Red Skull", False), ("Thor", True)
]

for nombre, es_heroe in datos:
    arbol.insert_node(nombre, {"is_hero": es_heroe})

print("------------------------------------------------")
print("PUNTO B")  # b. Listar villanos ordenados alfabéticamente


print("Villanos ordenados alfabéticamente:")
arbol.inorden_villanos()


print("------------------------------------------------")
print("PUNTO C")  # c. Mostrar superhéroes que empiezan con 'C'


print("\nSuperhéroes que empiezan con 'C':")
arbol.inorden_superheros_start_with("C")


print("------------------------------------------------")
print("PUNTO D")  # d. Determinar cuántos superhéroes hay en el árbol


cantidad_heroes = arbol.contar_super_heroes()
print(f"\nCantidad de superhéroes: {cantidad_heroes}")


print("------------------------------------------------")
print("PUNTO E")  # e. Buscar Doctor Strange y corregir su nombre


doctor_strange = arbol.proximity_search("Doctor St")
if doctor_strange:
    print(f"\nModificando nombre de: {doctor_strange.value}")
    doctor_strange.value = "Doctor Stephen Strange"


print("------------------------------------------------")
print("PUNTO F")  # f. Listar superhéroes en orden descendente


print("\nSuperhéroes en orden descendente:")


def inorden_descendente(root):
    if root:
        inorden_descendente(root.right)
        if root.other_value.get("is_hero"):
            print(root.value)
        inorden_descendente(root.left)


inorden_descendente(arbol.root)

print("------------------------------------------------")
print("PUNTO G")  # g. Generar un bosque de héroes y villanos


arbol_heroes = ARBOLAVL()
arbol_villanos = ARBOLAVL()


def separar_en_bosques(root):
    if root:
        if root.other_value.get("is_hero"):
            arbol_heroes.insert_node(root.value, root.other_value)
        else:
            arbol_villanos.insert_node(root.value, root.other_value)
        separar_en_bosques(root.left)
        separar_en_bosques(root.right)


separar_en_bosques(arbol.root)

print("I")  # I. Determinar cuántos nodos tiene cada árbol


def contar_nodos(arbol):
    def __contar(root):
        if not root:
            return 0
        return 1 + __contar(root.left) + __contar(root.right)
    return __contar(arbol.root)


print(
    f"\nCantidad de nodos en el árbol de héroes: {contar_nodos(arbol_heroes)}")
print(
    f"Cantidad de nodos en el árbol de villanos: {contar_nodos(arbol_villanos)}")

print("II")  # II. Barrido ordenado alfabéticamente de cada árbol


print("\nHéroes ordenados alfabéticamente:")
arbol_heroes.inorden()

print("\nVillanos ordenados alfabéticamente:")
arbol_villanos.inorden()
