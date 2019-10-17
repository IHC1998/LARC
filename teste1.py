import numpy as np
import cv2
from math import atan
import RPi.GPIO as gpio
import time


#open_can
gpio.setmode(gpio.BOARD)
cap = cv2.VideoCapture(1)

#define_resolution
def make_1080p():
    cap.set(3, 1920)
    cap.set(4, 1080)

def make_720p():
    cap.set(3, 1280)
    cap.set(4, 720)

def make_480p():
    cap.set(3, 640)
    cap.set(4, 480)

def change_res(width, height):
    cap.set(3, width)
    cap.set(4, height)

make_480p()
change_res(640, 480)

#variables
qx=0
qy=0
i=0
a=0
b=0
cX0=0
cX1=0
cX2=0
cX3=0
cY0=0
cY1=0
cY2=0
cY3=0
A=0
Cximg=320
Cyimg=240
q=0
k=0
metadedafita=20
gpio.setup(11, gpio.OUT)

while (cap.isOpened()):
    ret, img = cap.read()
    
    if ret == True:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret,thresh = cv2.threshold(gray,100,255,0)

        contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for c in contours:
            M = cv2.moments(c)
            if M["m00"] != 0:
             cX = int(M["m10"] / M["m00"])
             cY = int(M["m01"] / M["m00"])
             cX3=cX2
             cX2=cX1
             cX1=cX0
             cX0=cX
             cY3=cY2
             cY2=cY1
             cY1=cY0
             cY0=cY
             q=q+1
             k=abs(int(Cximg-cX))
             j=abs(int(Cyimg-cY))
             if (j-k)<0:
                 if (abs(cX0-cX2)<=10) & (abs(cX1-cX3)<=10) & (abs(cX0-cX1)>50) & (abs(cX2-cX3)>50):
                  if (a!=0) & ((a%2)==0):
                      i=0
                      a=0
                  elif (a!=0) & ((a%2)==1):
                      i=1
                      a=0
                  elif (b!=0) & ((b%2)==0):
                      i=1
                      b=0
                  elif (b!=0) & ((b%2)==1):
                      i=0
                      b=0
                  
                  i=i+1
                  dy=int(qy-cY)
                  qy=cY
                  dx=Cximg-cX
                  erro=int(dx+qx)
                  qx=dx
                  print('I:',i)
                  if (abs(erro)<=25) & (abs(dy)<=15):
                     print('Correto')
                     gpio.output(11, gpio.HIGH)
                  #elif ((abs(Cyimg-cY1)<=10) & (abs(Cyimg-cY0)>30)) or ((abs(Cyimg-cY0)<=10) & (abs(Cyimg-cY1)>30)) :
                     #print('Translação esquerda tantos mm')
                     #translação esquerda tantos mm.
                     #rotaciona horario 90 graus
                     #anda ré tantos mm.
                
                  else:
                     gpio.output(11, gpio.LOW)
                     if (abs(dy)<=15):
                         if (A==0):
                             print('Movimento 2 translacional, distancia de',-erro)
                         elif (A==1):
                             i=i-1
                             A=0                 
                     else:
                         angulo=atan((cY-Cyimg)/(cX-Cximg))*180/3.14
                         print('Movimento 2 rotacional, angulo de',angulo)                  
                                        
                 else: 
                  if (i%2)==0:
                      a=a+1
                      b=0
                      A=1
                      print('A:',a)
                  elif (i%2)==1:
                      b=b+1
                      a=0
                      A=1
                      print('B:',b)

               
             elif  (j-k)>0:
                 if (abs(cY0-cY2)<=10) & (abs(cY1-cY3)<=10) & (abs(cY0-cY1)>50) & (abs(cY2-cY3)>50):
                  if (a!=0) & ((a%2)==0):
                      i=0
                      a=0
                  elif (a!=0) & ((a%2)==1):
                      i=1
                      a=0
                  elif (b!=0) & ((b%2)==0):
                      i=1
                      b=0
                  elif (b!=0) & ((b%2)==1):
                      i=0
                      b=0
                  
                  i=i+1
                  dx=int(qx-cX)
                  qx=cX
                  dy=Cyimg-cY
                  erro=int(dy+qy)
                  qy=dy
                  print('I:',i)
                  if (abs(erro)<=25) & (abs(dx)<=15):
                     print('Correto')
                  else:
                     if (abs(dx)<=15):
                         if (A==0):
                             print('Movimento translacional, distancia de', erro)
                         elif (A==1):
                             i=i-1
                             A=0
                     else:
                         angulo=atan((cX-Cximg)/(cY-Cyimg))*180/3.14
                         print('Movimento rotacional, angulo de',-angulo)                  
                    
                     
                 else: 
                  if (i%2)==0:
                      a=a+1
                      b=0
                      A=1
                      print('A:',a)
                  elif (i%2)==1:
                      b=b+1
                      a=0
                      A=1
                      print('B:',b)

            else:
             cX, cY = 0, 0
            
             
            cv2.circle(thresh, (cX, cY), 5, (255, 255, 255), -1)
            cv2.circle(thresh, (320,240), 5, (255, 255, 255), -1)
            cv2.putText(thresh, "o", (cX , cY),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)        
            #cv2.imshow('img',img)
            cv2.imshow('Thresh',thresh)
            
        

        if cv2.waitKey(1) & 0xFF == ord ('q'):
            break
    else:
        break


cap.release()
cv2.destroyAllWindows() 

