# Sistema de Gestión Hospitalaria

## Nombre de los integrantes
- Richard Tabares Botero
- Roger Avila Uribe
- Laura Camila Parra Beltran

## Descripción general del proyecto
Sistema de gestión hospitalaria que permite administrar pacientes, personal de salud, personal administrativo, servicios y facturación. El proyecto aplica los conceptos de herencia, sobrescritura de métodos, polimorfismo y composición entre clases.

## Estructura de los archivos
```text
actividad_3_final_hospital/
├── main.py                          # Punto de entrada / menú interactivo (pendiente)
├── README.md
├── CHEKLIST.md                      # Lista de verificación del taller
├── Documento_Decisiones_Diseno.md   # Documento de decisiones de diseño
├── controllers/
│   └── facturacion_controller.py    # Controlador: registra y almacena facturas en una lista
└── models/
    ├── persona.py                   # Clase base: nombre, identificación, correo, teléfono y dirección
    ├── paciente.py                  # Hereda de persona: código, fecha de nacimiento, contacto de emergencia, EPS y nivel de acceso
    ├── personalSalud.py             # Hereda de persona: código, registro profesional, dependencia, especialidad, contratación, horas, turno y nivel de acceso
    ├── administrativo.py            # Hereda de persona: código, área, cargo, turno y nivel de acceso
    ├── servicio.py                  # Código y nombre del servicio
    └── facturacion.py               # Código de factura, paciente, servicio, personal de salud, administrativo, fecha y total
```

## Instrucciones para ejecutar el proyecto
1. Tener instalado **Python 3.10 o superior**. No se requieren librerías externas.
2. Clonar o descargar el repositorio.
3. Ubicarse en la carpeta raíz del proyecto, donde está `main.py`:
   ```
   cd actividad_3_final_hospital
   ```
4. Ejecutar:
   ```
   python main.py
   ```
   (en algunos sistemas el comando es `python3 main.py`).

Al iniciar, el sistema muestra un menú:

==================================================
    SISTEMA DE GESTIÓN HOSPITALARIA - MENÚ PRINCIPAL
==================================================
**********************************************
1. Gestion de usuarios
    1. Pacientes
        1. Registrar paciente
        2. Eliminar paciente
        0. Volver
    2. Personal de salud
        1. Registrar personal salud
        2. Eliminar personal salud
        0. Volver
    3. Personal administrativo
        1. Registrar personal administrativo
        2. Eliminar personal administrativo
        0. Volver
    0. Volver
2. Gestion de servicios
    1. Registrar nuevo servicio
    2. Eliminar servicio
    0. Volver
3. Gestion de facturacion
    1. Registar factura
    2. Eliminar factura
    3. Buscar factura
    0. Volver
4. Reportes
    1. Reporte polimorfico de usuarios
    2. Reporte de servicios
    3. Reporte de facturas
    0. Volver
0. Salir 
Ingrese una opción del 0 al 4:

## Explicación breve de cómo se aplicaron la herencia, la sobre escritura y el polimorfismo


## Relación de composición entre factura y servicio
