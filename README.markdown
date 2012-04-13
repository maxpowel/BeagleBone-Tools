==================================
BeagleBone Servo
==================================

This library clones the features of the arduino servo library

Methods
=========
Implemented methods are the same that arduino library

* attach(pin)
  The pin number is a string according to beaglebone users. At the moment only there are only two PWD pins available: P9_14 and P9_16

* write(angle)
  Angle of ration in degrees (from 0 to 180). This angle is converted to microseconds according to the standard but you can change it easily to
  adjust to your servos (just change MIN_DUTY_NS and MAX_DUTY_NS variables in the class servo, this variables contains time in nanoseconds)

* writeMicroseconds(microseconds)
  Pulse width in microseconds. By default the duty frecuency used is 50Hz (pulse time of 20000 microseconds). The standard says that the range
  of our pulses should go from 500 to 2000 microseconds but not all manufacturers comply with this standard. The pulse range is usually from 700 to 2300 microseconds
  but with this function you can find the exact value for your servo

* read
  The last value used with write

* attached
  Get if the servo is attached to some pin

* detach
  Free the pin (in beablebone its not required to free the pin)
  

Note
===========
Before use the servo library, you should enable PWM. Check the example.py file to see a full working example

Warning
===========
BeagleBone works at 3.3V but the servos (usually) works at 5V logic. The signal line should work fine if you connect it directly to beablebone but take care with the
power line. Use a power source of 5V but never a 3.3V or you can fry the pin.

Resources
=========
[GigaMegaBlog](http://www.gigamegablog.com/2012/03/16/beaglebone-coding-101-buttons-and-pwm/)
[Google Groups](https://groups.google.com/d/msg/beagleboard/alKf67dwMHI/b9W2igN6Lr4J)
