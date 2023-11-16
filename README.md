# Sistema de monitoreo activo para la Red Estatal Digital de Jalisco
Proyecto modular 2023B - Sistema de monitoreo activo de la Red Estatal Digital de Jalisco - Emilio Josafat Giacomo Quintero - INCO

![image](https://github.com/Adoptsomekids/Sistema-de-monitoreo-activo-Red-Estatal-Digital-Jalisco/assets/83385717/3044989f-bca6-44f6-83b3-1b071d2faa9a)


## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

Mira **Deployment** para conocer como desplegar el proyecto.

### Pre-requisitos 📋

_Que cosas necesitas para instalar el software y como instalarlas_

```
Raspbian - Debian 11
Python 3.9
Firmware Teltonika RUT2_R_00.07.04.2
pip install aiogram==2.22.1
pip3 show aiogram
python3.9 Active\ monitoring.py 
```

### Instalación 🔧

_Implementación para ejecución de entorno de desarrollo_

_Desde CLI de Raspberry Pi_

```
sudo apt update
sudo apt upgrade

R3_REGISTRATION_CODE="BC12
sudo apt install xrdp
sudo apt instal gpio

systemctl start xrdp
systemctl status xrdp
```

## Ejecutando las pruebas ⚙️

_Verificación de registro de equipos en Remote.IT y acceso por medio de protocolos SSH y RDP_

![image](https://github.com/Adoptsomekids/Sistema-de-monitoreo-activo-Red-Estatal-Digital-Jalisco/assets/83385717/0c39c3cb-fe56-47ff-b817-d34865d73692)

![image](https://github.com/Adoptsomekids/Sistema-de-monitoreo-activo-Red-Estatal-Digital-Jalisco/assets/83385717/abe3ab90-4c17-455d-8c6f-7d3a2aa40570)

_Verificación de pines GPIO en módulo relevador de 4 canales_

### Pruebas de estilo de codificación ⌨️

_Pruebas desde script .sh para reinicio de equipos_

![image](https://github.com/Adoptsomekids/Sistema-de-monitoreo-activo-Red-Estatal-Digital-Jalisco/assets/83385717/ca2ef4f0-ae10-4215-b6d6-16a04f8aa776)

_Funcionamiento de daemon para conexión SLA_

![image](https://github.com/Adoptsomekids/Sistema-de-monitoreo-activo-Red-Estatal-Digital-Jalisco/assets/83385717/7379e4be-1c22-4f05-ad4e-a9a5843b9ea3)

_Verficación de temperatura_

![image](https://github.com/Adoptsomekids/Sistema-de-monitoreo-activo-Red-Estatal-Digital-Jalisco/assets/83385717/b1aa24ba-db09-4e26-955a-d7f8ce0456bd)

_Consulta de logs_

![image](https://github.com/Adoptsomekids/Sistema-de-monitoreo-activo-Red-Estatal-Digital-Jalisco/assets/83385717/f09d5095-668b-45da-b9b1-964176c6bb4f)


## Despliegue 📦

_Deployment desde servidor local del dispositivo (Raspberry Pi)_

![image](https://github.com/Adoptsomekids/Sistema-de-monitoreo-activo-Red-Estatal-Digital-Jalisco/assets/83385717/8f93cbb1-579f-4364-a6cd-a575d1e38b32)

## Construido con 🛠️

_Menciona las herramientas que utilizaste para crear tu proyecto_

* [Shell Scripting](https://www.shellscript.sh/) - Lenguaje de scripting usado.
* [Python](https://www.python.org/) - Lenguaje de programación.
* [Remote.IT](https://www.remote.it/) - Software para gestión remota de equipos por medio de SSH y RDP.
* [Teltonika](https://rms.teltonika-networks.com/) - Software para verificación de alarmas por medio de SMS a través de SIM.
* [Raspberry Pi Imager](https://www.raspberrypi.com/software/) - Software para carga de sistema operativo dentro de Raspberry Pi.

  
## Contribuciones / Agradecimientos 🖇️

Participación directa dentro del proyecto [RED JALISCO](https://red.jalisco.gob.mx/) 

Infraestructura / Soporte / Recursos - Empresa de implementación - [HEMAC](https://www.grupohemac.com.mx/) 

## Autor ✒️

* **Emilio Josafat Giacomo Quintero** - Desarrollo / Codificación - [Adoptsomekids](https://github.com/Adoptsomekids)

## Licencia 📄

Este proyecto está bajo Licencia GPG

---
⌨️ con ❤️ por [Adoptsomekids](https://github.com/Adoptsomekids) 😸
