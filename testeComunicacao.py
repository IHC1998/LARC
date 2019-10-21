import RPi.GPIO as gpio
import serial
import time
import serial.tools.list_ports
from serial import Serial

__arduinoVid__ = '2341'
#__arduinoPid__ = '0043'
__arduinoPid__ = '8037'

#def findArduino():
#    for port in serial.tools.list_ports.comports():
#        if  port.vid != None and port.pid != None:
#            if ('{:04X}'.format(port.vid) == __arduinoVid__)and('{:04X}'.format(port.pid) == __arduinoPid__):
#                result = port.device
#    return result

arduino = Serial(
        port='/dev/ttyS0',
        baudrate = 9600,
        parity = serial.PARITY_NONE,
        stopbits = serial.STOPBITS_ONE,
        bytesize = serial.EIGHTBITS,
        timeout = None)

#arduino = serial.Serial(findArduino(), 9600, timeout = None)

#gpio.setmode(gpio.BCM)
#gpio.setup(20, gpio.OUT)


arduino.write(b'A')
print('EnviadoA')
time.sleep(1)
arduino.write(b'C')
print('EnviadoM')
time.sleep(1)
#arduino.write(b'D')
#time.sleep(1)
    
    #try:
    #    if arduino.inWaiting()>0:
    #        caracLido = arduino.readline()
    #        print(caracLido.decode("utf-8"))
    #except serial.SerialException:
    #    pass
    