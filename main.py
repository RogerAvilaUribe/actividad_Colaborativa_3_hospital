from controllers.facturacion_controller import facturacionController
from controllers.servicioController import servicioController


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


def menu_usuarios():
    while True:
        print("\n--- GESTIÓN DE USUARIOS ---")
        print("1. Pacientes")
        print("2. Personal de salud")
        print("3. Personal administrativo")
        print("0. Volver")
        opcion = input(">>>Ingrese una opción del 1 a 3: ").strip()

        match opcion:
            case "1":
                menu_pacientes()
            case "2":
                menu_personal_salud()
            case "3":
                menu_personal_administrativo()
            case "0":
                return
            case _:
                print("Opción inválida. Intente de nuevo.")


def menu_pacientes():
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


def menu_personal_salud():
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


def menu_personal_administrativo():
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


def menu_servicios():
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


def menu_facturacion():
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

    while True:
        mostrar_menu_principal()
        opcion = input(">>>Ingrese una opción del 1 a 4: ").strip()

        match opcion:
            case "1":
                menu_usuarios()
            case "2":
                menu_servicios()
            case "3":
                menu_facturacion()
            case "4":
                menu_reportes()
            case "0":
                print("Saliendo del sistema...")
                break
            case _:
                print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
