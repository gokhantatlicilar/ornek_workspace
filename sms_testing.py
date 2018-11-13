import serial
import io
from array import *
from codecs import encode #(alttaki ile birbirinin alternatifidir)
#from binascii import hexlify
ser = serial.Serial("/dev/ttyS0",9600)
ser2= serial.serial_for_url('loop://',timeout=0)
ser.write("AT\n".encode())
liste=[]
while ser.open:
    s =ser.readline()
    s=(s.decode('utf-8'))
    s=s[:-2]
    #if s != 'AT':
    #liste.append(s)
    print(s)#liste)
    
