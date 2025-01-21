from machine import Pin, ADC, PWM
from utime import sleep
import neopixel
import time
# Initialization
bottomservo = PWM(Pin(5, mode=Pin.OUT)) # Servo PIN reference
bottomservo.freq(50) # Servo frequency
topservo = PWM(Pin(6, mode=Pin.OUT)) # Servo PIN reference
topservo.freq(50) # Servo frequency

# Neopixel
n = 7
p = 10
np = neopixel.NeoPixel(machine.Pin(p), n)

# LDR
ldr = ADC(26)

# PIR
PIR_sensor = Pin(13, Pin.IN, Pin.PULL_UP)

# TOUCH
pin_sensor = Pin(18, mode=Pin.IN, pull=Pin.PULL_UP)

def bottomservomove(degree):
    servomin = 1800
    servomax = 8500
    servostep = (servomax-servomin)/180
    position = servomin + (degree * servostep)
    bottomservo.duty_u16(int(position))
def topservomove(degree):
    servomin = 1800
    servomax = 8500
    servostep = (servomax-servomin)/180
    position = servomin + (degree * servostep)
    topservo.duty_u16(int(position))
def center():
    topservomove(90)
    bottomservomove(90)
def shake():
    for i in range(45, 135, 5):
        bottomservomove(i)
        sleep(.1)
        print(i)
    sleep(1)
    for i in range(135, 45, -5):
        bottomservomove(i)
        sleep(.1)
        print(i)
    sleep(1)
    for i in range(45, 135, 5):
        topservomove(i)
        sleep(.1)
        print(i)
    sleep(1)
    for i in range(135, 45, -5):
        topservomove(i)
        sleep(.1)
        print(i)
    sleep(1)
def clear():
  for i in range(n):
    np[i] = (0, 0, 0)
    np.write()
def set_color(r, g, b):
  for i in range(n):
    np[i] = (r, g, b)
  np.write()
def cycle(r, g, b, wait):
  for i in range(1 * n):
    for j in range(n):
      np[j] = (0, 0, 0)
    np[i % n] = (r, g, b)
    np.write()
    time.sleep_ms(wait)
    
# Code
sleep(29+--)
while True:
    if pin_sensor.value() == 1:
        print("Enter Assist Mode")
        while True:
            clear()
            digital_value = ldr.read_u16()   # Lowest value 1440, Average 13500, Max 45300
            rgb_value = int((digital_value)/120)
            rgb = 155-rgb_value
            set_color(rgb,int(rgb/2),rgb)
            sleep(.5)
            if pin_sensor.value() == 1:
                clear()
                print("Exit LED Mode")
                break
    if PIR_sensor.value() == 1:
        if pin_sensor.value() == 1:
            print("Enter Assist Mode")
            while True:
                clear()
                digital_value = ldr.read_u16()   # Lowest value 1440, Average 13500, Max 45300
                rgb_value = int((digital_value)/120)
                rgb = 155-rgb_value
                set_color(rgb,int(rgb/2),rgb)
                sleep(.5)
                if pin_sensor.value() == 1:
                    clear()
                    print("Exit LED Mode")
                    break
        print("Motion Detected!")
        sleep(1)
        topservomove(90)
        bottomservomove(20)
        sleep(3)
        bottomservomove(0)
        sleep(.2)
        bottomservomove(40)
        sleep(.2)
        bottomservomove(0)
        sleep(.2)
        topservomove(45)
        sleep(.2)
        topservomove(135)
        sleep(.2)
        topservomove(90)
        sleep(1)
        cycle(0,200,0,100)
        sleep(1)
        clear()
        set_color(15,15,0)
        sleep(5)
        topservomove(135)
        sleep(1)
        while True:
            set_color(15,15,0)
            if PIR_sensor.value() == 0:
                break
            if pin_sensor.value() == 1:
                break
    elif PIR_sensor.value() == 0:
        if pin_sensor.value() == 1:
            print("Enter Assist Mode")
            while True:
                clear()
                digital_value = ldr.read_u16()   # Lowest value 1440, Average 13500, Max 45300
                rgb_value = int((digital_value)/120)
                rgb = 155-rgb_value
                set_color(rgb,int(rgb/2),rgb)
                sleep(.5)
                if pin_sensor.value() == 1:
                    clear()
                    print("Exit LED Mode")
                    break
        print("No Motion Detected!")
        topservomove(90)
        bottomservomove(20)
        sleep(3)
        clear()
        sleep(1)