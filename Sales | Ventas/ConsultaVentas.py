from io import open


def con_ventas():
    # Esta función está encargada de hacer dos tareas en base a la variable que se introduzca en el ciclo while.
    c_ven = """
----------------------------------------------------------------------------------
                            CONSULTA DE VENTAS
----------------------------------------------------------------------------------
            ID VENDEDOR / MODELO ARTÍCULO / CANTIDAD VENDIDA / GANANCIA
----------------------------------------------------------------------------------"""

    print(c_ven)

    order = """
--------------------------------------------------------------------------
¿Cómo quieres visualizar las ventas?
--------------------------------------------------------------------------
[1] Por Vendedor
[2] Por Artículo
--------------------------------------------------------------------------"""
    print(order)
    option = int(input())
    while option == 1 or 2:  # Si se ingresa 1, se mostrarán las ventas en orden por ID de Vendedor.
        if option == 1:
            with open('Ventas', 'r') as r:
                for line in sorted(r):
                    print(line, end='')
            break
            # op1 = open('Ventas', 'r')
            # listv = list(op1)
            # newv = (str(listv[1:]))
            # print(str(newv))
        if option == 2:  # Si se ingresa 2, se mostrarán las ventas en orden por modelo del artículo.
            with open('Ventas', 'r') as r:
                # Aún no ordena para artículo :(, libreria Pandas exige demasiado cambios en la lógica
                # establecida para nuestro código.
                for line in sorted(r):
                    print(line, end='')
            break
        else:
            print('Esa opción no esta disponible, vuelve a intentarlo.')  # Cortafuegos / Limitación
            option = int(input())

    ops_back = """
--------------------------------------------------------------------------
[v] Regresar a la Sección de Ventas
[m] Regresar al Menú Principal
--------------------------------------------------------------------------"""
    print(ops_back)
    back = input('¿A dónde quieres regresar?\n').lower()  # Back a su elección.

    while back == 'v' or 'm':
        if back == 'v':
            print('Regresando a Sección de Ventas...')  # Regresar a la Sección de Ventas (el submenú)
            from SecciónVentas import ventas
            ventas()
            break
        if back == 'm':
            print('Regresando al Menú Principal...')  # Regresar al Menú Principal sin tener que terminar el programa.
            from ProyectoIntegradorMenú import menu
            menu()
            break
        else:
            print('Esa opción no esta disponible, vuelve a intentarlo.')  # Cortafuegos / Limitación
            back = input().lower()
    return con_ventas()


con_ventas()
