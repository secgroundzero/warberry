![alt tag](https://github.com/secgroundzero/warberry/blob/master/SCREENS/1.png)
![alt tag](https://github.com/secgroundzero/warberry/blob/master/SCREENS/2.png)


### Flowcharts

# Static IP Bypass
![alt tag](https://github.com/secgroundzero/warberry/blob/master/SCREENS/warberry static.png)

# MAC Address Filtering Bypass
![alt tag](https://github.com/secgroundzero/warberry/blob/master/SCREENS/warberry mac bypass.png)

# NAC Filtering Bypass
![alt tag](https://github.com/secgroundzero/warberry/blob/master/SCREENS/warberry nac bypass.png)



### Connect to GND and port 23 pins on the RPi.
![alt tag](https://github.com/secgroundzero/warberry/blob/master/SCREENS/IMG_2394.JPG)


### Running the tool with a switch
![alt tag](https://github.com/secgroundzero/warberry/blob/master/SCREENS/IMG_2393.JPG)


### Script for autorunning with a switch

```
#!/usr/bin/env python2.7
import RPi.GPIO as GPIO
import subprocess
GPIO.setmode(GPIO.BCM)

# GPIO 23 set up as input. It is pulled up to stop false signals
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print "it will connect GPIO port 23 (pin 16) to GND (pin 6)\n"

print "Waiting for falling edge on port 23"

try:
    GPIO.wait_for_edge(23, GPIO.FALLING)
    subprocess.call(["python /home/pi/WarBerry/warberry/warberry.py -A"])

except KeyboardInterrupt:
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit
GPIO.cleanup()           # clean up GPIO on normal exit

```
