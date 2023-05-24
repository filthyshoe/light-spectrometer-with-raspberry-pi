#Program asks for user input to determine color to shine.

import time, sys
import RPi.GPIO as GPIO

redPin = 11   #Set to appropriate GPIO
greenPin = 15 #Should be set in the 
bluePin = 13  #GPIO.BOARD format

def blink(pin):
    GPIO.setmode(GPIO.BOARD)
    
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
    
def turnOff(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    
def redOn():
    blink(redPin)

def redOff():
    turnOff(redPin)

def greenOn():
    blink(greenPin)

def greenOff():
    turnOff(greenPin)

def blueOn():
    blink(bluePin)

def blueOff():
    turnOff(bluePin)

def yellowOn():
    blink(redPin)
    blink(greenPin)

def yellowOff():
    turnOff(redPin)
    turnOff(greenPin)

def cyanOn():
    blink(greenPin)
    blink(bluePin)

def cyanOff():
    turnOff(greenPin)
    turnOff(bluePin)

def magentaOn():
    blink(redPin)
    blink(bluePin)

def magentaOff():
    turnOff(redPin)
    turnOff(bluePin)

def whiteOn():
    blink(redPin)
    blink(greenPin)
    blink(bluePin)

def whiteOff():
    turnOff(redPin)
    turnOff(greenPin)
    turnOff(bluePin)

def allOn():
    #magenta
    blink(redPin)
    blink(bluePin)
    time.sleep(0.5)
    turnOff(bluePin)
    #red
    blink(redPin)
    time.sleep(0.5)
    #yellow
    blink(greenPin)
    time.sleep(0.5)
    turnOff(redPin)
    #green
    blink(greenPin)
    time.sleep(0.5)
    #cyan
    blink(bluePin)
    time.sleep(0.5)
    turnOff(greenPin)
    #blue
    blink(bluePin)
    time.sleep(0.5)
    turnOff(bluePin)
    
print("""Ensure the following GPIO connections: R-11, G-13, B-15
Colors: Red, Green, Blue, Yellow, Cyan, Magenta, White, and all colors
Use the format: color on/color off""")

def main():
    while True:
        cmd = input("-->")

        if cmd == "red on":
            redOn()
        elif cmd == "red off":
            redOff()
        elif cmd == "green on":
            greenOn()
        elif cmd == "green off":
            greenOff()
        elif cmd == "blue on":
            blueOn()
        elif cmd == "blue off":
            blueOff()
        elif cmd == "yellow on":
            yellowOn()
        elif cmd == "yellow off":
            yellowOff()
        elif cmd == "cyan on":
            cyanOn()
        elif cmd == "cyan off":
            cyanOff()
        elif cmd == "magenta on":
            magentaOn()
        elif cmd == "magenta off":
            magentaOff()
        elif cmd == "white on":
            whiteOn()
        elif cmd == "white off":
            whiteOff()
        elif cmd == "all on": #added
            allOn()
        else:
            print("Not a valid command")
        
        
    return
    

main()