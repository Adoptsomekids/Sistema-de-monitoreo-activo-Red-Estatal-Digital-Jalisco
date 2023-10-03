#!/bin/bash
#5559680053:AAHUGPBqwaoba6Ek-


case "$1" in

    "temp")

        sudo vcgencmd measure_temp

        ;;

    "rdp_ssh")

        systemctl is-active xrdp.service

        systemctl is-active ssh.service

        ;;

    "service")

        systemctl is-active sla.service

        ;;

    "ip")

        ip -c a

        ;;

    *)

        echo "Comando no válido"

        ;;

esac

