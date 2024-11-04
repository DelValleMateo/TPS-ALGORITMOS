from cola import Queue
from heap import HeapMax, HeapMin


def definirprioridad(encargado, descripcion, hora, cantidadstorm):
    if encargado == "Snoke" or encargado == "Kylo Ren":
        return 3
    elif encargado == "Phasma":
        return 2
    else:
        return 1


heap3 = HeapMax()


def agregarop(encargado, descripcion, hora, cantidadstorm):
    prioridad = definirprioridad(encargado, descripcion, hora, cantidadstorm)
    heap3.arrive([encargado, descripcion, hora, cantidadstorm], prioridad)
    print(
        f"Pedido agregado: {[encargado, descripcion, hora,cantidadstorm]} con prioridad {prioridad}")


def atenderop():
    if len(heap3.elements) > 0:
        opatentida = heap3.atention()
        print(f"Operación atendida: {opatentida}")
        mostrarcola()  # Mostrar el estado de la cola después de atender
    else:
        print("No hay operaciones para atender.")


def mostrarcola():
    print("Estado actual de la cola de prioridad:")
    for elemento in heap3.elements:
        print(f"Prioridad {elemento[0]} - {elemento[1]}")


agregarop("Snoke", "Reunion de Canciller", "10:00", 2)
agregarop("Phasma", "Entrenamiento StormTrooper", "12:00", 304)
agregarop("Kylo Ren", "Revision de operaciones nivel 3", "14:00", 0)
agregarop("General Veers", "Revision de operaciones nivel 2", "16:00", 0)
agregarop("General Zod", "Revision de operaciones nivel 1", "18:00", 0)

atenderop()
atenderop()
atenderop()
atenderop()
atenderop()

agregarop("Phasma", "Revision de intrusos en Hangar B7", "09:00", 25)

atenderop()

agregarop("Snoke", "Destruir planeta Takodana", "04:00", 0)

atenderop()
