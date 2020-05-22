import csv
import datetime
# Se usan estas librerias para usar expresiones regulares.
import re
# Se usa esta libreria para usar el sistema operativo.
import os
# Se importan las clases de el programa llamado clasePIA.
from clasePIA import Contacto
# Se importa una clase que permite extraer elementos de un objeto
from operator import attrgetter
# Función que nos sirve para mostrar los elementos de la lista de ejemplos.
def NumerodeElementos():
    txt = "Los elementos de la coleccion son {}"
    print(txt.format(len(Contactos)))

def BuscTelefono(telabuscar):
    coincidencia=False
    for contacto in Contactos:
        if (contacto.TELEFONO==telabuscar):
            coincidencia=True
            break
    return coincidencia

def BuscContacto(telabuscar):
    contador=-1
    indice_retorno=-1
    for contacto in Contactos:
        contador+=1
        if (contacto.TELEFONO==telabuscar):
            indice_retorno=contador
            break
    return indice_retorno

Contactos = []
# Se declara una lista que va a almacenar objetos, que en un inicio esta vacia.
NumerodeElementos()

# Se agregan objetos que estaran en la lista.
Contactos.append(Contacto("01AV","Angel Valdez","alexvaldez@unal.edu.mx",8123432187,datetime.date(year=2001,month=8,day=21),1300))
Contactos.append(Contacto("02IF","Ivan Femat","ivanfem@unal.edu.mx",8113453768,datetime.date(year=2002,month=5,day=2),1400))
NumerodeElementos()


# Se define una función utilizando la expresión lambda para ayudarnos a acortar procedimiento.
AclararPantalla = lambda: os.system('cls')

# Valida expresiones regulares
# _txt es el texto que se va a validar.
# _regex es el patrón de expresión regular a validar.
def RegEx(_txt,_regex):
    coincidencia=re.match(_regex, _txt)
    return bool(coincidencia)

def principal():
    while (True):
        AclararPantalla()
        print("LISTA DE CONTACTOS")
        print(" ")
        print("[1] Agregar un contacto.")
        print("[2] Buscar un contacto.")
        print("[3] Eliminar un contacto.")
        print("[4] Mostrar contactos.")
        print("[5] Serializar datos.")
        print("[0] Salir.")
        opcion_elegida = input("¿Qué deseas hacer?  > ")
        if RegEx(opcion_elegida,"^[123450]{1}$"):
            if opcion_elegida=="0":
                print("GRACIAS POR UTILIZAR EL PROGRAMA")
                break
            if opcion_elegida=="1":
                print("Llamar procedimiento para la acción")
            if opcion_elegida=="2":
                print("Seleccionaste la Opcion Buscar Contacto")
                Telefono=int(input("Ingresa Telefono a Buscar: "))

                indice_obtenido=BuscarContacto(Telefono)
                if indice_obtenido==-1:
                    print("No se encontró el objeto")
                else:
                    print(Contactos[indice_obtenido].TELEFONO)
                    print(Contactos[indice_obtenido].NOMBRE)
                    print(Contactos[indice_obtenido].CORREO)

            if opcion_elegida=="3":
                print("Llamar procedimiento para la acción")
            if opcion_elegida=="4":
                print("Mostrando Contactos")
                # Modo en que se ordena.
                Contactos.sort(key=attrgetter("TELEFONO"),reverse=False)
                # Barrido secuencial.
                for contacto in Contactos:
                    print("------------------------------------------")
                    print(contacto.NICKNAME)
                    print(contacto.NOMBRE)
                    print(contacto.CORREO)
                    print(contacto.TELEFONO)
                    print(contacto.FECHANACIMIENTO)
                    print(contacto.GASTO)
            if opcion_elegida=="5":
                print("Llamar procedimiento para la acción")

            input("Pulsa enter para contunuar...")
        else:
            print("Esa respuesta no es válida.")
            input("Pulsa enter para contunuar...")

principal()