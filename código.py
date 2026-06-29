def calcularCosto(peso, region):
    costo = peso * 500

    if region == 1:
        return costo
    elif region == 2:
        return costo * 1.15
    else:
        return costo * 1.40

def cargarEnvios(cantidad):
    costos = []

    for i in range(cantidad):
        print("\nEnvío", i + 1)
        peso = float(input("Ingrese el peso (kg): "))
        while peso <= 0:
            print("Error. El peso debe ser mayor a 0.")
            peso = float(input("Ingrese el peso (kg): "))

        region = int(input("Ingrese la región (1=Local, 2=Regional, 3=Internacional): "))
        while region < 1 or region > 3:
            print("Error. La región debe ser 1, 2 o 3.")
            region = int(input("Ingrese la región (1=Local, 2=Regional, 3=Internacional): "))

        costo = calcularCosto(peso, region)
        costos.append(costo)

    return costos

def mostrarTicket(costos):
    total = 0

    print("\n====== TICKET DE FLETES ======")

    for i in range(len(costos)):
        print("Envío", i + 1, "- Costo: $", round(costos[i], 2))
        total += costos[i]

    print("------------------------------")
    print("Total general: $", round(total, 2))

    return total


cantidad = int(input("¿Cuántos envíos desea liquidar? "))

while cantidad <= 0:
    print("La cantidad debe ser mayor a 0.")
    cantidad = int(input("¿Cuántos envíos desea liquidar? "))

costos = cargarEnvios(cantidad)
mostrarTicket(costos)
