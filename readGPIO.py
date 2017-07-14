import RPi.GPIO as GPIO
from evdev import uinput, ecodes as e

def tapKey(key):
    with uinput.UInput() as ui:
        ui.write(e.EV_KEY, key, 1)
        ui.write(e.EV_KEY, key, 0)
        ui.syn()


def risingEdgeCallback(self):
    print "Edge detected"
    tapKey(e.KEY_H)

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
