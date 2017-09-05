#!/usr/bin/python

import socket
import sys
import threading
import time

socket.timeout(10)

level5_pass = "HELICOTRMA"
address = "semtex.labs.overthewire.org"
host = '127.0.0.1'
port_no = 24027
unique_pass = "Matthew221"
diff_ip = ['127.0.0.11', '127.0.0.12', '127.0.0.13', '127.0.0.14', '127.0.0.15', '127.0.0.16', '127.0.0.17', '127.0.0.18', '127.0.0.19', '127.0.0.20']

def sxor(s1):    
    # convert strings to a list of character pair tuples
    # go through each tuple, converting them to ASCII code (ord)
    # perform exclusive or on the ASCII code
    # then convert the result back to ASCII (chr)
    # merge the resulting array of characters as a string
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,level5_pass))

class myThread (threading.Thread):

    def __init__(self, threadID, name, counter, IP):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.fake_IP = IP
      
    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.bind((self.fake_IP, 0))
        try:
            sock.connect((host, port_no))
        except Exception as e:
            print("something's wrong with %s:%d. Exception is %s" % (host, port_no, e))
            
        first_string = (sock.recv(1024))
        print first_string
        sock.send(bytearray(sxor(first_string) + unique_pass))
        print sock.recv(1024)
        time.sleep(0.3)

if __name__ == '__main__':

    thread0 = myThread(0, "Thread-0", 0, diff_ip[0])    
    thread1 = myThread(1, "Thread-1", 1, diff_ip[1])
    thread2 = myThread(2, "Thread-2", 2, diff_ip[2])
    thread3 = myThread(3, "Thread-3", 3, diff_ip[3])
    thread4 = myThread(4, "Thread-4", 4, diff_ip[4])
    thread5 = myThread(5, "Thread-5", 5, diff_ip[5])
    thread6 = myThread(6, "Thread-6", 6, diff_ip[6])
    thread7 = myThread(7, "Thread-7", 7, diff_ip[7])
    thread8 = myThread(8, "Thread-8", 8, diff_ip[8])    
    thread9 = myThread(9, "Thread-9", 9, diff_ip[9])
    
    thread0.start()
    """
    thread1.start()
    thread2.start()
    thread3.start()    
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()     
    thread8.start()
    thread9.start()    
    """
    
    
