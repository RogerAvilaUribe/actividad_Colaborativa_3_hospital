from controllers.facturacion_controller import facturacionController
from controllers.servicioController import servicioController
from controllers.persona_Controller import personaController


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
                pass
            case "2":
                # Eliminar paciente
                pass
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
                pass
            case "2":
                # Eliminar personal de salud
                pass
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
                pass
            case "2":
                # Eliminar personal administrativo
                pass
            case "0":
                return
            case _:
                print("Opción inválida. Intente de nuevo.")


def menu_servicios(servicio_controller):
    categorias = {"1": "Cita", "2": "Examen", "3": "Medicamento"}

    while True:
        print("\n--- SERVICIOS ---")
        print("1. Registrar nuevo servicio")
        print("2. Eliminar servicio")
        print("0. Volver")
        opcion = input(">>>Ingrese una opción del 1 a 2: ").strip()

        match opcion:
            case "1":
                # Registrar servicio
                print("\nCategoría del servicio:")
                print("1. Cita")
                print("2. Examen")
                print("3. Medicamento")
                categoria = input(">>>Ingrese una categoría del 1 a 3: ").strip()
                if categoria not in categorias:
                    print("Categoría inválida. Intente de nuevo.")
                    continue

                de_el = {"1": "de la cita", "2": "del examen", "3": "del medicamento"}[categoria]
                un_una = {"1": "una cita", "2": "un examen", "3": "un medicamento"}[categoria]

                tipo_servicio = input(f">>>Nombre {de_el}: ").strip()
                if not tipo_servicio:
                    print(f"El nombre {de_el} no puede estar vacío.")
                    continue

                if servicio_controller.buscar_servicio(tipo_servicio) is not None:
                    print(f"Ya existe {un_una} con ese nombre.")
                    continue

                try:
                    valor_servicio = float(input(">>>Valor del servicio (solo números, sin puntos ni comas): ").strip())
                except ValueError:
                    print("El valor debe ser un número válido.")
                    continue

                if valor_servicio < 0:
                    print("El valor del servicio no puede ser negativo.")
                    continue

                match categoria:
                    case "1":
                        servicio_controller.agregar_servicioCita(tipo_servicio, valor_servicio)
                    case "2":
                        servicio_controller.agregar_servicioExamen(tipo_servicio, valor_servicio)
                    case "3":
                        servicio_controller.agregar_servicioMedicamento(tipo_servicio, valor_servicio)
            case "2":
                # Eliminar servicios
                servicios = servicio_controller.servicios
                if not servicios:
                    print("No hay servicios registrados.")
                    continue

                print("\nServicios registrados:")
                for i, s in enumerate(servicios, start=1):
                    print(f"{i}. {s.get_tipoServicio()} - Valor: {s.get_valorServicio()}")
                print("0. Cancelar")

                try:
                    numero = int(input(">>>Ingrese el número del servicio a eliminar: ").strip())
                except ValueError:
                    print("Debe ingresar un número válido.")
                    continue

                if numero == 0:
                    continue
                if numero < 1 or numero > len(servicios):
                    print("Número fuera de rango. Intente de nuevo.")
                    continue

                # Los nombres son únicos (se valida al registrar), así que eliminar por nombre es seguro
                servicio_seleccionado = servicios[numero - 1]
                servicio_controller.eliminar_servicioCita(servicio_seleccionado.get_tipoServicio())
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
