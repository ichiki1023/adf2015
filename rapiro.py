import serial
import time
com = serial.Serial('/dev/ttyAMA0', 57600, timeout = 10)

com.write("#M0")
