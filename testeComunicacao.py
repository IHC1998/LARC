import RPi.GPIO as gpio
import serial
import time

arduino = serial.Serial('/dev/ttyACM0', 9600)

#gpio.setmode(gpio.BCM)
#gpio.setup(20, gpio.OUT)

while (True):
    #VALOR_RECEBIDO = arduino.readline()
    #print(VALOR_RECEBIDO.decode("utf-8"))
    #VALOR_RECEBIDO = 0
    VALOR_RECEBIDO = arduino.readline()
    #print(float(VALOR_RECEBIDO.decode("utf-8")))
    #if( float(VALOR_RECEBIDO.decode("utf-8"))<10):
    print('E')
    print(VALOR_RECEBIDO.decode("utf-8"))
    if(VALOR_RECEBIDO.decode("utf-8") == 'T'):
        print('Infinito')
    else:
        print(float(VALOR_RECEBIDO.decode("utf-8")))
    #VALOR_RECEBIDO = 0
    VALOR_RECEBIDO = arduino.readline()
    print('D')
    if(VALOR_RECEBIDO.decode("utf-8") == 'T'):
        print('Infinito')
    else:
        print(float(VALOR_RECEBIDO.decode("utf-8")))
    #VALOR_RECEBIDO = 0
    VALOR_RECEBIDO = arduino.readline()
    print('M')
    if(VALOR_RECEBIDO.decode("utf-8") == 'T'):
        print('Infinito')
    else:
        print(float(VALOR_RECEBIDO.decode("utf-8")))
    
    
        #gpio.output(20, gpio.HIGH)
    #elif(:
        #gpiput(20, gpio.LOW)