from io import open
id_vendedores = []
invread = open('InventarioInicial', 'r')
lineas = invread.readline()
datos_final = []

while lineas:
    lineas = lineas.replace('\n', '')
    datos = lineas.split(' / ')
    lineas = invread.readline()
    datos_final.append(datos)


def reg_ventas():
    # Esta función está encargada de hacer dos tareas en base a la variable que se introduzca en el ciclo while.
    r_ven = """
----------------------------------------------
              REGISTRO DE VENTAS
----------------------------------------------
[a] Registro de Venta
----------------------------------------------
[m] Regresar a la Sección de Ventas
----------------------------------------------"""

    print(r_ven)
    rv = input('¿A qué opción quieres acceder?\n').lower()

    while rv == 'a' or 'm':
        if rv == 'a':
            # Cuando la variable es a, significa que se quiere registrar una ventana (por lo que necesitarás acceder un
            # ID de Vendedor o crear una ID.
            id = input('Introduce tu ID de Vendedor, formato AaBb00. Ingresa + para crear una.\n')
            if id == '+':  # Si ingresas '+' ingresarás al sistema de creación de IDs.
                print('CREACIÓN DE ID DE VENDEDOR\n')
                nom = input('Ingresa tu(s) nombre(s) [sin acentos]:\n')
                ape = input('Ingresa tu(s) apellido(s) [sin acentos]:\n')
                nac = input('Ingresa tu año de nacimiento:\n')
                id_creada = nom[0] + nom[1] + ape[0] + ape[1] + nac[2:]
                # El formato de las IDs es AaBb00, es decir, primeros dos digitos de nombre (mayúscula y minúscula
                # resp.), primeros dos dígitos de apellido (mayúscula y minúscula resp.) y últimos dígitos del año
                # de nacimiento.
                print('Tu ID es: ' + id_creada + '\n-ID REGISTRADA CON ÉXITO-')
                registro = open('IDVendedores', 'a')
                registro.write(nom + ' / ' + ape + ' / ' + id_creada)
                registro.write('\n')
                registro.close()
                id_vendedores.append((nom + '/' + ape + '/' + id_creada).split('/'))
                print(id_vendedores)
                print('')
                print('Regresando al Registro de Ventas...')
                reg_ventas()
                rv = input('¿A qué opción quieres acceder?\n').lower()
            else:
                for x in range(len(id_vendedores)):
                    if id_vendedores[x][2] == id:
                        # Si la ID corresponde a alguna, seguirá el proceso de registro de venta, dándote la
                        # bienvenida con tu nombre y apellido, se soliicta el modelo del artículo, la cantidad vendida y
                        # el programa registrará estos datos además de calcular y registrar la ganancia por esa venta
                        # (en base a su precio unitario ubicado en el Inevntario Inicial)
                        print('Bienvenido ' + id_vendedores[x][0] + ' ' + id_vendedores[x][1] + '!')
                        modelox = input('¿Qué artículo vendiste? (Ingresar modelo con formato 00XX):\n')
                        cantidad = input('Ingrese la cantidad vendida:\n')
                        for a in range(len(datos_final)):
                            if datos_final[a][0] == modelox:
                                archivo_texto = open('Ventas', 'a')
                                ganancia = int(datos_final[a][3]) * int(cantidad)
                                archivo_texto.write(id_vendedores[x][2] + ' / ' + modelox + ' / '
                                                    + cantidad + ' / ' + str(ganancia))
                                archivo_texto.write('\n')
                                archivo_texto.close()
                                print('VENTA REGISTRADA')
                                print('')
                                print('Regresando a Registro de Ventas...')
                                reg_ventas()
                                rv = input('¿A qué opción quieres acceder?\n').lower()
                                break
        elif rv == 'm':
            # Por último tenemos la opción de volver a la Sección de Ventas mediante la importación de funciones.
            print('Regresando a Sección de Ventas...')
            from SecciónVentas import ventas
            ventas()
            break
        else:
            print('Esa opción no esta disponible, vuelve a intentarlo.')  # Cortafuegos / Limitación
            rv = input().lower()
    return reg_ventas()


reg_ventas()
