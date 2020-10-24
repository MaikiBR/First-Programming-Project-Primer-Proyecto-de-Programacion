# Miguel Ángel Bermea Rodríguez / A01411671
# José Ricardo Rodríguez Castillo / A01411676
def menu():
    # Esta función esta encargada de mandar a llamar a los diferentes archivos del código mediante importación.
    m = """
    >>> MENÚ <<<

[A] Sección de Ventas
[B] Sección de Inventario
[T] Terminar el programa\n"""

    print(m)
    x = input('¿A qué opción quieres acceder?\n').upper()

    while x == 'A' or 'B':
        # De su función principal siempre y cuando se ingrese una de las opciones aceptadas en el ciclo while.
        # Una vez que el ciclo while es iniciado y se ingresa una opción aceptada, el código procederá a realizar
        # las instrucciones declaradas dentro de la función que se mando a llamar por medio de la importación
        # entre archivos.
        if x == 'A':
            print('Accediendo a la Sección de Ventas...')  # Redirección a la Sección de Ventas.
            from SecciónVentas import ventas
            ventas()
            break
        elif x == 'B':
            print('Accediendo a la Sección de Inventario...')  # Redirección a la Sección de Inventario.
            from SecciónInventario import inventario
            inventario()
            break
        elif x == 'T':
            print('Terminando programa. ¡Que tenga un buen día!')  # Opción para terminar el programa.
            exit()
        else:
            print('Esa opción no esta disponible, vuelve a intentarlo.')  # Cortafuegos / Limitación
            x = input().upper()
    return menu()


menu()
