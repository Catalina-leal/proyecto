import random
import csv
import math

trabajadores = ['nombre',"Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]
sueldos = []


def sueldos_aleatorios():
    global sueldos
    sueldos=[random.randint(300000,2500000) for _ in  range(10)]
    print("sueldos asignados aleatoriamente")
def clasificar_sueldos():
    print("sueldos menores a $800.000", len([s for s in sueldos if s <= 800000]))
    print("sueldos entre $800.000 y $2.000.000", len([s for s in sueldos if 800000 >= s <=2000000]))
    print("sueldos mayores a $2.000.000", len([s for s in sueldos if s >2000000]))
def ver_estadisticas():
   sueldo_max= max(sueldos)
   sueldo_min = min(sueldos)
   sueldo_prom = sueldo/len(sueldos)

   print(f"El sueldo de mayor valor es: $ {sueldo_max}")
   print(f"El sueldo de menor valor es: $ {sueldo_min}")
   print(f"El promedio del valor es: $ {sueldo_prom}")

def reporte_de_sueldos():
    print("se encuentra fuera de servivio")
def salir_del_programa():
    print("finalizando programa...")
    print("Desarrollado por Catalina Leal")
    print("Rut: 20.794.282-0")
def menu():
    while True:
        print("--------------Menu--------------------------")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas.")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")
        opcion = input("Seleccione una opcion: ")
        if opcion == 1:
            salir_del_programa()
        elif opcion == 2:
           
           sueldos_aleatorios()
        elif opcion == 3:
           ver_estadisticas()
        elif opcion == 4:
           reporte_de_sueldos()
        else:
            sueldos_aleatorios()
            clasificar_sueldos()
            salir_del_programa()
menu()      
    

