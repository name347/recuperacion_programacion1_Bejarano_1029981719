# Actividad 2.1 — Depuración de código con errores (Herencia, polimorfismo, excepciones)
# (Py - Codigo corregido + señalamiento de errores)

class Equipo:
    def __init__(self, codigo, tipo): 
        # Error numero 1: Faltaba __ al final de la palabtra init. 
        # Correccion: Se agregó __ al final de la palabra init.
        self.codigo = codigo 
        # Error numero 2: Faltaba = en la seccion de la linea donde decia codigo codigo sin el = de por medio. 
        # # Correccion: Se agregó el =.
        self.tipo = tipo
        self.estado = "disponible"

    def asignar(self, responsable): 
        # Error numero 3: Al final de la linea se habia omitido escribir el : 
        # Correccion: Se agrego : al final de la linea.
        self.estado = "Asignado a " + responsable
        return self.estado

class PC(Equipo):
    def __init__(self, codigo, procesador): 
        # Error numero 4: Faltanban los __ antes y despues de la palabra init. 
        # # Correccion: Se agregaron los __ antes y despues de la palabra init.
        super().__init__(codigo, "PC") 
        # Error numero 5: Faltaban los __ antes y despues de la palabra init sumando a un espacio adicial.
        # # Correccion: Se corrigio a super().__init__ agregando los __ antes y despues de la palabra init y retirando el espacio adicional.
        self.procesador = procesador

    def asignar(self, responsable):
        if self.estado == "disponible": 
            # Error numero 6: Estaba escrito unicamente con un solo signo de igual envez de dos signos de igual ==.
            # Correccion: Se cambió = por == agregando el segundo signo de igual.
            return super().asignar(responsable)
        else:
            raise Exception("El equipo ya está asignado")

class Impresora(Equipo):
    def __init__(self, codigo, tipo_impresion): 
        # Error numero 7: Faltanban los __ antes y despues de la palabra init y en la seccion tipo_impresion estaba escrito tipo impresion sin el =.
        # # Correccion: Se cambió a __init__ y tipo_impresion.
        super().__init__(codigo, "Impresora")
        self.tipo_impresion = tipo_impresion

inventario = [PC("INT-001", "i5"), PC("INT-002", "i7"), Impresora("INT-003", "Láser")]
for equipo in inventario:
    try:
        print(equipo.asignar("Juan"))
        print(equipo.asignar("María"))
    except Exception as e:
        print(f'Error: {e}')