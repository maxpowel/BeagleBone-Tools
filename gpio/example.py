import gpio


# Put a led with positive leg in p8_3 and negative pin in p8_1

gpio.pinMode("P8_3",gpio.OUTPUT)
gpio.digitalWrite("P8_3",gpio.HIGH)

#Now your led are lighting
#To turn off your led
#gpio.digitalWrite("P8_3",gpio.LOW)
