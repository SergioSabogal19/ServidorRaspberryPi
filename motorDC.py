from gpiozero import PWMOutputDevice
import time

# Configuración de pines
pin_derecha = PWMOutputDevice(23)
pin_izquierda = PWMOutputDevice(24)

# Método para controlar el motor DC
def controlar_motor_dc(direccion, velocidad):
    if direccion == 'derecha':
        pin_derecha.value = velocidad / 100.0
        pin_derecha.value = 0
    elif direccion == 'izquierda':
        pin_izquierda.value = velocidad / 100.0
        pin_izquierda.value = 0
    else:
        pin_derecha.close()
        pin_izquierda.close()
# Limpieza al finalizar

