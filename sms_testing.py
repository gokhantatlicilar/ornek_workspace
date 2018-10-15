import serial

port = serial.Serial("/dev/ttyS0", baudrate=9600)

port.write('AT'.encode())
rcv = port.read(40)
print(rcv)
#print(serial.rcv())
