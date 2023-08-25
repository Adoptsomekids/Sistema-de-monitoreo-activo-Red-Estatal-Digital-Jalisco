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

options=("Cnx por consola" "Reinicio Equipos Fisicos" "Revision de ruta" "Reinicio RDP" "Revision de temperatura" "Reinicio de Raspberry Pi" "Ver últimos logs importantes" "Salir")

# Function to confirm reboot
confirm_reboot() {
    echo """
====================================================

      ¡¡ATENCIÓN!!

      Al confirmar ésta opción se reiniciará el
      sistema operativo del equipo (Raspberry Pi)...

====================================================
      """
  read -p "¿Estás seguro de que deseas reiniciar el equipo (Raspberry Pi)? (S/N): " choice
  case $choice in
    [sS]) sudo reboot;;
    [nN]) return;;
    *) echo "Opción inválida. Inténtalo de nuevo."; confirm_reboot;;
  esac
}

# Function to display last important logs
display_logs() {
  echo """
================================
      ¡¡ATENCIÓN!!

      Para SALIR del menu de visualizacion de logs
      es necesaria la siguiente combinación:

      Presiona ENTER para bajar
      Presiona la letra ( q ) Para salir y regresar al menú principal
================================
      """
      sleep 10
echo """
================================
Últimos 50 logs generales del sistema:
"""
  sudo journalctl -n 50
  echo """
================================
"""
}

# Show menu and get selection
select opt in "${options[@]}"; do
  case $opt in
    "Cnx por consola")
      echo """
      ======================================
      ¡¡ATENCIÓN!!

      Para SALIR de la conexión por consola
      es necesario la siguiente combinación:

      ctrl + a
      Después escribir : seguido de quit

      :quit

      Presiona ENTER
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

Para salir presiona ctrl + c
================================
"""; echo "Tiempo activo ==>"; uptime; echo "Fecha sistema ==>"; date; echo "Espacio sistema ==>"; free -m; echo "Temperadura MotherBoard ==>"; sudo vcgencmd measure_temp'
      ;;
    "Reinicio de Raspberry Pi")
      confirm_reboot
      ;;
    "Ver últimos logs importantes")
      display_logs
      ;;
    "Salir")
      echo """
    ==============================================================
    Finalizando programa, esperemos que se solucionara tu problema
    """
      sleep 5
      break
      ;;
    *) echo "¡¡Ingresa una opción válida!!";;
  esac
done
