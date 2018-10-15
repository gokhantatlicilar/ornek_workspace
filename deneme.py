import serial
ser=serial.Serial("/dev/ttyAMA0",9600)
while (1):
 ser.write('selam'.encode())
