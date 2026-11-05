from controllers.facturacion_controller import facturacionController
from controllers.servicioController import servicioController
from controllers.persona_Controller import personaController
from models.excepciones import FechaNacimientoInvalida, CitasElMismoDia, ServicioObligatorioAlFacturar


def mostrar_menu_principal():
    print("\n==================================================")
    print("    MENÚ PRINCIPAL - SISTEMA DE GESTIÓN HOSPITALARIA")
    print("==================================================")
    print("**********************************************")
    print("1. Gestion de usuarios")
    print("2. Gestion de servicios")
    print("3. Gestion de facturacion")
    print("4. Reportes")
    print("5. Casos Excepcionales")
    print("0. Salir")


def menu_usuarios(persona_controller):
    while True:
        print("\n--- GESTIÓN DE USUARIOS ---")
        print("1. Pacientes")
        print("2. Personal de salud")
        print("3. Personal administrativo")
        print("0. Volver")
        opcion = input(">>>Ingrese una opción del 1 a 3: ").strip()

        match opcion:
            case "1":
                menu_pacientes(persona_controller)
            case "2":
                menu_personal_salud(persona_controller)
            case "3":
                menu_personal_administrativo(persona_controller)
            case "0":
                return
            case _:
                print("Opción inválida. Intente de nuevo.")


def menu_pacientes(persona_controller):
    while True:
        print("\n--- PACIENTES ---")
        print("1. Registrar paciente")
        print("2. Eliminar paciente")
        print("0. Volver")
        opcion = input(">>>Ingrese una opción del 1 a 2: ").strip()

        match opcion:
            
            case "1":
                # Registrar paciente
                print("\n--- Ingrese los datos del paciente ---")
                try:
                    nombre = input("Nombre: ")
                    identificacion = input("Identificación: ")
                    correo = input("Correo electrónico: ")
                    telefono = input("Número de teléfono: ")
                    direccion = input("Dirección de residencia: ")
                    nivelDeAcceso = "Paciente"  # Nivel de acceso fijo para pacientes
                    fechaNacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ")
                    if not fechaNacimiento.strip():
                        raise FechaNacimientoInvalida(fechaNacimiento)
                    contactoEmergencia = input("Contacto de emergencia: ")
                    nombreEps = input("Nombre de la EPS: ")
                
                    persona_controller.agregar_paciente(nombre, identificacion, correo, telefono, direccion, nivelDeAcceso, fechaNacimiento, contactoEmergencia, nombreEps)
                    print("Paciente registrado exitosamente.")
                except FechaNacimientoInvalida as e:
                    print(f"Error: {e}")                    
                
                                    
            case "2":
                # Eliminar paciente
                print("\n--- Eliminar paciente ---")
                pacientesDisponiles = [p for p in persona_controller.get_personas()if type(p).__name__]
                identificacion = input("Ingrese la identificación del paciente a eliminar: ")
                if not pacientesDisponiles:
                    print("No hay pacientes registrados.")
                else:
                    print("\n--- Pacientes disponibles ---")
                    for p, paciente in enumerate(pacientesDisponiles, start=1):
                        print(f"{p}. {paciente.get_nombre()} - ID: {paciente.get_identificacion()}")    
                    try:
                        persona_controller.eliminar_paciente(identificacion)
                        print("Paciente eliminado exitosamente.")
                    except ValueError as e:
                        print(f"Error:{e}") ("No se encontró un paciente con esa identificación.")
            case "0":
                return
            case _:
                print("Opción inválida. Intente de nuevo.")

def menu_personal_salud(persona_controller):
    while True:
        print("\n--- PERSONAL DE SALUD ---")
        print("1. Registrar personal salud")
        print("2. Eliminar personal salud")
        print("0. Volver")
        opcion = input(">>>Ingrese una opción del 1 a 2: ").strip()

        match opcion:
            case "1":
                # Registrar personal de salud
                print("\n--- Ingrese los datos del personal de salud ---")
                nombre = input("Nombre: ")
                identificacion = input("Identificación: ")
                correo = input("Correo electrónico: ")
                telefono = input("Número de teléfono: ")
                direccion = input("Dirección de residencia: ")
                nivelDeAcceso = "Personal de Salud"  # Nivel de acceso fijo para personal de salud
                registroProfesional = input("Registro profesional: ")
                dependencia = input("Dependencia: ")
                especialidad = input("Código de especialidad: ")
                numeroDeHorasSemanales = input("Número de horas semanales: ")
                turno = input("Turno de trabajo: ")
                
                persona_controller.agregar_personalSalud(nombre, identificacion, correo, telefono, direccion, nivelDeAcceso, registroProfesional, dependencia, especialidad, numeroDeHorasSemanales, turno)
                print("Personal de salud registrado exitosamente.")
                
            case "2":
                # Eliminar personal de salud
                print("\n--- Eliminar personal de salud ---")
                personalSaludDisponibles = [p for p in persona_controller.get_personas() if type(p).__name__ == "personalSalud"]
                identificacion = input("Ingrese la identificación del personal de salud a eliminar: ")
                if not personalSaludDisponibles:
                    print("No hay personal de salud registrado.")
                else:
                    print("\n--- Personal de salud disponible ---")
                    for p, personalSalud in enumerate(personalSaludDisponibles, start=1):
                        print(f"{p}. {personalSalud.get_nombre()} - ID: {personalSalud.get_identificacion()}")
                    try:
                        persona_controller.eliminar_personalSalud(identificacion)
                        print("Personal de salud eliminado exitosamente.")
                    except ValueError as e:
                        print(f"Error:{e}") ("No se encontró un personal de salud con esa identificación.")
                
            case "0":
                return
            case _:
                print("Opción inválida. Intente de nuevo.")

