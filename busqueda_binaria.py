A = [5, 10, 21, 32, 56, 77, 90, 115]

# Función de la búsqueda
def buscar(lista, numero):
    izq = 0
    der = len(lista) - 1

    while izq <= der:
        cen = (izq + der) // 2

        if lista[cen] == numero:
            return True
        elif lista[cen] < numero:
            izq = cen + 1
        else:
            der = cen - 1

    return False

opcion = "si"

while opcion == "si":

    n = int(input("\nDame un numero: "))

    if buscar(A, n):
        print("Lindooo, Te encontre el numero rey")
    else:
        print("Yaper, Esa vaina no esta aqui")

    opcion = input("¿Quieres buscar otro numero que? (si/no): ").lower()

print("\nPrograma finalizado")
