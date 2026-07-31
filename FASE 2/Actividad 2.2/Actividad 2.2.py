# Actividad 2.2 — Ordenamiento con restricción y datos propios 
# (Py - Ordenamiento numeros finales de la cedula)

def ordenamiento_insercion(arreglo):
    for i in range(1, len(arreglo)):
        clave = arreglo[i]
        j = i - 1
        
        while j >= 0 and arreglo[j] > clave:
            arreglo[j + 1] = arreglo[j]
            j -= 1
        arreglo[j + 1] = clave


ocho_ultimos_digitos_de_la_cedula = [2, 9, 9, 8, 1, 7, 1, 9]
#Mi cedula es: 102998179 y por ende sus ultimos 8 digitos son: 29981719

calificaciones = []
for posicion, digito in enumerate(ocho_ultimos_digitos_de_la_cedula, start=1):
    calificaciones.append(digito * posicion)

print("1. Antes de ordenar la lista dice:", *calificaciones)

ordenamiento_insercion(calificaciones)

print("2. Despues de ordenar la lista dice:", *calificaciones)