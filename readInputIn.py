from motorcontroller import *
from machine import Pin, ADC
import time
 
inputPin = machine.Pin(29) #Pin A3
ain = machine.ADC(inputPin)

def getAmbientLight():
    lightReadings = []
    
    for i in range(10):
        currentLight = ain.read_u16()
        lightReadings.append(currentLight)
        time.sleep_ms(100)
    
    ambientAverage = sum(lightReadings)/len(lightReadings);
    
    return ambientAverage

baselineLight = getAmbientLight()
print("\n Average Light: "+ str(baselineLight))

while True:
    print(ain.read_u16())
    time.sleep_ms(100)