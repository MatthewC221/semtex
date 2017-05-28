#!/usr/bin/python

import sys
import socket

sock = socket.socket()  
port_no = 24027
addr = 'semtex.labs.overthewire.org'
try:
    sock.connect((addr, port_no))
except Exception as e:
    print("Exception: %s" % (e))
    
data = (sock.recv(10))
if not data:
    print ("Receive unsuccessful")
else:
    print ("Length = " + str(len(data)))
sock.close()


