#Elaborar un progrma en utilizando multi listas y realiza las siguientes funciones:
# 1.Registrar candidatos a una oportunidad de empleo el cual debe cumplir las siguientes condiciones:
# a.edad(25-35 años)
# b.profesion:Ing.SISTEMAS /INFORMATICO
# Experiencia:2 a 4 años
# 2.consultar candidatos:Mostrar todos los candidatos

# 3.Informacion a capturar
# -Nombres y apellidos  completos
# -Identificacion
# -Correo electronico
# -Contacto
# -Edad
# -Años de experiencia
# -Profesion
# -Ciudad
import os

list_nombres =[]
list_identificacion=[]
list_correo = []
list_contacto = []
list_edad= []
list_años_e = []
list_ciudad = []
ls_sexo = []
list_profesion=[]

def fnt_limpiar():
    os.system('cls')
    print('Autor: Andres Felipe')
    print('18-04-2024')
    
def fnt_registrar(nombre, identificacion, correo, contacto, edad, años_e, ciudad, sexo,profesion):
    if nombre == '' or identificacion == '' or correo == '' or contacto == '' or edad == '' or años_e == '' or ciudad == '' or sexo == '' or profesion == '':
        input('Debe llenar todos los campos')
    else:
        edad = int(edad)
        años_e = int(años_e)
        # Verificar si cumple con las condiciones
        if 25 <= edad <= 35 and años_e >= 2 and años_e <= 4:
            # Agregar a las listas solo si cumple con las condiciones
            list_nombres.append(nombre)
            list_identificacion.append(identificacion)
            list_correo.append(correo)
            list_contacto.append(contacto)
            list_profesion.append(profesion)
            list_edad.append(edad)
            list_años_e.append(años_e)
            list_ciudad.append(ciudad)
            ls_sexo.append(sexo)
        else:
            print('El candidato no cumple con los requisitos de la oferta de empleo.')
def fnt_consultar_candidatos():
    for i in range(len(list_nombres)):
        print(f'Nombres: {list_nombres[i]}')
        print(f'Identificacion: {list_identificacion[i]}')
        print(f'Correo: {list_correo[i]}')
        print(f'Contacto: {list_contacto[i]}')
        print(f'Profesion:{list_profesion}')
        print(f'Edad: {list_edad[i]}')
        print(f'Años de experiencia: {list_años_e[i]}')
        print(f'Ciudad: {list_ciudad[i]}')
        print(f'Sexo: {ls_sexo[i]}\n\n\n')

    input('\nPresiona <ENTER> para continuar...')
    
def fnt_selector(opcion):
    global sw
    if opcion == '1':
        identificacion = input('Ingrese su identificacion: ')
        if identificacion in list_identificacion:
            input('La persona ya está registrada.')
        else:
            nombres = input('Ingrese los nombres y apellidos completos: ')
            correo = input('Ingrese su correo electrónico: ')
            contacto = input('Ingrese su contacto: ')
            profesion = input('Ingrese su profesion\n1.Ingeniero informatico\n2.Otro\n-->')
            if profesion == '1':
                profesion = 'Ingeniero informatico'
            edad = input('Ingrese su edad: ')
            años_e = input('Ingrese los años de experiencia: ')
            ciudad = input('Ingrese la ciudad donde reside: ')
            sexo = input('Ingrese su sexo: ')
            fnt_registrar(nombres, identificacion, correo, contacto, edad, años_e, ciudad, sexo,profesion)
    elif opcion == '2':
        fnt_limpiar()
        fnt_consultar_candidatos()
    elif opcion == '3':
        sw = False   
sw = True
#Menu de opciones
while sw == True:
    fnt_limpiar()
    opcion = input('<<<<<< MENU DE OPCIONES >>>>>>>>>>> \n1.Registrar\n2.Consultar\n3.Salir\nIngrese su opción: ')
    fnt_selector(opcion)
