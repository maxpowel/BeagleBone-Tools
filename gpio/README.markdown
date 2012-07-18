==================================
BeagleBone GPIO
==================================

Write/Read digital HIGH or LOW to GPIO

Introduction
=========
There are a lot GPIO (66) in beagle bone and with this library
you can use is like in arduino (pinMode, digitalWrite and digitalRead functions)
  
Methods
=========
Implemented methods are the same that arduino library

* **mode(pin, mode)**
  Set a pin as in or out

* **digitalWrite(pin, value)**
  Write high or low to a pin (only when pin mode is out)

* **digitalRead(pin)**
  Read high or low from a pin. If pin mode is out, the value returned is the actual value of the pin

* **activeLow(true/false)**
  Set the pin as active low

* **freePin(pin)**
  Unbind a pin

  
How to use
===========
Please read the example.py file to view a full working example

Note
===========
This scripts has been tested on Angstrom, Ubuntu and Debian. In Debian you should
mount the debugfs with the following command: mount -t debugfs none /sys/kernel/debug

Warning
===========
BeagleBone works at 3.3V so be sure that the other device uses 3.3V logic. If you connect your beaglebone to a 5V logic device probably you will burn
your RXD pin (but you can use the TXD pin without any risk). You can use pull-up resistors or logic level converter to connect your beaglebone with a 5V logic device.
