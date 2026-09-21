import serial

PORT = '/dev/ttyUSB0'
BAUDRATE = 115200

# Inicia la conexión serial con el ESP32
esp32 = serial.Serial(PORT, BAUDRATE, timeout=1)

while True:
    # Lee continuamente los datos entrantes del puerto serial
    linea = esp32.readline().decode().strip()
    # Si hay un dato válido, lo imprime en pantalla
    if linea:
        print(f'ADC = {linea}')