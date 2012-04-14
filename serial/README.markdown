==================================
BeagleBone Serial
==================================

This library just prepare the serial ports to be used

Introduction
=========
In beagle bone we can use four serial ports:

* /dev/ttyO1
* /dev/ttyO2
* /dev/ttyO4
* /dev/ttyO5

/dev/ttyO3 is on in the PCB layout

But before use it we should set the right MUX settings. This task is what this library does.

  
How to use
===========
Please read the example.py file to view a full working example

Warning
===========
BeagleBone works at 3.3V so be sure that the other device uses 3.3V logic. If you connect your beaglebone to a 5V logic device probably you will burn
your RXD pin (but you can use the TXD pin without any risk). You can use pull-up resistors or logic level converter to connect your beaglebone with a 5V logic device.
