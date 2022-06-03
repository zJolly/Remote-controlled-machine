#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import os


GPIO.setmode(GPIO.BCM)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
#-------------------------------------------------------------------------------
GPIO.output(3,True)
GPIO.output(5,True)
GPIO.output(7,False)
GPIO.output(8,True)
GPIO.output(10,True)
GPIO.output(12,False)
#-------------------------------------------------------------------------------

def avanti():
    GPIO.output(5,True)
    GPIO.output(10,True)
    time.sleep(3)
    GPIO.output(5,False)
    GPIO.output(10,False)
#-------------------------------------------------------------------------------
def indietro():
    GPIO.output(7,True)
    GPIO.output(12,True)
    time.sleep(1)
    GPIO.output(7,False)
    GPIO.output(12,False)
#-------------------------------------------------------------------------------
def sinistra():
    GPIO.output(7,True)
    GPIO.output(10,True)
    time.sleep(1)
    GPIO.output(7,False)
    GPIO.output(10,False)
#-------------------------------------------------------------------------------
def destra():
    GPIO.output(5,True)
    GPIO.output(12,True)
    time.sleep(1)
    GPIO.output(5,False)
    GPIO.output(12,False)
#-------------------------------------------------------------------------------

#Motori abilitati
GPIO.output(3,False)
GPIO.output(8,False)

comando="ciao"

while (True):
    os.system('clear')
    print("Per andare avanti premere W:")
    print("Per andare indietro premere S: ")
    print("Per andare a sinistra premere A:")
    print("Per andare a destra premere D: ")
    print("Q per uscire: ")

    comando = raw_input("Scelta:")

    if comando == "W":
        GPIO.output(3,True)
        GPIO.output(8,True)
        avanti()
    elif comando == "S":
        GPIO.output(3,True)
        GPIO.output(8,True)
        indietro()
    elif comando == "D":
        GPIO.output(3,True)
        GPIO.output(8,True)
 	destra()
    elif comando == "A":
        GPIO.output(3,True)
        GPIO.output(8,True)
	sinistra()
    elif comando == "Q":
        GPIO.output(3,False)
        GPIO.output(8,False)
        break
