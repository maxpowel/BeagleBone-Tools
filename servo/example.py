import time
import pwm #Used to enable PWM
from servo import Servo

#You can use your own method to enable PWM, but this just works
pwm.enable();


servo = Servo()
servo.attach("P9_14")

print "To middle"
servo.writeMicroseconds(1500) #to middle
time.sleep(1)

print "To max"
servo.writeMicroseconds(2000) #max
time.sleep(1)

print "To min"
servo.writeMicroseconds(500) #min
time.sleep(1)
# The value in microseconds can change between servos. You can use this function to obtain the max and min values.
# Next, you can use this values to fix the servo class to your own servos (if you need it)

i = 0
while i <= 180:
	#Angle from 0 to 180 degrees
	servo.write(i)
	time.sleep(0.02)
	i = i + 1
	
while i >= 0:
	servo.write(i)
	time.sleep(0.02)
	i = i - 1

servo.detach()





