import RPi.GPIO as GPIO #Add GPIO library to a Python sketch
import time #Add time library to a Python sketch
GPIO.setmode(GPIO.BOARD) #Setup GPIO using Board numbering
GPIO.setup(11, GPIO.OUT) #Setup pin 11 to output
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#Setup pin 12 to input and Pull-Up
state = 0
count = 0
while True:
if (GPIO.input(12)==1): #Read Botton pin 7
state = 0
else:
state = 1
if(state==1):
count +=1
if(count %2 == 0):
print(“LED = 0, LOW”)
GPIO.output(11,GPIO.LOW)
elif(count %2 == 1):
print(“LED = 1, HIGH”)
GPIO.output(11,GPIO.HIGH)
print(“Count number = “+str(count))
time.sleep(0.5)
