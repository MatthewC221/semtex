#!/usr/bin/python

import sys
import hashlib
import re

# Another attempt at merkle!

merkle = open("merkle.txt", "r")
salt_hash = open("hash.txt", "r")
count = 0

for line in salt_hash:
    match = re.search("salt:(.*) hash:(.*)", line)
    temp_salt = match.group(1)
    temp_hash = match.group(2)
    temp_hash = temp_hash.strip()
    print temp_hash
    sha_1 = hashlib.sha1()
    print "Index " + str(count)
    print "Salt = " + temp_salt
    print "Hash = " + temp_hash
    for m_line in merkle:
        m_line = m_line.strip()
        temp_string = "COMP3441{" + m_line + ":" + temp_salt + "}"
        print temp_string
        sha_1.update(temp_string)
        if (sha_1.hexdigest() == temp_hash):
            print sha_1.hexdigest()
    count += 1
    merkle.seek(0, 0)
    
        
