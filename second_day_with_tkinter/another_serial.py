
import serial

ser = serial.Serial()
ser.baudrate = 9600
ser.bytesize=serial.SEVENBITS
ser.parity=serial.PARITY_EVEN
ser.stopbits=serial.STOPBITS_ONE
ser.xonxoff=0
ser.rtscts=0
ser.timeout=20
ser.port="/dev/ttyS0"

ser.close()
ser.open()
print ("Waiting for P1 output on "  + ser.portstr)

counter=0
#read 20 lines    
while counter < 20:
    print (ser.readline())
    counter+=1

try:
    ser.close()
    print ("Closed serial port.")
except:
    sys.exit ("Couldn't close serial port.")

