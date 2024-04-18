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
# -Sexo

import os

list_nombres =[]
list_identificacion=[]
list_correo = []
list_contacto = []
list_edad= []
list_años_e = []
list_ciudad = []
ls_sexo = []

def fnt_limpiar():
    os.system('cls')
    print('Autor:Andres Felipe')
    print('18-04-2024')
    
def fnt_registrar(nombre,identificacion,correo,contacto,edad,años_e,ciudad,sexo ):
    if nombre == '' or identificacion == '' or correo == '' or contacto == '' or edad == '' or años_e == '' or ciudad == '' or sexo == '':
        input('Debe llenar todos los campos')
    else:
        list_nombres.append(nombre)
        list_identificacion.append(identificacion)
        list_correo.append(correo)
        list_contacto.append(contacto)
        list_edad.append(edad)
        list_años_e.append(años_e)
        list_ciudad.append(ciudad)
        ls_sexo.append(sexo)

def fnt_consultar():
    for i in range(len(list_nombres)):
        print(f'Nombres: {list_nombres[i]}')
        print(f'Identificacion: {list_identificacion[i]}')
        print(f'Correo: {list_correo[i]}')
        print(f'Contacto: {list_contacto[i]}')
        print(f'Edad: {list_edad[i]}')
        print(f'Años de experiencia: {list_años_e[i]}')
        print(f'Ciudad: {list_ciudad[i]}')
        print(f'Sexo: {ls_sexo[i]}')
        
def fnt_selector(opcion):
    global sw
    if opcion == '1':
        identificacion= input('Ingrese los nombres y apellidos completos')
        if identificacion in list_identificacion:
            input('La persona ya esta registrada')
        else:
            nombres= input('Ingrese los nombres y apellidos completos')
            correo = input('Ingrese su correo electronico')
            contacto=input('Ingrese su contacto')
            edad = input('Ingrese su edad')
            años_e = input('Ingrese los años de experiencia')
            ciudad = input('Ingrese la ciudad donde reside')
            sexo = input('Ingrese su sexo')
            fnt_registrar(nombres,correo,contacto,edad,años_e,ciudad,sexo)
    elif opcion == '2':
        fnt_limpiar()
        for i in range(len(list_nombres)):
            print(f'Nombres:{list_nombres[i]}    Identificacion:{list_identificacion[i]}   Correo:{list_correo[i]}   Contacto:{list_contacto[i]} {list_edad} {list_años_e} {list_ciudad} {ls_sexo}')
        enter = input('\nPresiona <ENTER> para continuar...')
    elif opcion == '3':
        sw = False
    
sw = True

while sw == True:
    opcion = input('<<<<<< MENU DE OPCIONES >>>>>>>>>>> \n1.Registar\n2.Consultar\n3.Salir')