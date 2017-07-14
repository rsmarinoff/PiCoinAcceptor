import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:  
    while 1:  
	print GPIO.input(4)
except KeyboardInterrupt:  
    print "Reading GPIO Interrupted"
  
except:  
    print "Other error or exception occurred!"  
  
finally:  
    GPIO.cleanup()
