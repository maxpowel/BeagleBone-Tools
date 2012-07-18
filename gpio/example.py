import gpio
import time


# Put a led with positive leg in p8_3 and negative pin in p8_1

gpio.pinMode("P8_3",gpio.OUTPUT)
gpio.pinMode("P8_4",gpio.INPUT)

gpio.digitalWrite("P8_3",gpio.HIGH)

#Now your led are lighting


val = gpio.digitalRead("P8_4")
# If P8_4 is connected with P8_3 val = 1
print val

time.sleep(1)
#To turn off your led
gpio.digitalWrite("P8_3",gpio.LOW)

val = gpio.digitalRead("P8_4")
# If P8_4 is connected with P8_3 val = 0
print val
