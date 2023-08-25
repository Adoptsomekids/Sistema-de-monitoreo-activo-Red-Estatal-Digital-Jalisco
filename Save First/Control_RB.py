# obteniendo la biblioteca principal de GPIO
import RPi.GPIO as GPIO
# obtener la biblioteca de tiempo
import time
# Obtener la biblioteca del sistema operativo
import os

# configurando un modo actual
GPIO.setmode(GPIO.BCM)
# eliminando los warings
GPIO.setwarnings(False)
# creando una lista (matriz) con el número de GPIO que usamos

# Creados una lista de variables donde estan nuestros relay a prender

relay_pins = [6, 13]


#GPIO.setup(relay_pins[0], GPIO.OUT)


#GPIO.output(relay_pins,  GPIO.LOW)
# estableciendo el modo para todos los pines para que todos esten encendidos
def start():
    print("""
============================================
*CONTROL DE MONITOREO HEMAC RADIO BASES*
   ¡¡CUIDADO CON LO QUE REINICIAS!!
============================================
¿ Selecciona el equipo a reiniciar?
1- Enlace BackBone
2- GPS
3- REINICIO GENERAL CUIDADO
4- Reinicio de menu
5- Salir del programa
            """)

def relay():
    print("======================")
    opcion = input("Ingresa la opcion: ")

    # For para reiniciar el Backbone
    if opcion == "1":
        print("==========================")
        print("Reiniciando Enlace BackBone")
        print("Esta accion tomara 15 seg.")
        print("==========================")
        GPIO.setup(relay_pins[0], GPIO.OUT)
        time.sleep(15)
        GPIO.setup(relay_pins[0], GPIO.IN)
        print("==========================")
        print("¡¡Reinicio exitoso!!")
        print("==========================")
        time.sleep(3)
        os.system("clear")
        start()
        relay()

    # For para reiniciar GPS
    elif opcion == "2":
        print("==========================")
        print("Reiniciando GPS")
        print("Esta accion tomara 15 seg.")
        print("==========================")
        GPIO.setup(relay_pins[1], GPIO.OUT)
        time.sleep(15)
        GPIO.setup(relay_pins[1], GPIO.IN)
        print("==========================")
        print("¡¡Reinicio exitoso!!")
        print("==========================")
        time.sleep(3)
        os.system("clear")
        start()
        relay()

    #  Reinicio general
    elif opcion == "3":
        print("==========================")
        print("Reinicio General")
        print("Esta accion tomara 15 seg.")
        print("==========================")
        GPIO.setup(relay_pins, GPIO.OUT)
        time.sleep(15)
        GPIO.setup(relay_pins, GPIO.IN)
        print("==========================")
        print("¡¡Reinicio exitoso!!")
        print("==========================")
        time.sleep(3)
        os.system("clear")
        start()
        relay()

    elif opcion == "4":
        print("========================================")
        print("Se reiniciara el programa en 5 segundos.")
        time.sleep(5)
        os.system("clear")
        start()
        relay()

    elif opcion == "5":
        print("==============================================================")
        print("Finalizando programa, esperemos que se solucionara tu problema")
        GPIO.cleanup()
        time.sleep(3)
        return

    else:
        print("==========================")
        print("Opcion no valida")
        print("Se reiniciara el programa.")
        time.sleep(3)
        os.system("clear")
        start()
        relay()

start()
relay()
