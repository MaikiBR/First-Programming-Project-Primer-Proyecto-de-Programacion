from io import open


def con_inventario():
    # Esta función esta encargada de mostrar el inventario actualizado en pantalla, en el formato indicado abajo con
    # simplemente inicializar la función.
    c_inv = """
------------------------------------------------------------------------------------------
                                CONSULTA DE INVENTARIO
------------------------------------------------------------------------------------------
    MODELO  /   ARTÍCULO    /   CANTIDAD DE ARTÍCULOS   /   PRECIO UNITARIO (Pesos MXN)
------------------------------------------------------------------------------------------"""

    print(c_inv)

    archivo_texto = open('InventarioInicial', 'r')
    print(archivo_texto.read().replace(" / ", "  /  "))
    ops_back = """
-------------------------------------------------------------------------------
[i] Regresar a la Sección de Inventario
[m] Regresar al Menú Principal
-------------------------------------------------------------------------------"""
    print(ops_back)
    back = input('¿A dónde quieres regresar?\n').lower()

    while back == 'i' or 'm':
        # Después de ello se tiene un ciclo while donde dependiendo de la variable ingresada puede haber dos opciones.
        if back == 'i':
            print('Regresando a Sección de Inventario...')  # Regresar a la Sección de Inventario (el submenú)
            from SecciónInventario import inventario
            inventario()
            break
        if back == 'm':
            print('Regresando al Menú Principal...')  # Regresar al Menú Principal sin tener que terminar el programa.
            from ProyectoIntegradorMenú import menu
            menu()
            break
        else:
            print('Esa opción no esta disponible, vuelve a intentarlo.')  # Cortafuegos / Limitación
            back = input().lower()
    return con_inventario()


con_inventario()
