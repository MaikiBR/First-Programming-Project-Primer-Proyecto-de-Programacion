from io import open
archivo_texto2 = open('InventarioInicial', 'r')
linea = archivo_texto2.readline()
datos_final = []
while linea:
    linea = linea.replace('\n', '')
    datos = linea.split(' / ')
    linea = archivo_texto2.readline()
    datos_final.append(datos)


def reg_inventario():
    # Esta función está encargada de hacer dos tareas en base a la variable que se introduzca en el ciclo while.
    r_inv = """
--------------------------------------------------
              REGISTRO DE INVENTARIO
--------------------------------------------------
[a] Agregar artículo
[b] Modificar artículo
--------------------------------------------------
[m] Regresar al Menú Principal
--------------------------------------------------"""

    print(r_inv)
    r = input('¿A qué opción quieres acceder?\n').lower()

    while r == 'a' or 'b' or 'm':
        if r == 'a':
            # Cuando la variable es a, significa que se quiere agregar un árticulo completamente nuevo a la lista de
            # inventario, el código posteriormente pregunta el modelo, nombre, cantidad disponible y precio, y almacena
            # los datos en el archivo .txt destinado.
            modelo = input('Ingresa el modelo del nuevo artículo en formato 00XX:\n')
            nombre_nuevo_articulo = input('Escriba el nombre del nuevo artículo:\n')
            unidades_adquiridas = input('Ingresa el número de unidades adquiridas:\n')
            precio_unitario = input('Ingresa el precio unitario:\n')
            archivo_texto = open('InventarioInicial', 'a')
            archivo_texto.write('\n')
            archivo_texto.write(
                modelo + ' / ' + nombre_nuevo_articulo + ' / ' + unidades_adquiridas + ' / ' + precio_unitario)
            archivo_texto.close()
            print('Artículo agregado a Inventario')
            print('')
            print('Regresando a Registro de Inventario...')
            reg_inventario()
            r = input('¿A qué opción quieres acceder?\n').lower()
        elif r == 'b':
            # Si la variable ingresada es b, significa que se requiere modificar la cantidad disponible de un modelo
            # específico, el código pide el modelo a modificar y la cantidad de objetos nuevos que llegaron al almacén,
            # los suma y después lo modifica en el inventario.
            modelox = input('Ingrese alguno de los modelos existentes en'
                            ' la lista para modificar su cantidad total disponible:\n')
            cambioinv = input('Ingrese la cantidad que se recibió:\n')
            for x in range(len(datos_final)):
                if datos_final[x][0] == modelox:
                    cambio_final = int(cambioinv) + int(datos_final[x][2])
                    datos_final[x][2] = str(cambio_final)
                    datos0 = ''.join(str(datos_final))
                    datos1 = datos0.replace("', '", ' / ')
                    datos2 = datos1.replace(']', '\n')
                    datos3 = datos2.replace('[', '')
                    datos4 = datos3.replace(", '", "")
                    datos5 = datos4.replace("'", "")
                    archivo_texto = open('InventarioInicial', 'w')
                    archivo_texto.write(datos5)
                    archivo_texto.close()
                    print('Cambio hecho en el Inventario')
                    print('')
                    print('Regresando a Registro de Inventario...')
                    reg_inventario()
                    r = input('¿A qué opción quieres acceder?\n').lower()
                    break
        elif r == 'm':  # Por último tenemos la opción de volver al menú mediante la importación de funciones.
            print('Regresando al Menú Principal...')
            from ProyectoIntegradorMenú import menu
            menu()
            break
        else:
            print('Esa opción no esta disponible, vuelve a intentarlo.')  # Cortafuegos / Limitación
            r = input().lower()
    return reg_inventario()


reg_inventario()
