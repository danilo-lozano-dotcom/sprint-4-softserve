from datetime import datetime # Importación del módulo datetime para manejar fechas

# Definición de la clase Dueño que almacena información del dueño de la mascota
class Dueno:
    def __init__(self, nombre, telefono, direccion):
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion

    # Método para mostrar la información del dueño
    def __str__(self):
        return f"Dueño: {self.nombre}, Teléfono: {self.telefono}, Dirección: {self.direccion}"

# Definición de la clase Mascota que almacena información de la mascota y su dueño
class Mascota:
    def __init__(self, nombre, especie, raza, edad, dueno):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.dueno = dueno
        self.consultas = []

    def agregar_consulta(self, consulta):
        self.consultas.append(consulta)

    # Método para mostrar la información de la mascota y su dueño
    def __str__(self):
        return (f"Nombre: {self.nombre}, Especie: {self.especie}, Raza: {self.raza}, "
                f"Edad: {self.edad}, {self.dueno}")

# Definición de la clase Consulta que almacena información de una consulta veterinaria
class Consulta:
    def __init__(self, fecha, motivo, diagnostico, mascota):
        self.fecha = fecha
        self.motivo = motivo
        self.diagnostico = diagnostico
        self.mascota = mascota

    # Método para mostrar la información de la consulta veterinaria
    def __str__(self):
        return (f"Fecha: {self.fecha}, Motivo consulta: {self.motivo}, "
                f"Diagnóstico: {self.diagnostico}")

# Lista vacía para almacenar todas las mascotas registradas
mascotas = []

# Función para registrar una nueva mascota y su dueño
def registrar_mascota():
    print("\n--- Registrar Nueva Mascota ---")
    nombre = input("Nombre de la mascota: ")
    especie = input("Especie: ")
    raza = input("Raza: ")
    edad = input("Edad: ")
    print("\n--- Datos del Dueño ---")
    nombre_dueno = input("Nombre del dueño: ")
    telefono = input("Teléfono: ")
    direccion = input("Dirección: ")
    dueno = Dueno(nombre_dueno, telefono, direccion)
    mascota = Mascota(nombre, especie, raza, edad, dueno)
    mascotas.append(mascota)
    print("\n¡Mascota registrada exitosamente!\n")

# Función para registrar una consulta veterinaria para una mascota
def registrar_consulta():
    print("\n--- Registrar Consulta ---")
    if not mascotas:
        print("\nNo hay mascotas registradas.\n")
        return
    listar_mascotas()
    idmascota = int(input("Seleccione el número de la mascota: ")) - 1
    if 0 <= idmascota < len(mascotas):
        while True:
            fecha = input("Fecha (YYYY-MM-DD): ")
            try:
                datetime.strptime(fecha, "%Y-%m-%d")  # Validar formato de fecha
                break
            except ValueError:
                print("Formato de fecha inválido. Intente nuevamente.")
        motivo = input("Motivo de la consulta: ")
        diagnostico = input("Diagnóstico: ")
        consulta = Consulta(fecha, motivo, diagnostico, mascotas[idmascota])
        mascotas[idmascota].agregar_consulta(consulta)
        print("\n¡Consulta registrada exitosamente!\n")
    else:
        print("\nSelección inválida.\n")

# Función para mostrar todas las mascotas registradas
def listar_mascotas():
    print("\n--- Lista de Mascotas ---")
    if not mascotas:
        print("No hay mascotas registradas.\n")
        return
    for i, mascota in enumerate(mascotas, 1):
        print(f"{i}. {mascota}")

# Función para mostrar el historial de consultas veterinarias de una mascota
def ver_historial_consultas():
    print("\n--- Historial de Consultas ---")
    if not mascotas:
        print("\nNo hay mascotas registradas.\n")
        return
    listar_mascotas()
    idx = int(input("Seleccione el número de la mascota: ")) - 1
    if 0 <= idx < len(mascotas):
        mascota = mascotas[idx]
        if not mascota.consultas:
            print("\nNo hay consultas registradas para esta mascota.\n")
        else:
            print(f"\nHistorial de consultas para {mascota.nombre}:")
            for consulta in mascota.consultas:
                print(consulta)
    else:
        print("Selección inválida.\n")

# Menú principal de la aplicación
def menu():
    while True:
        print("\n--- Clínica Veterinaria Amigos Peludos ---")
        print("1. Registrar mascota")
        print("2. Agendar consulta")
        print("3. Listar mascotas")
        print("4. Ver historial de consultas de una mascota específica")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_mascota()
        elif opcion == "2":
            registrar_consulta()
        elif opcion == "3":
            listar_mascotas()
        elif opcion == "4":
            ver_historial_consultas()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.\n")

# Punto de entrada de la aplicación
if __name__ == "__main__":
    menu()