#!/usr/bin/python

import sys

if (len(sys.argv) != 4):
    print ("./crack_diffie_part2.py <value> <power> <mod>")
else:
    num = int(sys.argv[1]) ** int(sys.argv[2])
    print num
    remainder = num % int(sys.argv[3])
    print remainder
