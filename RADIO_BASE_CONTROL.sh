#!/bin/bash

# Serial port settings
PORT=/dev/ttyUSB0
BAUD=9600

# Define menu options
echo """
============================================
***CONTROL DE MONITOREO HEMAC RADIO BASES***
   ***¡¡CUIDADO CON LO QUE REINICIAS!!***
============================================
"""

options=("Cnx por consola" "Reinicio Equipos Fisicos" "Revision de ruta" "Reinicio RDP" "Revision de temperatura" "Salir")

# Show menu and get selection
select opt in "${options[@]}"; do
  case $opt in
    "Cnx por consola")
      echo """
      ======================================
      ¡¡ATENCION!!

      Para SALIR de la conexión por consola
      es necesario la siguiente combinacion

      ctrl + a
      Despues escribir : seguido de quit

      :quit

      INGRESA con un enter
      ======================================
      """
      sleep 10
      pkill screen
      screen -S serial -L $PORT $BAUD
      ;;
    "Reinicio Equipos Fisicos")
      sudo python3 /home/rdp/Desktop/CODE/Control_RB.py
      ;;
    "Revision de ruta")
    route
    ping -c 4 8.8.8.8
    traceroute 8.8.8.8
    systemctl status sla.service
    ;;
    "Reinicio RDP")
    systemctl stop xrdp
    systemctl start xrdp
    systemctl status xrdp
    ;;
    "Revision de temperatura")
    watch -c -b -d -t -n 1 -- 'echo """
================================
Control de memoria y temperatura

Para salir preciona ctrl + c
================================
"""; echo "Tiempo activo ==>"; uptime; echo "Fecha sistema ==>"; date; echo "Espacio sistema ==>"; free -m; echo "Temperadura MotherBoard ==>"; sudo vcgencmd measure_temp'
    ;;
    "Salir")
    echo """
    ==============================================================
    Finalizando programa, esperemos que se solucionara tu problema
    """
    sleep 5
      break
      ;;
    *) echo "¡¡Ingresa una opcion valida!!";;
  esac
done
