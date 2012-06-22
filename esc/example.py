import time
import pwm #Used to enable PWM
from esc import ESC

#You can use your own method to enable PWM, but this just works
pwm.enable();


esc = ESC()
esc.attach("P9_16")

# This example works with aeolian car (double direction) ESC which minimum throttle is 80.
# Try changing values until you found the right value for your ESC
esc.write(80)
#esc.writeMicroseconds(1600)
#Now the ESC es ready, in my case if I use values less than 80 the motor goes rearward
# and if the values are greater than 80 the motor goes fordward

