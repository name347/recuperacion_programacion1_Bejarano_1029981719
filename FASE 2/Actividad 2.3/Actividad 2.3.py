# Actividad 2.3 – Manejo de archivos con contexto local
# (Py – Leer archivo de texto y creador de reporte como archivo de texto)

disponibles = 0
en_mantenimiento = 0

with open("FASE 2/Actividad 2.3/equipos_intep.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")
        estado = datos[2].strip().lower()
        
        if estado == "disponible":
            disponibles += 1
        elif estado == "en mantenimiento":
            en_mantenimiento += 1

with open("FASE 2/Actividad 2.3/reporte_intep.txt", "w", encoding="utf-8") as reporte:
    reporte.write("Estado de Equipos INTEP\n")
    reporte.write(f"Equipos disponibles: {disponibles}\n")
    reporte.write(f"Equipos en mantenimiento: {en_mantenimiento}\n")

print("El reporte se creo como el archivo 'reporte_intep.txt'.")