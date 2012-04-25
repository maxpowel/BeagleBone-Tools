#Connect P8_22 (uart2 rx) and P8_24 (uart1 tx)
#Some text will be sent and read at the same time
#If the program does not print the text its because
#something goes wrong

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
port2 = '/dev/ttyO2'

#First enable the port (configure MUX settings)
uartmux.enable(port);
uartmux.enable(port2);

#Now you can use the serial port
ser = serial.Serial(port, baudRate)
ser2 = serial.Serial(port2, baudRate)
ser.write("Test")
	
print ser2.read(4)

ser.close();
ser2.close();
#print serLe.inWaiting()

