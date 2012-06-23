==================================
BeagleBone ESC
==================================

This library allows you to use Electronic Speed Control (ESC) used by rc cars, planes, helicopters...

Methods
=========
Implemented methods are the same that arduino library

* **attach(pin)**
  The pin number is a string according to beaglebone users. Up to 8 PWM are avaiable: P8_13, P8_19, P9_14, P9_16, P9_29, P9_31, P9_42, P9_48

* **write(percent)**
  Percent of the duty, from 0 to 100

* **writeMicroseconds(microseconds)**
  Pulse width in microseconds. Use this method if you need more precission
  
* **detach(pin)**
  Free the PWM pin

Note
===========
Before use the esc library, you should enable PWM. Check the example.py file to see a full working example

Warning
===========
BeagleBone works at 3.3V but the servos (usually) works at 5V logic. The signal line should work fine if you connect it directly to beablebone but take care with the
power line. Use a power source of 5V but never a 3.3V or you can fry the pin.

Resources
=========
[GigaMegaBlog](http://www.gigamegablog.com/2012/03/16/beaglebone-coding-101-buttons-and-pwm/)
[Google Groups](https://groups.google.com/d/msg/beagleboard/alKf67dwMHI/b9W2igN6Lr4J)
