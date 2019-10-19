import RPi.GPIO as gpio
import serial
import time

__arduinoVid__ = '2341'
__arduinoPid__ = '0043'

###############################################################
## TESTE DO MAURÍCIO
def findArduino():
    for port in serial.tools.list_ports.comports():
        if  port.vid != None and port.pid != None:
            if ('{:04X}'.format(port.vid) == __arduinoVid__)and('{:04X}'.format(port.pid) == __arduinoPid__):
                result = port.device
    return result
###############################################################

arduino = serial.Serial(findArduino(), 9600, timeout = None)

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