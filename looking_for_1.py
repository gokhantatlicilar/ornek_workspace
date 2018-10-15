import RPi.GPIO as GPIO
import time
#ackapa fonksiyonu asagidaki
def blink(pin):
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin,GPIO.LOW)
    time.sleep(1)
    return
#raspberry pin kullanimi atama islemi, _!_resimlere bak
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
for i in range(0,4):
    blink(7)
  
GPIO.cleanup()
