import RPi.GPIO as GPIO

def risingEdgeCallback(self):
    print "Edge detected"

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(16, GPIO.RISING)
GPIO.add_event_callback(16, risingEdgeCallback)

try:  
    while 1:  
	pass
except KeyboardInterrupt:  
    print "Reading GPIO Interrupted"
except:  
    print "Other error or exception occurred!"  
finally:  
    GPIO.cleanup()
