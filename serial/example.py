# If not installed the serial package in your angstrom
# opkg install python-pyserial
import serial
import uartmux

#Ports avaiable:
# /dev/ttyO1
# /dev/ttyO2
# /dev/ttyO4
# /dev/ttyO5
# ttyO3 is not in the PCB

baudRate = 9600
port = '/dev/ttyO1'

#First enable the port (configure MUX settings)
uartmux.enable(port);

#Now you can use the serial port
ser = serial.Serial(port, baudRate)
ser.write("Test")

while (True):
	ser.write("Test")
	
#print serLe.read(6)
#print serLe.inWaiting()

