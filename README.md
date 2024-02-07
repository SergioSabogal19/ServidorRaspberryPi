# ServidorRaspberryPi
Este proyecto implementa un servidor en una Raspberry Pi que permite controlar diferentes dispositivos a través de una interfaz web. Utiliza Flask como framework web y ngrok para permitir conexiones externas a partir de una Raspberry PI modelo 3B+.

El el proyecto se implemento un bus de comunicación I2C con el sensor RTC, un sensor de temperatura analogo TMP36GZ al cual fue necesario agregarle un ADC I2C. 
Adicionalmente se agrego un motor DC y un servomotor el cual mediante PWM se controloba la velocidad y sentido de giro para el motor DC y la posición en angulo para el servomotor

## Funcionalidades

- **Motor DC:**
  - Controla la dirección y velocidad de un motor de corriente continua (DC).

- **Servo Motor:**
  - Controla un servo motor mediante ajuste del ángulo.

- **Sensor RTC:**
  - Obtiene la fecha y hora actualizada a través de un sensor de tiempo real (RTC) conectado por I2C.

- **Sensor de Temperatura:**
  - Muestra la temperatura actual obtenida de un sensor de temperatura TMP36GZ a través de un convertidor ADC I2C.

## Configuración del Proyecto

### Requisitos

- Raspberry Pi configurada y en ejecución.
- Python 3 y las bibliotecas necesarias instaladas.
- Ngrok para la exposición externa del servidor.

### Instalación

1. Clona este repositorio en tu Raspberry Pi.

   ```bash
   git clone <https://github.com/SergioSabogal19/ServidorRaspberryPi.git>
   cd <SERVIDOR>
