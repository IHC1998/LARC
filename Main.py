from __future__ import print_function
import serial.tools.list_ports
import numpy as np
import cv2 as cv
from math import atan
from gpiozero import LED
import time
import serial
import argparse
#import RPi.GPIO as gpio

#Inicializar porta serial do arduino
__arduinoVid__ = '2341'
__arduinoPid__ = '8037'


def findArduino():
    for port in serial.tools.list_ports.comports():
        if  port.vid != None and port.pid != None:
            if ('{:04X}'.format(port.vid) == __arduinoVid__)and('{:04X}'.format(port.pid) == __arduinoPid__):
                result = port.device
    return result

#Cria objeto arduino
arduino = serial.Serial(findArduino(), 9600, timeout = None)


'''
A,B,C,D = posicao elevador; L = Ligar Sensor de Cor; I = Liga eltroima
S = Desliga eletroima; E = Liga Infravermelho;
'''


'''
K = quantidade de conteineres q foi pega na pilha
V = quantidade containeres verde depositados em uma pilha
A = quantidade containeres azul depositados em uma pilha
'''
K = 0
V = 0
A = 0

#def sobeElevadorCarregado():

def posicaoElevadorCarregadoVerde():
    if(V == 0):
        arduino.write(b'D')
        V = V+1
    elif(V == 1):
        arduino.write(b'C')
        V = V+1
    elif(V == 2):
        arduino.write(b'B')
        V = V+1
    elif(V == 3):
        arduino.write(b'A')
        V = V+1
    elif(V == 4):
        #Zerar a pilha e começar outra

def posicaoElevadorCarregadoAzul():
    if(A == 0):
        arduino.write(b'D')
        A = A+1
    elif(A == 1):
        arduino.write(b'C')
        A = A+1
    elif(A == 2):
        arduino.write(b'B')
        A = A+1
    elif(A == 3):
        arduino.write(b'A')
        A = A+1
    elif(A == 4):
        #Zerar a pilha e começar outra


def sobeElevadorDescarregado():
    #O arduino deve mandar subir a posição mais a segurança
    if (K == 0):
        arduino.write(b'A')
    if (K == 1):
        arduino.write(b'B')
    if (K == 2):
       arduino.write(b'C')
    if (K == 3):
        arduino.write(b'D')
    if (K == 4):
        #Zerar a pilha e começar outra


def desceElevadorDescarregado():
    if (K == 0):
        arduino.write(b'A')
        K = K+1
    if (K == 1):
        arduino.write(b'B')
        K = K+1
    if (K == 2):
       arduino.write(b'C')
        K = K+1 
    if (K == 3):
        arduino.write(b'D')
        K = K+1
    if (K == 4):
        #Zerar a pilha e começar outra
        
def ligaCor():
    arduino.write(b'L')
    print('LigouCor')

def lerCor():
    try:
        if arduino.inWaiting()>0:
            valor = arduino.read()
            print(valor)
            return valor.decode("utf-8")
    except serial.SerialException:
        pass
    
def ligaIma():
    arduino.write(b'I')
    
def desligaIma():
    arduino.write(b'S')

def ligaInfra():
    arduino.write(b'E')

def lerInfra():
    return float(arduino.readline())
    
def valorInfra():
    try:
        if arduino.inWaiting()>0:
            valorInfra = arduino.readline()
            return float(valorInfra)
    except serial.SerialException:
        pass


while (1):
    ligaCor()
    valorCor = lerCor()
    if(valorCor == 'G'):
        ligaIma()
        print('Verde')
    else:
        desligaIma()
        print('Azul')
    time.sleep(5)
        