def menu_personal_administrativo(persona_controller):
    while True:
        print("\n--- PERSONAL ADMINISTRATIVO ---")
        print("1. Registrar personal administrativo")
        print("2. Eliminar personal administrativo")
        print("0. Volver")
        opcion = input(">>>Ingrese una opción del 1 a 2: ").strip()

        match opcion:
            case "1":
                # Registrar personal administrativo
                print("\n--- Ingrese los datos del personal administrativo ---")
                nombre = input("Nombre: ")
                identificacion = input("Identificación: ")
                correo = input("Correo electrónico: ")
                telefono = input("Número de teléfono: ")
                direccion = input("Dirección de residencia: ")
                nivelDeAcceso = "Personal Administrativo"  # Nivel de acceso fijo para personal administrativo
                dependencia = input("Dependencia: ")
                cargo = input("Cargo: ")
                turno = input("Turno de trabajo: ") 
                
                persona_controller.agregar_adminitrativo(nombre, identificacion, correo, telefono, direccion, nivelDeAcceso, dependencia, cargo, turno)
                print("Personal administrativo registrado exitosamente.")
                
            case "2":
                # Eliminar personal administrativo
                print("\n--- Eliminar personal administrativo ---")
                personalAdministrativoDisponibles = [p for p in persona_controller.get_personas() if type(p).__name__ == "administrativo"]
                identificacion = input("Ingrese la identificación del personal administrativo a eliminar: ")
                if not personalAdministrativoDisponibles:
                    print("No hay personal administrativo registrado.")
                else:
                    print("\n--- Personal administrativo disponible ---")
                    for p, personalAdministrativo in enumerate(personalAdministrativoDisponibles, start=1):
                        print(f"{p}. {personalAdministrativo.get_nombre()} - ID: {personalAdministrativo.get_identificacion()}")
                    try:
                        persona_controller.eliminar_administrativo(identificacion)
                        print("Personal administrativo eliminado exitosamente.")
                    except ValueError as e:
                        print(f"Error:{e}") ("No se encontró un personal administrativo con esa identificación.")
                        
            case "0":
                return
            case _:
                print("Opción inválida. Intente de nuevo.")


def menu_servicios(servicio_controller):
    while True:
        print("\n--- SERVICIOS ---")
        print("1. Registrar nuevo servicio")
        print("2. Eliminar servicio")
        print("0. Volver")
        opcion = input(">>>Ingrese una opción del 1 a 2: ").strip()

        match opcion:
            case "1":
                # Registrar servicio
                pass
            case "2":
                # Eliminar servicios
                pass
            case "0":
                return
            case _:
                print("Opción inválida. Intente de nuevo.")


def menu_facturacion(facturacion_controller):
    
    while True:
        print("\n--- FACTURACIÓN ---")
        print("1. Registrar factura")
        print("2. Eliminar factura")
        print("3. Buscar factura")
        print("0. Volver")
        opcion = input(">>>Ingrese una opción del 1 a 3: ").strip()

        match opcion:
            case "1":
                # registrar factura           
                pass
            case "2":
                # eliminar factura
                pass
            case "3":
                # buscar factura
                pass
            case "0":
                return
            case _:
                print("Opción inválida. Intente de nuevo.")


def menu_reportes():
    while True:
        print("\n--- REPORTES ---")
        print("1. Reporte polimórfico de usuarios")
        print("2. Reporte de servicios")
        print("3. Reporte de facturas")
        print("0. Volver")
        opcion = input(">>>Ingrese una opción del 1 a 3: ").strip()

        match opcion:
            case "1":
                # Reporte polimórfico de usuarios
                pass
            case "2":
                # Reporte de servicios
                pass
            case "3":
                # Reportes de facturas
                pass
            case "0":
                return
            case _:
                print("Opción inválida. Intente de nuevo.")

def main():
    facturacion_controller = facturacionController()
    servicio_controller = servicioController()
    persona_controller = personaController()
    
    while True:
        mostrar_menu_principal()
        opcion = input(">>>Ingrese una opción del 1 a 4: ").strip()

        match opcion:
            case "1":
                menu_usuarios(persona_controller)
            case "2":
                menu_servicios(servicio_controller)
            case "3":
                menu_facturacion(facturacion_controller)
            case "4":
                menu_reportes()
            case "0":
                print("Saliendo del sistema...")
                break
            case _:
                print("Opción inválida. Intente de nuevo.")
                

if __name__ == "__main__":
    main()
    