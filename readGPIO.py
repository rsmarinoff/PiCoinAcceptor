import RPi.GPIO as GPIO
import keyboard
from time import sleep

def risingEdgeCallback(self):
    keyboard.press('5')
    sleep(0.20)
    keyboard.release('5')

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(16, GPIO.RISING)
GPIO.add_event_callback(16, risingEdgeCallback)
try:
    while 1:
	pass
except KeyboardInterrupt:
    print "Reading GPIO interrupted!"
except:
    print "Unknown error occurred!"
finally:
    GPIO.cleanup()
