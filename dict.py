tarjeta_personal = {}

while True:
    menu = int(input('''Selecciona una opcion
                   1. Para introducir datos
                   2. Para editar datos
                   3. Para eliminar datos
                   4. Para valor'''))
    if menu == 1:
        clave = input('Ingrese el valor de la clave')
        valor = input(f'Ingrese el valor de {clave}')
        tarjeta_personal[clave] = valor
        print(tarjeta_personal)
    elif menu == 2:
        clave = input('Ingrese el valor de la clave que desea sobreescribir')
        valor = input(f'Ingrese el valor de {clave}')
        tarjeta_personal[clave] = valor
        print(tarjeta_personal)
    elif menu == 3:
        clave = input('Ingrese el valor de la clave que desea sobreescribir')
        del tarjeta_personal[clave]
        print(tarjeta_personal)
    elif menu == 4:
        break
