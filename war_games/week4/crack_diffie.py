#!/usr/bin/python

import sys

# Crack Diffie

if (len(sys.argv) != 5):
    print ("./crack_diffie.py <gen> <mod> <a_mod> <b_mod>")
else:
    generator = int(sys.argv[1])
    mod = int(sys.argv[2])
    secret = int(sys.argv[3])
    other_person = int(sys.argv[4])
    
    alice_secret = 1
    while (1):
        if ((generator ** alice_secret) % mod == secret):
            break
        alice_secret += 1
    
    num = other_person ** alice_secret
    remainder = num % mod
    print remainder
