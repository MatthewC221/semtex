#!/usr/bin/python2

# Simple Crypto

import sys

temp = "TGPRGWTADEKI HI3OYNODONAT ES4LOCIINTB} FC4LURSDTHO_ LO1IRYAEEIU_ AM{NOPBAVNT_"
count = 0
position = 0
while (count < len(temp)):
    sys.stdout.write(temp[position])
    position = position + 13
    if (position >= len(temp)):
        position = position - len(temp)
    count += 1
