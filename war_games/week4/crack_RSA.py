#!/usr/bin/python

import sys

# Crack RSA

if (len(sys.argv) != 4):
    print ("./crack_RSA.py <exponent> <key> <message>")
else:
    exponent = int(sys.argv[1])
    key = int(sys.argv[2])
    message = int(sys.argv[3])
    
    attempt = 1
    while (1):
        if ((attempt ** exponent) % key == message):
            print attempt
            break
        attempt += 1
