def romano_a_decimal(romano):
    romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if len(romano) == 0:
        return 0
    elif len(romano) == 1:
        return romanos[romano[0]]
    else:
        if romanos[romano[0]] < romanos[romano[1]]:
            return romanos[romano[1]] - romanos[romano[0]] + romano_a_decimal(romano[2:])
        else:
            return romanos[romano[0]] + romano_a_decimal(romano[1:])

numero_romano = input("Ingrese el número romano que desea convertir: ").upper()

print("Número romano:", numero_romano)
print("Número decimal:", romano_a_decimal(numero_romano))