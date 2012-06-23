==================================
BeagleBone Tools
==================================

Are new in beaglebone? Dont worry, you can use this libraries and forget any problem

Tools provided
=========

* **servo** Control servos using PWM pins
* **esc** Use ESC to control brushless motors
* **serial** Enable serial ports
* **gpio** GPIO control

  
Note
===========
You can use this scripts as helpers. Of course, you can do everything without this scripts.
If you want to learn more about what this scripts does you can read the [beaglebone mail list](https://groups.google.com/forum/?fromgroups#!forum/beagleboard)

This scripts has been tested on Angstrom, Ubuntu and Debian. In Debian you should
mount the debugfs with the following command: mount -t debugfs none /sys/kernel/debug

Warning
===========
BeagleBone works at 3.3V so be sure that the other device uses 3.3V logic. If you connect your beaglebone to a 5V logic device probably you will burn
your RXD pin (but you can use the TXD pin without any risk). You can use pull-up resistors or logic level converter to connect your beaglebone with a 5V logic device.

