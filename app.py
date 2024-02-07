from flask import Flask, render_template, request, redirect, url_for
from gpiozero import PWMOutputDevice
from gpiozero import PWMLED
from time import sleep
from smbus import SMBus
import time



pin_derecha = PWMOutputDevice(23)
pin_izquierda = PWMOutputDevice(24)
servo = PWMLED(17, frequency=50)

DS3231_I2C_ADDRESS = 0x68
DS3231_REGISTER = 0x00
ADS1015_ADDRESS = 0x48
ADS1015_CONFIG_REG = 0x01
ADS1015_CONFIG = 0xC583



bus = SMBus(1)
lectura = 0 







def read_adc():
   
    bus.write_i2c_block_data(ADS1015_ADDRESS, ADS1015_CONFIG_REG, [(ADS1015_CONFIG >> 8) & 0xFF, ADS1015_CONFIG & 0xFF])
    time.sleep(0.5)  

   
    data = bus.read_i2c_block_data(ADS1015_ADDRESS, 0x00, 2)
    raw_adc = (data[0] << 8 | data[1])

    return raw_adc


def convert_to_temp(raw_adc):
    
    voltage = raw_adc * 4.096 / 32767.0

    
    temperature_c = (voltage - 0.5) * 21.0

    return temperature_c
# Convertir los datos del sensor
def bcd_to_decimal(bcd):
    return (bcd // 16) * 10 + (bcd % 16)

def decimal_to_bcd(decimal):
    return (decimal // 10) << 4 | (decimal % 10)

# RTC
def get_time():
    date_time_data = bus.read_i2c_block_data(DS3231_I2C_ADDRESS, DS3231_REGISTER, 7)
    second = bcd_to_decimal(date_time_data[0])
    minute = bcd_to_decimal(date_time_data[1])
    hour = bcd_to_decimal(date_time_data[2])
    day = bcd_to_decimal(date_time_data[4])
    month = bcd_to_decimal(date_time_data[5])
    year = bcd_to_decimal(date_time_data[6])
    
    formatted_date = f"{day:02d}/{month:02d}/{year:02d}"
    formatted_time = f"{hour:02d}:{minute:02d}:{second:02d}"
    return f"Fecha: {formatted_date}\nHora: {formatted_time}"



app = Flask(__name__)

ngrok_address = "http://c955-161-18-133-64.ngrok-free.app"  # Reemplaza con tu subdominio

@app.route('/')
def index():
    return render_template('index.html', ngrok_address=ngrok_address)

@app.route('/motor')
def motor():
    ngrok_address_motor = ngrok_address + "/motor"
    return render_template('motor.html', ngrok_address_motor=ngrok_address_motor)

@app.route('/controlar_motor', methods=['POST'])
def controlar_motor():
    
    if request.method == 'POST':
        direccion = request.form.get('direccion')
        velocidad = int(request.form.get('velocidad'))
        if direccion == 'derecha':
            pin_derecha.value = velocidad / 100.0
            pin_izquierda.value = 0
            print(f'Dirección: {direccion}, Velocidad: {velocidad}')
            sleep(20)
            return redirect(url_for('motor'))
        elif direccion == 'izquierda':
            pin_izquierda.value = velocidad / 100.0
            pin_derecha.value = 0
            print(f'Dirección: {direccion}, Velocidad: {velocidad}')
            sleep(20)
            return redirect(url_for('motor'))
        else:
            pin_derecha.value = 0
            pin_izquierda.value = 0
            print(f'Dirección: {direccion}, Velocidad: {velocidad}')
            
            return redirect(url_for('motor'))
 
 
 
@app.route('/servo')
def servo_motor():
    ngrok_address_servo = ngrok_address + "/servo"
    return render_template('servo.html', ngrok_address_servo=ngrok_address_servo) 

@app.route('/controlar_servo', methods=['POST'])
def controlar_servo():
    if request.method == 'POST':
        angulo = int(request.form.get('angulo')) 
        servo.value = (angulo / 1800.0) + 0.025
        sleep(0.5)
        servo.off()
        print(angulo)
        return redirect(url_for('servo_motor'))
    else:
        print("Valor no llego")
        
@app.route('/sensor')
def sensor():
    ngrok_address_motor = ngrok_address + "/sensor"
    return render_template('sensor.html', ngrok_address_motor=ngrok_address_motor)

@app.route('/controlar_sensor', methods=['GET'])
def controlar_sensor():
    resultado = get_time()
    print(resultado)
    return resultado

        
@app.route('/temp')
def temp():
    ngrok_address_temp = ngrok_address + "/temp"
    return render_template('temp.html', ngrok_address_temp=ngrok_address_temp)


@app.route('/controlar_temp', methods=['GET'])
def controlar_temp():
    adc_value = read_adc()
    temperature = convert_to_temp(adc_value)
    print(f"Temperatura: %.2f °C" %temperature)
    return temperature

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)



